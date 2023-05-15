import json
import glob
import os
import pandas as pd
from erddapy import ERDDAP
from urllib.request import urlretrieve

base_path = os.path.join(os.getcwd(), "data")

projects = [
    "ACE1",
    "ACE2",
    "ACEASIA",
    "AEROSOLS_INDOEX99",
    "ATOMIC",
    "CALNEX",
    "DYNAMO",
    "ICEALOT",
    "MAGE92",
    "NAAMES1",
    "NAURU99",
    "NEAQS2002",
    "NEAQS2004",
    "RITS93",
    "RITS94",
    "TEXAQS2006",
    "TEXAQSS2006",
    # "UBWOS",
    # "UBWOS-2013",
    # "UBWOS2014",
    "VOCALS",
    "WACS2012",
    "WACS2014",
]


def download_ncojson_files():

    e = ERDDAP(server="https://data.pmel.noaa.gov/pmel/erddap")
 
    for project in projects:
        print(f"Project: {project}")
        url = e.get_search_url(search_for=project, response="csv")
        df = pd.read_csv(url)
        for id in df["Dataset ID"].values.tolist():
            print(f"Dataset ID: {id}")
            info_url = e.get_info_url(dataset_id=id, response="csv")
            df2=pd.read_csv(info_url)
            last_time = df2.loc[df2["Attribute Name"] == "time_coverage_end", "Value"].values[0]
            print(f"last_time {last_time}")
            dl_url = e.get_download_url(
                dataset_id=id, 
                protocol="tabledap", 
                response="ncoJson", 
                # constraints={"time>=": last_time},
                relative_contraints={"time>=": f"{last_time}-1hour"},
            )
            print(f"dl_url: {dl_url}")
            input_path = os.path.join(base_path,"input", project)
            os.makedirs(input_path, exist_ok=True)
            filename = f"{id}.json"
            print(f"filename: {filename}")
            urlretrieve(dl_url, os.path.join(input_path, filename))
            # exit()



