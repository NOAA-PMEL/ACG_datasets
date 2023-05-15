import json
import glob
import os
from erddapy import ERDDAP
from urllib.request import urlretrieve
from netCDF4 import Dataset, date2num
import numpy as np
import pandas as pd
import xarray as xr
from datetime import datetime, timedelta

import data.config.project_config as proj_config
import data.config.dataset_config_size_dist as ds_config
import data.config.readme as readme_config

base_path = os.path.join(os.getcwd(), "data")


def create_project_datasets(project_id: str):
    input_path = os.path.join(base_path, "input", project_id)
    # with open(os.path.join(input_path,"config", f"dataset_config.json"), "r") as f:
    # dataset_config = json.load(f)
    dataset_config = ds_config.dataset_config[project_id]
    for dataset in dataset_config.keys():
        create_dataset(project_id=project_id, dataset=dataset)


def create_dataset(project_id: str, dataset: str, cf: bool = True):
    tmpl_input_path = os.path.join(base_path, "templates", "input")
    # output_path = os.path.join(base_path, "output", project)
    input_path = os.path.join(base_path, "input", project_id)
    output_path = os.path.join(base_path, "output", project_id)

    with open(os.path.join(tmpl_input_path, f"MAIN_dataset_tmpl_all.json"), "r") as f:
        tmpl = json.load(f)

    variable_names = dict()
    with open(os.path.join(tmpl_input_path, f"MAIN_variable_names_map.csv"), "r") as f:
        f.readline()
        for line in f:
            parts = line.strip().split(",")
            if parts[0] not in variable_names:
                variable_names[parts[0]] = {"old_name": parts[1], "dataset": parts[2]}

    platforms = proj_config.platforms
    project_config = proj_config.project_config[project_id]

    # with open(os.path.join(input_path,"config", f"dataset_config.json"), "r") as f:
    #     dataset_config = json.load(f)
    dataset_config = ds_config.dataset_config[project_id]

    # with open(os.path.join(input_path,"config", f"readme.json"), "r") as f:
    #     readme = json.load(f)
    readme = readme_config.readme[project_id]
    # create data
    data = dict()
    data["attributes"] = tmpl["attributes"]
    data["dimensions"] = ""
    data["variables"] = {}
    for name, map in variable_names.items():
        try:
            if map["dataset"] in dataset_config[dataset]["map"]:
                data["variables"][name] = tmpl["variables"][name]
        except KeyError:
            pass

    source_data = dict()
    # source_ds = dict()
    files = glob.glob(os.path.join(input_path, "netcdf", "*.cdf"))
    for source in dataset_config[dataset]["source"]:
        for file in files:
            # print(f"file: {os.path.basename(file)}")
            if f"_{source}_" in os.path.basename(
                file
            ) or f"_{source}." in os.path.basename(file):
                ds = xr.open_dataset(file)
                source_data[source] = ds
                # print(f"size of {source}: {len(ds.time)}")
                break

    # handle the special data
    source = dataset_config[dataset]["source"][0]
    ds = source_data[source]

    # get common global attributes
    # proj = ds.attrs["PROJECT"]
    # platform = ds.attrs["PLATFORM"]
    project = project_config["project"]
    platform = project_config["platform"]
    contrib_source = ds.attrs["SOURCE"]
    product_version = ds.attrs["VERSION"]

    platform_id = "Unknown"
    for id, pform in platforms.items():
        if pform["name"] == platform:
            platform_id = id
            break

    # proj = data["attributes"]["project"]["data"]
    # proj.replace("<PROJECT>", project)
    if cf:
        # data["attributes"]["Conventions"] = {"type": "string", "data": "COARDS, CF-1.6, ACDD-1.3"} #, NCCSV-1.0"}
        data["attributes"]["featureType"] = {"type": "string", "data": "Trajectory"}

        data["variables"]["latitude"]["attributes"]["_CoordinateAxisType"] = {
            "type": "string",
            "data": "Lat",
        }
        data["variables"]["latitude"]["attributes"]["axis"] = {
            "type": "string",
            "data": "Y",
        }
        data["variables"]["latitude"]["attributes"]["ioos_category"] = {
            "type": "string",
            "data": "Location",
        }

        data["variables"]["longitude"]["attributes"]["_CoordinateAxisType"] = {
            "type": "string",
            "data": "Lon",
        }
        data["variables"]["longitude"]["attributes"]["axis"] = {
            "type": "string",
            "data": "X",
        }
        data["variables"]["longitude"]["attributes"]["ioos_category"] = {
            "type": "string",
            "data": "Location",
        }

        # data[]
    data["attributes"]["project"]["data"] = project
    data["attributes"]["platform"]["data"] = platform
    data["attributes"]["contributor_name"]["data"] = contrib_source
    data["attributes"]["product_version"]["data"] = product_version
    data["attributes"]["infoUrl"] = {
        "type": "string",
        "data": "https://saga.pmel.noaa.gov/data/index.html",
    }

    title = data["attributes"]["title"]["data"]
    title = title.replace("<PROJECT>", project).replace("<DATASET>", dataset)
    data["attributes"]["title"]["data"] = title

    altitude = []
    trajectory_id = []
    # data["variables"]["trajectory_id"]["shape"] = ["trajectory_id"]
    # data["variables"]["trajectory_id"]["data"] = [f"{project}_{platform}"]

    dt = []
    for t in ds["time"].values:
        dt.append(pd.Timestamp(t).to_pydatetime().strftime("%Y-%m-%dT%H:%M:%SZ"))
        trajectory_id.append(f"{project}_{platform}")
        altitude.append(platforms[platform_id]["inlet_height"])
    data["variables"]["time"]["data"] = dt
    data["variables"]["trajectory_id"]["data"] = trajectory_id
    data["variables"]["altitude"]["data"] = altitude

    data["variables"]["duration"]["data"] = list(
        ds[variable_names["duration"]["old_name"]].values * 60.0
    )

    try:
        mid = []
        end = []
        for dts, dur in zip(
            data["variables"]["time"]["data"], data["variables"]["duration"]["data"]
        ):
            dt = datetime.strptime(dts, "%Y-%m-%dT%H:%M:%SZ")
            stop = dt + timedelta(seconds=dur)
            middle = dt + timedelta(seconds=(dur / 2))
            # middle = (dt+stop) / 2.
            mid.append(middle.strftime("%Y-%m-%dT%H:%M:%SZ"))
            end.append(stop.strftime("%Y-%m-%dT%H:%M:%SZ"))
        data["variables"]["mid_time"]["data"] = mid
        data["variables"]["end_time"]["data"] = end
    except KeyError:
        pass

    # comment = []
    for source, ds in source_data.items():
        for name, var in data["variables"].items():
            if name != "trajectory_id":
                data["variables"][name]["shape"] = ["time"]

            if name in ["time", "trajectory_id", "duration"]:
                continue
            try:
                data["variables"][name]["data"] = list(
                    ds[variable_names[name]["old_name"]].values
                )
            except KeyError as e:
                # print(f"key not found: {name}, {source}, {e}")
                pass

    #     source_comment = []
    #     for name, att in ds.attrs.items():
    #         if "REMARK_" in name:
    #             source_comment.append(att)
    #     if source_comment:
    #         comment.append(" ".join(source_comment))

    # if comment:
    #     data["attributes"]["comment"] = ";\n".join(comment)

    if dataset in readme:
        data["attributes"]["comment"]["data"] = readme[dataset]

    variables = list(data["variables"].keys())
    for name in variables:
        if len(data["variables"][name]["data"]) == 0:
            data["variables"].pop(name)

    os.makedirs(output_path, exist_ok=True)
    with open(
        os.path.join(
            output_path, f"{project}_{platform}_{dataset}_v{product_version}.json"
        ),
        "w",
    ) as f:
        json.dump(data, f)

    with open(
        os.path.join(
            output_path, f"{project}_{platform}_{dataset}_v{product_version}.csv"
        ),
        "w",
    ) as f:
        f.write('*GLOBAL*,Conventions,"COARDS, CF-1.6, ACDD-1.3, NCCSV-1.0"\n')
        for name, attr in data["attributes"].items():
            value = attr["data"]
            if type(value) == str:
                # # value = value.replace('"', '').replace('\"', '').strip()#.replace("\n",";")
                # value = value.strip().replace('"', '').replace('\"', '')
                # # value = value.replace("\n\n", "\n").replace("\n","<__nl__>")
                # # parts = value.split("<__nl__>")
                # # if len(parts) > 1:
                # #     value = "\n".join(parts)
                if value:
                    if value[0] == "'" or value[0] == '"':
                        value = value[1:]
                    if value[-1] == "'" or value[-1] == '"':
                        value = value[:-1]
                cleaned = []
                value = value.strip()
                # for part in value.split("\n"):
                #     part.strip().replace("\r", "")
                # cleaned.append(json.loads(json.dumps(part)))
                # value = '\n'.join(cleaned)
                # value = json.dumps(value)
                # value = f'"{value}"'
                # f.write(f'*GLOBAL*,{name},{repr(json.dumps(value))}\n')
                # f.write(f"*GLOBAL*,{name},{repr(value)}\n")
                f.write(f"*GLOBAL*,{name},{json.dumps(value)}\n")
                pass
            else:
                f.write(f"*GLOBAL*,{name},{value}\n")
        for name, var in data["variables"].items():
            f.write(f"{name},*DATA_TYPE*,{var['type']}\n")
            for vname, attr in var["attributes"].items():
                value = attr["data"]
                if type(value) == str:
                    # value = value.strip().replace('"', '').replace("\n\n","\n")
                    # value = value.strip().replace('"', '').replace('\"', '')
                    # value = f'"{repr(value)}"'
                    f.write(f"{name},{vname},{json.dumps(value)}\n")
                else:
                    f.write(f"{name},{vname},{value}\n")
        f.write("*END_METADATA*\n")

        f.write(f'{",".join(data["variables"].keys())}\n')
        for index, item in enumerate(data["variables"]["time"]["data"]):
            line = []
            try:
                for name, var in data["variables"].items():
                    if name == "trajectory_id":
                        line.append(var["data"][0])
                    else:
                        line.append(str(var["data"][index]))
                f.write(f'{",".join(line)}\n')
            except IndexError as e:
                src = [x for x in dataset_config[dataset]["source"]]
                print(f"index error: {project_id}, {dataset}, {src}, error: {e}")
                raise
        f.write("*END_DATA*\n")
    pass