def create_var_forms():
    dir_path = os.path.join(os.getcwd(), "data", "input", "atomic", "*.json")
    output_path = os.path.join(os.getcwd(), "data", "output")
    files = glob.glob(dir_path)
    
    common_global_atts = {
        "comment": "",
        "contributor_name": "",
        "creator_name": "",
        "creator_email": "",
        "creator_url": "",
        "history": "",
        "platform": "",
        "product_version": "",
        "project": "",
        "sourceUrl": "",
        "title": "",
    }

    old_atts_map = {
        "platform": "PLATFORM",
        "project": "PROJECT",
        "product_version": 
    }

    common_var_atts = {
        "long_name": "",
        "units": "",
        "instrument": "",
        "source": "surface observation",
        "valid_min": None,
        "valid_max": None,
        "uncertainty": "",
        "standard_name": "",
        "ioos_category": "",
        "history": "",
        "comment": "",
        "description": "",

    }

    old_var_atts_map = {
        "instrument":"instr_id",
        "valid_min":"min_value",
        "valid_max":"max_value",

    }

    for project in projects:

        input_path = os.path.join(base_path, "input", project)
        output_path = os.path.join(base_path, "output", project)
        files = glob.glob(os.path.join(input_path, "*.json"))

        os.makedirs(output_path, exist_ok=True)

        if project == "ATOMIC":

            for file in files:
                with open(file, "r") as f:
                    input = json.load(f)
            
                dset = {"attributes": {}, "variables": {}}
                for name, att in common_global_atts.items():
                    dset["attributes"][name] = None
                    if name in input["attributes"]:
                        dset["attributes"][name] = input["attributes"][name]["data"]

                for name, var in input["variables"].items():
                    if name not in ["time", "latitude", "longitude", "trajectory_id"]:
                        dset["variables"][name] = dict()
                        for attname, att in common_var_atts.items():
                            if attname in var["attributes"]:
                                dset["variables"][name][attname] = var["attributes"][attname]["data"]
                            else:
                                dset["variables"][name][attname] = att

                # print(f"{project} - {file}: {dset}")    
                # for name, att in common_var_atts.items():
                #     if name in input["variables"]["attributes"]

                # # print(input["variables"])
                # for name, var in input["variables"].items():
                #     if name not in ["time", "latitude", "longitude"]:
                #         print(f"{name}: {var}")
                #         print("\n")
                
                outfile = os.path.join(output_path, os.path.basename(file))
                outfile = outfile.replace(".json", ".csv")
                with open(outfile, "w") as f:
                    f.write("**START GLOBAL**\n\n")
                    f.write("Current parameter,Proposed parameter,Value\n")
                    for name, att in dset["attributes"].items():
                        # print(name, att)
                        if type(att) == str:
                            row = f'{name},,"{att}"'
                        else:
                            row = f'{name},,{att}'
                        f.write(row)
                        f.write("\n")
                    f.write("\n")
                    f.write("**END GLOBAL**\n\n")


                    f.write("**START VARIABLES**\n\n")
                    f.write("proposed parameter\n")
                    header = [
                        "current parameter",
                        "current_variable",
                        "proposed_variable",
                    ]
                    for param,_ in common_var_atts.items():
                        header.append(param)

                    f.write(",".join(header))
                    f.write("\n")
                    for name, var in dset["variables"].items():
                        row = ["", name, ""]
                        for attname, att in var.items():
                            # print(name, att)
                            if type(att) == str:
                                if att is None:
                                    att = ""
                                row.append(f'"{att}"')
                                # row = f'{name},{attname},"{att}"'
                            else:
                                if att is None:
                                    att = ""
                                row.append(f"{att}")
                                # row = f'{name},{attname},{att}'
                        f.write(",".join(row))
                        f.write("\n")
                    f.write("\n")
                    f.write("**END VARIABLES**\n\n")
        else:

            for file in files:
                with open(file, "r") as f:
                    input = json.load(f)
            
                dset = {"attributes": {}, "variables": {}}
                for name, att in common_global_atts.items():
                    dset["attributes"][name] = None
                    if name in input["attributes"]:
                        # if name.lower() in {k.lower():v for k,v in input["attributes"].items()}:
                        dset["attributes"][name] = input["attributes"][name]["data"]
                    elif name in old_atts_map:
                        dset["attributes"][name] = input["attributes"][old_atts_map[name]]["data"]

                for name, var in input["variables"].items():
                    if name not in ["time", "latitude", "longitude", "altitude", "depth", "trajectory_id", "traj", "id"]:
                        dset["variables"][name] = dict()
                        for attname, att in common_var_atts.items():
                            if attname in var["attributes"]:
                                dset["variables"][name][attname] = var["attributes"][attname]["data"]
                            else:
                                dset["variables"][name][attname] = att

                # print(f"{project} - {file}: {dset}")    
                # for name, att in common_var_atts.items():
                #     if name in input["variables"]["attributes"]

                # # print(input["variables"])
                # for name, var in input["variables"].items():
                #     if name not in ["time", "latitude", "longitude"]:
                #         print(f"{name}: {var}")
                #         print("\n")
                
                outfile = os.path.join(output_path, os.path.basename(file))
                outfile = outfile.replace(".json", ".csv")
                with open(outfile, "w") as f:
                    f.write("**START GLOBAL**\n\n")
                    f.write("Current parameter,Proposed parameter,Value\n")
                    for name, att in dset["attributes"].items():
                        # print(name, att)
                        if att is None:
                            att = ""
                        if type(att) == str:
                            row = f'{name},,"{att}"'
                        else:
                            row = f'{name},,{att}'
                        f.write(row)
                        f.write("\n")
                    f.write("\n")
                    f.write("**END GLOBAL**\n\n")


                    f.write("**START VARIABLES**\n\n")
                    # f.write("Proposed parameter,,")
                    header = [
                        "proposed parameter",
                        "",
                        "",
                    ]
                    for param,_ in common_var_atts.items():
                        if param in old_var_atts_map:
                            header.append(param)
                        else:
                            header.append("")
                    f.write(",".join(header))
                    f.write("\n")
 
                    header = [
                        "current parameter",
                        "current_variable",
                        "proposed_variable",
                    ]
                    for param,_ in common_var_atts.items():
                        if param in old_var_atts_map:
                            header.append(old_var_atts_map[param])
                        else:
                            header.append(param)

                        # header.append(param)

                    f.write(",".join(header))
                    f.write("\n")
                    for name, var in dset["variables"].items():
                        row = ["", name, ""]
                        for attname, att in var.items():
                            # print(name, att)
                            if type(att) == str:
                                if att is None:
                                    att = ""
                                row.append(f'"{att}"')
                                # row = f'{name},{attname},"{att}"'
                            else:
                                if att is None:
                                    att = ""
                                row.append(f"{att}")
                                # row = f'{name},{attname},{att}'
                        f.write(",".join(row))
                        f.write("\n")
                    f.write("\n")
                    f.write("**END VARIABLES**\n\n")
                    


            # exit()



if __name__ == "__main__":
    # download_ncojson_files()
    create_var_forms()