def create_project_datasets_size_dist(project_id: str):
    input_path = os.path.join(base_path, "input", project_id)
    # with open(os.path.join(input_path,"config", f"dataset_config.json"), "r") as f:
    # dataset_config = json.load(f)
    dataset_config = ds_config.dataset_config[project_id]
    for dataset in dataset_config.keys():
        create_dataset_size_dist(project_id=project_id, dataset=dataset)

def create_dataset_size_dist(project_id: str, dataset: str, cf: bool = True):
    tmpl_input_path = os.path.join(base_path, "templates", "input")
    # output_path = os.path.join(base_path, "output", project)
    input_path = os.path.join(base_path, "input", project_id)
    output_path = os.path.join(base_path, "output", project_id)

    with open(
        os.path.join(tmpl_input_path, f"MAIN_size_dist_dataset_tmpl_all.json"), "r"
    ) as f:
        tmpl = json.load(f)

    # variable_names = dict()
    # with open(os.path.join(tmpl_input_path, f"MAIN_variable_names_map.csv"), "r") as f:
    #     f.readline()
    #     for line in f:
    #         parts = line.strip().split(",")
    #         if parts[0] not in variable_names:
    #             variable_names[parts[0]] = {"old_name": parts[1], "dataset": parts[2]}

    platforms = proj_config.platforms
    project_config = proj_config.project_config[project_id]

    # with open(os.path.join(input_path,"config", f"dataset_config.json"), "r") as f:
    #     dataset_config = json.load(f)
    dataset_config = ds_config.dataset_config[project_id]

    # with open(os.path.join(input_path,"config", f"readme.json"), "r") as f:
    #     readme = json.load(f)
    readme = readme_config.readme[project_id]
    # create data
    data = dict()
    data["attributes"] = tmpl["attributes"]
    data["dimensions"] = {}
    data["variables"] = {}
    variable_names = ["time", "dNdlogDp"]
    # for name, map in variable_names.items():
    # for name in variable_names:
    #     try:
    #         # if map["dataset"] in dataset_config[dataset]["map"]:
    #         data["variables"][name] = tmpl["variables"][name]
    #     except KeyError:
    #         pass

    source_data = dict()
    # source_ds = dict()
    files = glob.glob(os.path.join(input_path, "size_distribution", "*.csv"))
    for sd_var, source in zip(dataset_config[dataset]["map"],dataset_config[dataset]["source"]):
        for file in files:
            # print(f"file: {os.path.basename(file)}")
            if f"_{source}_v" in os.path.basename(
                file
            ):  # or f"_{source}." in os.path.basename(file):
                # ds = xr.open_dataset(file)
                # source_data[source] = ds
                # print(f"size of {source}: {len(ds.time)}")
                sd_file = os.path.basename(file)
                product_version = "0"
                if (index := sd_file.find("_v")) >= 0:
                    product_version = sd_file[index:].replace("_v", "").replace(".csv", "")
                source_data[sd_var] = {"source_file": sd_file, "product_version": product_version}
                # break

    # product_version = "0"
    # if (index := sd_file.find("_v")) >= 0:
    #     product_version = sd_file[index:].replace("_v", "").replace(".csv", "")

    data["variables"]["time"] = tmpl["variables"]["time"]
    file = dataset_config[dataset]["source"][0]
    if "dmps" in dataset:
        diam_var = "diameter"
    elif "aps" in dataset:
        diam_var = "diameter_aero"

    data["variables"][diam_var] = tmpl["variables"][diam_var]
    # data["variables"]["dNdlogDp"] = tmpl["variables"]["dNdlogDp"]

    project = project_config["project"]
    platform = project_config["platform"]
    # contrib_source = ds.attrs["SOURCE"]
    # product_version = ds.attrs["VERSION"]

    dp = []
    doy = []
    dt = []
    for sd_var, source in source_data.items():
        sd_file = source["source_file"]
        product_version = source["product_version"]
        dndlogdp = []
        data["variables"][sd_var] = tmpl["variables"][sd_var]
        # sd_file = source
        with open(os.path.join(input_path, "size_distribution", sd_file), "r") as f:
            f.readline()
            line = f.readline()
            parts = line.strip().split(",")
            first_dp = 0
            for idx, item in enumerate(parts):
                if item == "1":
                    first_dp = idx
                    break

            dpline = f.readline()
            parts = dpline.strip().split(",")
            test = parts[first_dp:]
            if len(dp) == 0:
                dp = [float(x) for x in parts[first_dp:]]

            if project in [
                "ATOMIC",
                "NAAMES1",
                "NAAMES2",
                "NAAMES3",
                "NAAMES4",
            ]:  # time is in datetime string
                # f.readline()
                for line in f:
                    parts = line.strip().split(",")
                    if parts:
                        dt.append(parts[0])
                        dndlogdp.append([None if float(x)<0 else float(x) for x in parts[first_dp:]])

                newdt = []
                for t in dt:
                    test = datetime.strptime(t, "%Y-%m-%d %H:%M:%S")
                    newdt.append(
                        datetime.strptime(t, "%Y-%m-%d %H:%M:%S").strftime(
                            "%Y-%m-%dT%H:%M:%SZ"
                        )
                    )
                if len(data["variables"]["time"]["data"]) == 0:
                    data["variables"]["time"]["data"] = newdt
            else:
                for line in f:
                    parts = line.strip().split(",")
                    doy.append(parts[0])
                    dndlogdp.append([None if float(x)<0 else float(x) for x in parts[first_dp:]])

                # convert time
                year = dataset_config[dataset]["year"]
                jan1 = datetime(year, 1, 1)
                dt = []
                last = None
                for d in doy:
                    ddoy = float(d)
                    if last and ddoy < last:  # increment year
                        jan1 = datetime(year + 1, 1, 1)
                    dt.append((jan1 + timedelta(days=ddoy)).strftime("%Y-%m-%dT%H:%M:%SZ"))
                    last = ddoy

                if len(data["variables"]["time"]["data"]) == 0:
                    data["variables"]["time"]["data"] = dt

        data["variables"][sd_var]["data"] = dndlogdp
    data["variables"][diam_var]["data"] = dp

    data["dimensions"]["time"] = len(data["variables"]["time"]["data"])
    data["dimensions"][diam_var] = len(data["variables"][diam_var]["data"])
    # print(f'time, dndlogdp: {len(data["variables"]["time"]["data"])}, {len(data["variables"]["dNdlogDp"]["data"])}')
    # print(f'{data["variables"]["dNdlogDp"]["data"][0]}\n{data["variables"]["dNdlogDp"]["data"][-1]}')
    # print(f'{data["variables"]["time"]["data"][0]}\n{data["variables"]["time"]["data"][-1]}')
    # print(f'{doy[0]}\n{doy[-1]}')
    # print(f'{len(doy)}, {len(dt)}')
    # ds["dNdlogDp"] = xr.DataArray(data["variables"]["dNdlogDp"]["data"], dims=["time", diam_var])
    # for name,attr in data["variables"]["dNdlogDp"]["attributes"].items():
    #     ds.dNdlogDp.attrs[name] = attr["data"]

    # ds.to_netcdf("test_sd.nc")
    # # convert time
    # year = dataset_config[dataset]["year"]
    # jan1 = datetime(year, 1, 1)
    # dt = []
    # last = None
    # for d in doy:
    #     if last and d < last: # increment year
    #         jan1 = datetime(year+1, 1, 1)
    #     dt.append(jan1 + timedelta(days=d))
    #     last =  d

    # data["variables"][diam_var]["time"]["data"] = dt

    # return

    # handle the special data
    # source = dataset_config[dataset]["source"][0]
    # ds = source_data[source]

    # get common global attributes
    # proj = ds.attrs["PROJECT"]
    # platform = ds.attrs["PLATFORM"]
    project = project_config["project"]
    platform = project_config["platform"]
    # contrib_source = ds.attrs["SOURCE"]
    # product_version = ds.attrs["VERSION"]

    platform_id = "Unknown"
    for id, pform in platforms.items():
        if pform["name"] == platform:
            platform_id = id
            break

    # proj = data["attributes"]["project"]["data"]
    # proj.replace("<PROJECT>", project)
    # if cf:
    #     # data["attributes"]["Conventions"] = {"type": "string", "data": "COARDS, CF-1.6, ACDD-1.3"} #, NCCSV-1.0"}
    #     data["attributes"]["featureType"] = {"type": "string", "data": "Trajectory"}

    #     data["variables"]["latitude"]["attributes"]["_CoordinateAxisType"] = {
    #         "type": "string",
    #         "data": "Lat",
    #     }
    #     data["variables"]["latitude"]["attributes"]["axis"] = {
    #         "type": "string",
    #         "data": "Y",
    #     }
    #     data["variables"]["latitude"]["attributes"]["ioos_category"] = {
    #         "type": "string",
    #         "data": "Location",
    #     }

    #     data["variables"]["longitude"]["attributes"]["_CoordinateAxisType"] = {
    #         "type": "string",
    #         "data": "Lon",
    #     }
    #     data["variables"]["longitude"]["attributes"]["axis"] = {
    #         "type": "string",
    #         "data": "X",
    #     }
    #     data["variables"]["longitude"]["attributes"]["ioos_category"] = {
    #         "type": "string",
    #         "data": "Location",
    #     }

    # data[]
    data["attributes"]["project"]["data"] = project
    data["attributes"]["platform"]["data"] = platform
    data["attributes"]["contributor_name"]["data"] = ""
    data["attributes"]["product_version"]["data"] = product_version
    data["attributes"]["infoUrl"] = {
        "type": "string",
        "data": "https://saga.pmel.noaa.gov/data/index.html",
    }

    title = data["attributes"]["title"]["data"]
    title = title.replace("<PROJECT>", project).replace("<DATASET>", dataset)
    data["attributes"]["title"]["data"] = title

    # altitude = []
    # trajectory_id = []
    # # data["variables"]["trajectory_id"]["shape"] = ["trajectory_id"]
    # # data["variables"]["trajectory_id"]["data"] = [f"{project}_{platform}"]

    # dt = []
    # for t in ds["time"].values:
    #     dt.append(pd.Timestamp(t).to_pydatetime().strftime("%Y-%m-%dT%H:%M:%SZ"))
    #     trajectory_id.append(f"{project}_{platform}")
    #     altitude.append(platforms[platform_id]["inlet_height"])
    # data["variables"]["time"]["data"] = dt
    # data["variables"]["trajectory_id"]["data"] = trajectory_id
    # data["variables"]["altitude"]["data"] = altitude

    # data["variables"]["duration"]["data"] = list(
    #     ds[variable_names["duration"]["old_name"]].values * 60.0
    # )

    # try:
    #     mid = []
    #     end = []
    #     for dts, dur in zip(
    #         data["variables"]["time"]["data"], data["variables"]["duration"]["data"]
    #     ):
    #         dt = datetime.strptime(dts, "%Y-%m-%dT%H:%M:%SZ")
    #         stop = dt + timedelta(seconds=dur)
    #         middle = dt + timedelta(seconds=(dur / 2))
    #         # middle = (dt+stop) / 2.
    #         mid.append(middle.strftime("%Y-%m-%dT%H:%M:%SZ"))
    #         end.append(stop.strftime("%Y-%m-%dT%H:%M:%SZ"))
    #     data["variables"]["mid_time"]["data"] = mid
    #     data["variables"]["end_time"]["data"] = end
    # except KeyError:
    #     pass

    # # comment = []
    # for source, ds in source_data.items():
    #     for name, var in data["variables"].items():
    #         if name != "trajectory_id":
    #             data["variables"][name]["shape"] = ["time"]

    #         if name in ["time", "trajectory_id", "duration"]:
    #             continue
    #         try:
    #             data["variables"][name]["data"] = list(
    #                 ds[variable_names[name]["old_name"]].values
    #             )
    #         except KeyError as e:
    #             # print(f"key not found: {name}, {source}, {e}")
    #             pass

    # #     source_comment = []
    # #     for name, att in ds.attrs.items():
    # #         if "REMARK_" in name:
    # #             source_comment.append(att)
    # #     if source_comment:
    # #         comment.append(" ".join(source_comment))

    # # if comment:
    # #     data["attributes"]["comment"] = ";\n".join(comment)

    if dataset in readme:
        data["attributes"]["comment"]["data"] = readme[dataset]

    variables = list(data["variables"].keys())
    for name in variables:
        if len(data["variables"][name]["data"]) == 0:
            data["variables"].pop(name)

    ds = xr.Dataset(
        coords={
            "time": data["variables"]["time"]["data"],
            diam_var: data["variables"][diam_var]["data"],
        }
    )
    for name, attr in data["variables"]["time"]["attributes"].items():
        ds.time.attrs[name] = attr["data"]

    for name, attr in data["variables"][diam_var]["attributes"].items():
        ds[diam_var].attrs[name] = attr["data"]

    for name, variable in data["variables"].items():
        if name not in ["time", diam_var]:
            ds[name] = xr.DataArray(
                data["variables"][name]["data"], dims=["time", diam_var]
            )
            for attname, attr in data["variables"][name]["attributes"].items():
                ds[name].attrs[attname] = attr["data"]

    for attname, attr in data["attributes"].items():
        ds.attrs[attname] = attr["data"]
    # ds.to_netcdf("test_sd.nc")

    output_path_gridded = os.path.join(output_path, "gridded")
    output_path_gridded_json = os.path.join(output_path, "gridded", "json")
    os.makedirs(output_path_gridded_json, exist_ok=True)
    # os.makedirs(output_path, exist_ok=True)
    with open(
        os.path.join(
            output_path_gridded_json, f"{project}_{platform}_{dataset}_v{product_version}.json"
        ),
        "w",
    ) as f:
        json.dump(data, f)

    ds.to_netcdf(
        os.path.join(
            output_path_gridded, f"{project}_{platform}_{dataset}_v{product_version}.nc"
        )
    )
    # with open(
    #     os.path.join(
    #         output_path, f"{project}_{platform}_{dataset}_v{product_version}.csv"
    #     ),
    #     "w",
    # ) as f:
    #     f.write('*GLOBAL*,Conventions,"COARDS, CF-1.6, ACDD-1.3, NCCSV-1.0"\n')
    #     for name, attr in data["attributes"].items():
    #         value = attr["data"]
    #         if type(value) == str:
    #             # # value = value.replace('"', '').replace('\"', '').strip()#.replace("\n",";")
    #             # value = value.strip().replace('"', '').replace('\"', '')
    #             # # value = value.replace("\n\n", "\n").replace("\n","<__nl__>")
    #             # # parts = value.split("<__nl__>")
    #             # # if len(parts) > 1:
    #             # #     value = "\n".join(parts)
    #             if value:
    #                 if value[0] == "'" or value[0] == '"':
    #                     value = value[1:]
    #                 if value[-1] == "'" or value[-1] == '"':
    #                     value = value[:-1]
    #             cleaned = []
    #             value = value.strip()
    #             # for part in value.split("\n"):
    #             #     part.strip().replace("\r", "")
    #             # cleaned.append(json.loads(json.dumps(part)))
    #             # value = '\n'.join(cleaned)
    #             # value = json.dumps(value)
    #             # value = f'"{value}"'
    #             # f.write(f'*GLOBAL*,{name},{repr(json.dumps(value))}\n')
    #             # f.write(f"*GLOBAL*,{name},{repr(value)}\n")
    #             f.write(f"*GLOBAL*,{name},{json.dumps(value)}\n")
    #             pass
    #         else:
    #             f.write(f"*GLOBAL*,{name},{value}\n")
    #     for name, var in data["variables"].items():
    #         f.write(f"{name},*DATA_TYPE*,{var['type']}\n")
    #         for vname, attr in var["attributes"].items():
    #             value = attr["data"]
    #             if type(value) == str:
    #                 # value = value.strip().replace('"', '').replace("\n\n","\n")
    #                 # value = value.strip().replace('"', '').replace('\"', '')
    #                 # value = f'"{repr(value)}"'
    #                 f.write(f"{name},{vname},{json.dumps(value)}\n")
    #             else:
    #                 f.write(f"{name},{vname},{value}\n")
    #     f.write("*END_METADATA*\n")

    #     f.write(f'{",".join(data["variables"].keys())}\n')
    #     for index, item in enumerate(data["variables"]["time"]["data"]):
    #         line = []
    #         try:
    #             for name, var in data["variables"].items():
    #                 if name == "trajectory_id":
    #                     line.append(var["data"][0])
    #                 else:
    #                     line.append(str(var["data"][index]))
    #             f.write(f'{",".join(line)}\n')
    #         except IndexError as e:
    #             src = [x for x in dataset_config[dataset]["source"]]
    #             print(f"index error: {project_id}, {dataset}, {src}, error: {e}")
    #             raise
    #     f.write("*END_DATA*\n")
    pass


def write_project_config():
    # project_config = proj_config.project_config

    with open("proj_config.csv", "w") as f:
        f.write("project_id,parameter,value\n")
        for project_id, project in proj_config.project_config.items():
            f.write("\n")
            for param, value in project.items():
                f.write(f"{project_id},{param},{value}\n")
            traj_id = f'{project["project"]}_{project["platform"]}'
            f.write(f"{project_id},trajectory_id,{traj_id}\n")


if __name__ == "__main__":
    # write_project_variables()
    # build_dataset_merge()
    # create_dataset_meta("CALNEX", "inorganic_ion_chemistry")
    # create_dataset_templates()
    # create_atomic_dataset_meta("BASE")
    # create_atomic_dataset_templates()

    # rewrite_variable_map("CALNEX")
    # create_main_dataset_templates()
    # save_main_tmpl_as_json()

    # create_dataset(project="CALNEX", dataset="main")

    # write_project_config()
    # exit()

    projects = [
        "ATOMIC",
        # "NAAMES4",
        # "NAAMES3",
        # "NAAMES2",
        # "NAAMES1",
        # "WACS2014",
        # "WACS2012",
        # "DYNAMO",
        "CALNEX",
        # "VOCALS",
        # "ICEALOT",
        # "TEXAQS2006",
        # "NEAQS2004", ###
        # "NEAQS2002",
        # "ACEASIA",
        # "NAURU99",
        # "AEROINDO99",
        # "ACE2",
        # "CSP",
        # "ACE1",
        # "RITS94",
        # "RITS93",
        # "MAGE92",
        # "PSI3",
    ]
    # projects = ["NAAMES2", "NAAMES1"]
    # projects = ["WACS2014"]

    # create_dataset_size_dist("ATOMIC", dataset="nsd_dmps_aps")
    # create_project_datasets_size_dist(project_id="CALNEX")
    # exit()
    for proj in projects:
        try:
            print(f"Project: {proj}...")
            create_project_datasets_size_dist(project_id=proj)
            print(f"Project: {proj}...done")
        # create_project_datasets(project_id="NAAMES4")
        except Exception as e:
            print(f"error: {proj} - {e}")
            pass
    # TODO
    # Create project config: project, platform, events?, trajectory_id and ??
    # One trajectory per file
    # Can use ncCSV or netCDF
