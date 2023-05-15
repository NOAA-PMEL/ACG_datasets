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
import data.config.dataset_config as ds_config
import data.config.readme as readme_config

base_path = os.path.join(os.getcwd(), "data")

# common_global_atts = {
#     "comment": "",
#     "contributor_name": "",
#     "creator_name": "",
#     "creator_email": "",
#     "creator_url": "",
#     "history": "",
#     "platform": "",
#     "product_version": "",
#     "project": "",
#     "sourceUrl": "",
#     "title": "",
# }

# common_var_atts = {
#     "long_name": {"type":  "string", "data": ""},
#     "units": {"type":  "string", "data": ""},
#     "instrument": {"type":  "string", "data": ""},
#     "source": {"type":  "string", "data": "surface observation"},
#     "valid_min": {"type": "double", "data": None},
#     "valid_max": {"type": "double", "data": None},
#     "uncertainty": {"type":  "string", "data": ""},
#     "standard_name": {"type":  "string", "data": ""},
#     # "ioos_category": {"type":  "string", "data": "Unknown"},
#     "history": {"type":  "string", "data": ""},
#     "comment": {"type":  "string", "data": ""},
#     "description": {"type":  "string", "data": ""},
# }


# projects = [
#     # "ACE1",
#     # "ACE2",
#     # "ACEASIA",
#     # "AEROSOLS_INDOEX99",
#     # "ATOMIC",
#     "CALNEX",
#     # "DYNAMO",
#     # "ICEALOT",
#     # "MAGE92",
#     # "NAAMES1",
#     # "NAURU99",
#     # "NEAQS2002",
#     # "NEAQS2004",
#     # "RITS93",
#     # "RITS94",
#     # "TEXAQS2006",
#     # "TEXAQSS2006",
#     # # "UBWOS",
#     # # "UBWOS-2013",
#     # # "UBWOS2014",
#     # "VOCALS",
#     # "WACS2012",
#     # "WACS2014",
# ]

# common_global_atts = {
#     "comment": "",
#     "contributor_name": "",
#     "creator_name": "",
#     "creator_email": "",
#     "creator_url": "",
#     "history": "",
#     "platform": "",
#     "product_version": "",
#     "project": "",
#     "sourceUrl": "",
#     "title": "",
# }

# old_atts_map = {
#     "platform": "PLATFORM",
#     "project": "PROJECT",
#     "product_version": "VERSION",
# }

# # common_var_atts = {
# #     "long_name": "",
# #     "units": "",
# #     "instrument": "",
# #     "source": "surface observation",
# #     "valid_min": None,
# #     "valid_max": None,
# #     "uncertainty": "",
# #     "standard_name": "",
# #     "ioos_category": "",
# #     "history": "",
# #     "comment": "",
# #     "description": "",
# # }

# old_var_atts_map = {
#     "instrument": "instr_id",
#     "valid_min": "min_value",
#     "valid_max": "max_value",
# }


# def get_atomic_variables() -> dict:
#     atomic_meta = {"attributes": {}, "variables": {}}
#     # load atomic variables
#     input_path = os.path.join(base_path, "input", "ATOMIC", "ncoJSON")
#     # output_path = os.path.join(base_path, "output", "ATOMIC")
#     # os.makedirs(output_path, exist_ok=True)

#     files = glob.glob(os.path.join(input_path, "*.json"))
#     for file in files:
#         with open(file, "r") as f:
#             input = json.load(f)
#             if os.path.basename(file) not in atomic_meta["attributes"]:
#                 atomic_meta["attributes"][os.path.basename(file)] = dict()
#             for name, att in common_global_atts.items():
#                 atomic_meta["attributes"][os.path.basename(file)][name] = None
#                 if name in input["attributes"]:
#                     if type(input["attributes"][name]["data"]) == str:
#                         if "\r" in input["attributes"][name]["data"]:
#                             pass
#                         val = input["attributes"][name]["data"].replace("\r", "")
#                         val = val.replace("\n\n", "\n")
#                         val = val.replace('"', "")
#                         input["attributes"][name]["data"] = f'"{val}"'
#                     atomic_meta["attributes"][os.path.basename(file)][name] = input[
#                         "attributes"
#                     ][name]["data"]

#             for name, var in input["variables"].items():
#                 if name not in atomic_meta["variables"]:
#                     atomic_meta["variables"][name] = {"attributes": {}}
#                     for attname, att in common_var_atts.items():
#                         if attname in var["attributes"]:
#                             if type(var["attributes"][attname]["data"]) == str:
#                                 var["attributes"][attname][
#                                     "data"
#                                 ] = f'"{var["attributes"][attname]["data"]}"'
#                                 # if "\n" in var["attributes"][attname]["data"]:
#                                 #     var["attributes"][attname]["data"].replace("\n", ";")
#                                 # if "," in var["attributes"][attname]["data"]:
#                                 #     var["attributes"][attname]["data"].replace(",", " ")

#                             atomic_meta["variables"][name]["attributes"][attname] = var[
#                                 "attributes"
#                             ][attname]
#                         else:
#                             atomic_meta["variables"][name]["attributes"][attname] = att
#                             # {
#                             #     "data": att
#                             # }

#     return atomic_meta


# def write_atomic_variables():
#     # atomic_meta = {"attributes": {}, "variables": {}}
#     # # load atomic variables
#     # input_path = os.path.join(base_path, "input", "ATOMIC", "ncoJSON")
#     output_path = os.path.join(base_path, "output", "ATOMIC")
#     os.makedirs(output_path, exist_ok=True)

#     # files = glob.glob(os.path.join(input_path, "*.json"))
#     # for file in files:
#     #     with open(file, "r") as f:
#     #         input = json.load(f)

#     #         for name, att in common_global_atts.items():
#     #             atomic_meta["attributes"][name] = None
#     #             if name in input["attributes"]:
#     #                 if type(input["attributes"][name]["data"]) == str:
#     #                     input["attributes"][name][
#     #                         "data"
#     #                     ] = f'"{input["attributes"][name]["data"]}"'
#     #                 atomic_meta["attributes"][name] = {
#     #                     os.path.basename(file): input["attributes"][name]
#     #                 }

#     #         for name, var in input["variables"].items():
#     #             if name not in atomic_meta["variables"]:
#     #                 atomic_meta["variables"][name] = dict()
#     #                 for attname, att in common_var_atts.items():
#     #                     if attname in var["attributes"]:
#     #                         if type(var["attributes"][attname]["data"]) == str:
#     #                             var["attributes"][attname][
#     #                                 "data"
#     #                             ] = f'"{var["attributes"][attname]["data"]}"'
#     #                             # if "\n" in var["attributes"][attname]["data"]:
#     #                             #     var["attributes"][attname]["data"].replace("\n", ";")
#     #                             # if "," in var["attributes"][attname]["data"]:
#     #                             #     var["attributes"][attname]["data"].replace(",", " ")

#     #                         atomic_meta["variables"][name][attname] = var["attributes"][
#     #                             attname
#     #                         ]
#     #                     else:
#     #                         atomic_meta["variables"][name][attname] = att

#     atomic_meta = get_atomic_variables()
#     outfile = os.path.join(output_path, "ATOMIC_global_attributes.csv")
#     with open(outfile, "w") as f:
#         f.write("name,source_file,value")
#         # f.write(",".join(common_global_atts.keys()))
#         f.write("\n")

#         for name, attr in common_global_atts.items():
#             if name in atomic_meta["attributes"]:
#                 for fname, value in atomic_meta["attributes"][name].items():
#                     f.write(f"{name},{fname},{value['data']}\n")
#             else:
#                 f.write(f"{name},,\n")

#     outfile = os.path.join(output_path, "ATOMIC_variable_names.csv")
#     # outfile = outfile.replace(".json", ".csv")

#     with open(outfile, "w") as f:
#         f.write("name,")
#         f.write(",".join(common_var_atts.keys()))
#         f.write("\n")
#         for name, var in atomic_meta["variables"].items():
#             f.write(f"{name}")
#             for attname, attr in common_var_atts.items():
#                 if attname in var:
#                     f.write(f",{var[attname]['data']}")
#                 else:
#                     f.write(",")
#             f.write("\n")

#     # project_meta = dict()
#     # for project in projects:

#     #     input_path = os.path.join(base_path, "input", project)
#     #     output_path = os.path.join(base_path, "output", project)
#     #     files = glob.glob(os.path.join(input_path, "*.json"))

#     #     os.makedirs(output_path, exist_ok=True)

#     #     if project == "ATOMIC":

#     #         for file in files:
#     #             with open(file, "r") as f:
#     #                 input = json.load(f)

#     #             dset = {"attributes": {}, "variables": {}}
#     #             for name, att in common_global_atts.items():
#     #                 dset["attributes"][name] = None
#     #                 if name in input["attributes"]:
#     #                     dset["attributes"][name] = input["attributes"][name]["data"]

#     #             for name, var in input["variables"].items():
#     #                 if name not in ["time", "latitude", "longitude", "trajectory_id"]:
#     #                     dset["variables"][name] = dict()
#     #                     for attname, att in common_var_atts.items():
#     #                         if attname in var["attributes"]:
#     #                             dset["variables"][name][attname] = var["attributes"][attname]["data"]
#     #                         else:
#     #                             dset["variables"][name][attname] = att


# def get_project_variables(project: str) -> dict:
#     project_meta = {"attributes": {}, "variables": {}}

#     # for project in projects:
#     input_path = os.path.join(base_path, "input", project, "netcdf")
#     # output_path = os.path.join(base_path, "output", project)
#     files = glob.glob(os.path.join(input_path, "*.cdf"))

#     # os.makedirs(output_path, exist_ok=True)

#     for file in files:
#         ds = xr.open_dataset(file)

#         if os.path.basename(file) not in project_meta["attributes"]:
#             project_meta["attributes"][os.path.basename(file)] = dict()
#         for name, attr in ds.attrs.items():
#             # if isinstance(attr, str):
#             # f'"{input["attributes"][name]["data"]}"'
#             if type(attr) == str:
#                 if "\r" in attr:
#                     pass
#                 val = attr.replace("\r", "")
#                 val = val.replace("\n\n", "\n")
#                 val = val.replace('"', "")
#                 project_meta["attributes"][os.path.basename(file)][name] = f'"{val}"'
#             else:
#                 project_meta["attributes"][os.path.basename(file)][name] = attr
#         for name, var in ds.variables.items():
#             if name != "time" and name not in project_meta["variables"]:
#                 project_meta["variables"][name] = {"attributes": var.attrs}

#     return project_meta


# def write_project_variables():
#     # project_meta = {"attributes": {}, "variables": {}}

#     for project in projects:
#         # input_path = os.path.join(base_path, "input", project)
#         output_path = os.path.join(base_path, "output", project)
#         # files = glob.glob(os.path.join(input_path, "*.cdf"))

#         #     os.makedirs(output_path, exist_ok=True)

#         #     for file in files:
#         #         ds = xr.open_dataset(file)

#         #         for name, var in ds.variables.items():
#         #             if name != "time" and name not in project_meta["variables"]:
#         #                 project_meta["variables"][name] = {"attributes": var.attrs}

#         project_meta = get_project_variables(project=project)
#         # outname = os.path.basename(file).replace("cdf", "csv")
#         with open(os.path.join(output_path, f"{project}_variable_names.csv"), "w") as f:
#             f.write("New Name,Old Name, name, long_name\n")
#             for name, var in project_meta["variables"].items():
#                 f.write(f",{name},")
#                 if "name" in var["attributes"]:
#                     f.write(f'"{var["attributes"]["name"]}",')
#                 else:
#                     f.write(",")
#                 if "long_name" in var["attributes"]:
#                     f.write(f'"{var["attributes"]["long_name"]}"\n')
#                 else:
#                     f.write("\n")


# def build_dataset_merge():
#     merge_map = dict()

#     atomic_meta = get_atomic_variables()

#     for project in projects:
#         # get mapping
#         input_path = os.path.join(base_path, "input", project)
#         output_path = os.path.join(base_path, "output", project)
#         with open(
#             os.path.join(input_path, "maps", f"{project}_variable_names_map.csv"), "r"
#         ) as f:
#             f.readline()
#             for line in f:
#                 parts = line.strip().split(",")
#                 merge_map[parts[1]] = {
#                     "old_name": parts[0],
#                     "dataset": parts[2],
#                     "convert": parts[3],
#                 }

#         project_meta = get_project_variables(project=project)

#         with open(os.path.join(output_path, f"{project}_variable_map.csv"), "w") as f:
#             f.write("variable_name,old_variable_name,attribute_name, attribute_value\n")
#             for var in ["time", "latitude", "longitude"]:  # , "duration"]:
#                 # common_var_atts = {
#                 #     "long_name": "",
#                 #     "units": "",
#                 #     "instrument": "",
#                 #     "source": "surface observation",
#                 #     "valid_min": None,
#                 #     "valid_max": None,
#                 #     "uncertainty": "",
#                 #     "standard_name": "",
#                 #     "ioos_category": "",
#                 #     "history": "",
#                 #     "comment": "",
#                 #     "description": "",

#                 # }

#                 for vatt in common_var_atts.keys():
#                     f.write(f"{var},{merge_map[var]['old_name']},")
#                     if vatt in atomic_meta["variables"][var]["attributes"]:
#                         f.write(
#                             f"{vatt}, {atomic_meta['variables'][var]['attributes'][vatt]['data']}\n"
#                         )
#             f.write(f"duration,{merge_map[var]['old_name']},long_name,Duration\n")
#             f.write(f"duration,{merge_map[var]['old_name']},units,second\n")
#             f.write(f"trajectory_id,,long_name,Trajetory ID\n")

#             for name, varmap in merge_map.items():
#                 if name not in ["time", "latitude", "longitude", "duration"]:
#                     old_name = varmap["old_name"]

#                     if old_name and old_name in project_meta["variables"]:
#                         # for name, var in project_meta["variables"].items():
#                         #     if name not in ["time", "latitude", "longitude", "duration"]:
#                         #         old_name = merge_map[var]['old_name']
#                         #         if old_name and old_name in project_meta["variables"]:

#                         f.write(f"{name},{old_name},dataset,{varmap['dataset']}\n")
#                         f.write(f"{name},{old_name},convert,{varmap['convert']}\n")
#                         # f.write(f"{name},{old_name},trajectory_id,{f'{project}_Atlantis_Leg1'}\n")
#                         if name in atomic_meta["variables"]:
#                             for vatt in common_var_atts.keys():
#                                 f.write(f"{name},{old_name},")
#                                 if vatt in atomic_meta["variables"][name]["attributes"]:
#                                     # old_var_atts_map = {
#                                     #     "instrument":"instr_id",
#                                     #     "valid_min":"min_value",
#                                     #     "valid_max":"max_value",

#                                     # }
#                                     try:
#                                         if (
#                                             old_var_atts_map[vatt]
#                                             in project_meta["variables"][old_name][
#                                                 "attributes"
#                                             ]
#                                         ):
#                                             f.write(
#                                                 f"{vatt}, {project_meta['variables'][old_name]['attributes'][old_var_atts_map[vatt]]}\n"
#                                             )
#                                     except KeyError:
#                                         f.write(
#                                             f"{vatt}, {atomic_meta['variables'][name]['attributes'][vatt]['data']}\n"
#                                         )

#                     if old_name in project_meta["variables"]:
#                         for old_att_name, old_att in project_meta["variables"][
#                             old_name
#                         ]["attributes"].items():
#                             f.write(f"{name},{old_name},")
#                             f.write(f"OLD_{old_att_name},{old_att}\n")

#                 # f.write(f",{name},")
#                 # if "name" in var["attributes"]:
#                 #     f.write(f'"{var["attributes"]["name"]}",')
#                 # else:
#                 #     f.write(",")
#                 # if "long_name" in var["attributes"]:
#                 #     f.write(f'"{var["attributes"]["long_name"]}"\n')
#                 # else:
#                 #     f.write("\n")

#     # write all global attributes
#     with open(os.path.join(output_path, f"{project}_global_attributes.csv"), "w") as f:
#         f.write("source,attribute_name, attribute_value\n")
#         for source, source_atts in atomic_meta["attributes"].items():
#             for name, attr in source_atts.items():
#                 f.write(f"{source},{name},{attr}\n")

#         for source, source_atts in project_meta["attributes"].items():
#             for name, attr in source_atts.items():
#                 f.write(f"{source},{name},{attr}\n")


# dataset_map = {
#     "BASE": ["all", "nav", "met", "microphys", "gas"],
#     "CHEM": ["all", "chemistry"],
#     "AMS": ["all", "ams"],
#     "CCN": ["all", "ccn"],
#     "OPTICS": ["all", "optics"],
#     "AOD": ["all", "aod"],
#     "SW": ["all", "seawater"],
#     "DMS": ["all", "dms"],
#     "RADON": ["all", "radon"],
# }

# dataset_config = {
#     "base": {
#         "map": ["all", "nav", "met", "microphys"],
#         "conversions": {},
#         "replace_map": {},
#     },
#     "inorganic_ion_chemistry": {
#         "map": ["all", "inorganic_ion_chemistry"],
#         "conversions": {
#             "sub10": {
#                 "components": ["sub1", "super1", "add"],
#                 "long_name": "Particulate <ion> Concentration for Dp < 10 um, ug m-3"
#                 },
#         },
#         "replace_map": {
#             "Concentration in Dp < 1.1um": "Particulate <ion> Concentration for Dp < 1.1 um, ug m-3",
#         },
#     },
#     "trace_element_chemistry": {
#         "map": ["all", "trace_element_chemistry"],
#         "conversions": {
#             "sub10": {
#                 "components": ["sub1", "super1", "add"],
#                 "long_name": "Particulate <ion> Concentration for Dp < 10 um, ug m-3"
#                 },
#         },
#         "replace_map": {
#             "Concentration in Dp < 1.1um": "Particulate <ion> Concentration for Dp < 1.1 um, ug m-3",
#         },

#     },
#     "total_mass": {
#         "map": ["all", "total_mass"],
#         "conversions": {
#             "sub10": {
#                 "components": ["sub1", "super1", "add"],
#                 "long_name": "Total aerosol mass for Dp < 10 um, ug m-3"
#                 },
#         },
#         "replace_map": {},
#     },

#     "non-refractory_chemistry": {
#         "map": ["all", "non_refractory_chemistry"],
#         "conversions": {
#             "sub10": {},
#         },
#         "replace_map": {},
#     },
#     "gas_chemistry": {
#         "map": ["all", "gas_chemistry"],
#         "conversions": {},
#         "replace_map": {},
#     },
#     "carbon_chemistry": {
#         "map": ["all", "carbon_chemistry"],
#         "conversions": {},
#         "replace_map": {},
#     },
#     "aod": {
#         "map": ["all", "aod"],
#         "conversions": {},
#         "replace_map": {},
#     },
#     "ccn": {
#         "map": ["all", "ccn"],
#         "conversions": {},
#         "replace_map": {},
#     },
#     "radon": {
#         "map": ["all", "radon"],
#         "conversions": {},
#         "replace_map": {},
#     },
#     "optics": {
#         "map": ["all", "optics"],
#         "conversions": {},
#         "replace_map": {},
#     },
#     "dms": {
#         "map": ["all", "dms"],
#         "conversions": {},
#         "replace_map": {},
#     },
#     "seawater": {
#         "map": ["all", "seawater"],
#         "conversions": {},
#         "replace_map": {},
#     },

# }

# chemistry_long_names = {
#     "IC": "Particulate <ion> Concentration for <size_range>, ug m-3",
#     "XRF": "Particulate <ion> Concentration for <size_range>, ug m-3",
#     "total_aerosol_mass": "Total aerosol mass for <size_range>, ug m-3",
# }

# chemistry_inst_names = {
#     "IC": "2-stage impactor, 50% aerodynamic cut-off diameters of 1.1 and 10 um -- ion chromatographic analysis",
#     "XRF": "Impactor with 50% aerodynamic cutoff diameter of <size> um -- x-ray emission spectrometry",
# }

# optics_long_names = {
#     "absorb": "Aerosol light absorption coefficient for Dp < <size> um at <wl> nm, Mm-1",
#     "absorb_angstrom": "Absorption Angstrom Exponent for Dp < <size> um and the <wl1>, <wl2> wavelength pair",
#     "scatter": "Aerosol light scattering coefficient for Dp < <size> um at <wl> nm, Mm-1",
#     "backscatter": "Aerosol light backscattering coefficient for Dp < <size> um at <wl> nm, Mm-1",
#     "scatter_fRH": "Dependence of aerosol light scattering on RH (fRH) for Dp < <size> um at <wl> nm",
#     "scatter_rh": "Sample RH of aerosol light scattering coefficient for Dp < <size> um, %",
#     "scatter_angstrom": "Scattering Angstrom Exponent for Dp < <size> um and the <wl1>, <wl2> wavelength pair",
#     "ssa": "Single Scattering Albedo for Dp < <size> um at <wl> nm",
# }

# def rewrite_variable_map(project: str):

#     variable_map = dict()
#     input_path = os.path.join(base_path, "input", project)
#     output_path = os.path.join(base_path, "output", project)
#     with open(os.path.join(output_path, f"{project}_variable_map_V1.csv"), "r",encoding="cp1252") as f:
#         f.readline()
#         for line in f:
#             parts = line.strip().split(",")
#             if parts[0] not in variable_map:
#                 variable_map[parts[0]] = {"old_name": parts[1], "attributes": {}}
#             variable_map[parts[0]]["attributes"][parts[2]] = parts[3]
#             if "OLD_note" in parts[2]:
#                 if "UNCERTAINTY" in parts[3]:
#                     variable_map[parts[0]]["attributes"]["uncertainty"] = parts[3].split("=")[-1]
#                 else:
#                     comment = variable_map[parts[0]]["attributes"]["comment"]
#                     if comment:
#                         variable_map[parts[0]]["attributes"]["comment"] = ";".join([comment, parts[3]])
#                     else:
#                         variable_map[parts[0]]["attributes"]["comment"] = parts[3]

#     for var in ["time", "trajectory_id", "latitude", "longitude"]:
#         if var in variable_map:
#             variable_map[var]["attributes"]["dataset"] = "all"

#     # add converted chemistry_parameters
#     converted_map = dict()

#     # remove bad frh variables
#     bad_vars = []
#     for name in variable_map.keys():
#         if "frh" in name:
#             bad_vars.append(name)
#     for name in bad_vars:
#         variable_map.pop(name)

#     # for name, var in variable_map.items():
#     #     try:
#     #         if var["attributes"]["convert"] == "TRUE":
#     #             parts = name.split("_")
#     #             newname = name.replace("super1", "sub10")
#     #             converted_map[newname] = {"old_name": "", "attributes": {}}
#     #             for attname, att in var["attributes"].items():
#     #                 if attname == "convert":
#     #                     converted_map[newname]["attributes"]["convert"] = ""
#     #                 else:
#     #                     converted_map[newname]["attributes"][attname] = att
#     #     except KeyError as e:
#     #         print(f"convert error: {e}")

#     for name, var in converted_map.items():
#         variable_map[name] = var


#     # map long names for chem
#     for name in variable_map.keys():
#         if "IC_" in name or "XRF_" in name:
#             parts = name.split("_")
#             ion = parts[1]
#             # size = parts[2]
#             fraction = parts[-1]
#             long_name = chemistry_long_names["IC"]
#             long_name = long_name.replace("<ion>", ion)

#             if fraction == "sub1":
#                 size_range = "Dp < 1.1 um"
#             elif fraction == "super1":
#                 size_range = "1.1 um < Dp < 10 um"
#             elif fraction == "sub10":
#                 size_range = "Dp < 10 um"

#             long_name = long_name.replace("<size_range>", size_range)
#             variable_map[name]["attributes"]["long_name"] = long_name

#         elif "total_aerosol_mass_" in name:
#             parts = name.split("_")
#             fraction = parts[-1]
#             if fraction == "sub1":
#                 size_range = "Dp < 1.1 um"
#             elif fraction == "super1":
#                 size_range = "1.1 um < Dp < 10 um"
#             elif fraction == "sub10":
#                 size_range = "Dp < 10 um"
#             long_name = long_name.replace("<size_range>", size_range)
#             variable_map[name]["attributes"]["long_name"] = long_name

#     # replace long_names for optics
#     for name in variable_map.keys():
#         if "absorb_" in name:
#             parts = name.split("_")
#             fraction = parts[-1]
#             if parts[1] == "angstrom":
#                 wl2 = parts[-2]
#                 wl1 = parts[-3]

#                 long_name = optics_long_names["absorb_angstrom"]
#                 long_name = long_name.replace("<wl1>", wl1)
#                 long_name = long_name.replace("<wl2>", wl2)
#             else:
#                 long_name = optics_long_names["absorb"]
#                 wl = parts[-2]
#                 long_name = long_name.replace("<wl>", wl)

#             size = "1.1"
#             if fraction == "sub10":
#                 size = "10"

#             long_name = long_name.replace("<size>", size)
#             variable_map[name]["attributes"]["long_name"] = long_name

#         elif "backscatter_" in name:
#             parts = name.split("_")
#             fraction = parts[-1]
#             if parts[1] == "angstrom":
#                 wl2 = parts[-2]
#                 wl1 = parts[-3]

#                 long_name = optics_long_names["backscatter_angstrom"]
#                 long_name = long_name.replace("<wl1>", wl1)
#                 long_name = long_name.replace("<wl2>", wl2)
#             elif parts[1] == "rh":
#                 long_name = optics_long_names["backscatter_rh"]
#             else:
#                 if parts[1] == "fRH":
#                     long_name = optics_long_names["backscatter_fRH"]
#                 else:
#                     long_name = optics_long_names["backscatter"]

#                 wl = parts[-2]
#                 long_name = long_name.replace("<wl>", wl)

#             size = "1.1"
#             if fraction == "sub10":
#                 size = "10"

#             long_name = long_name.replace("<size>", size)
#             variable_map[name]["attributes"]["long_name"] = long_name

#         elif "scatter_" in name:
#             parts = name.split("_")
#             fraction = parts[-1]
#             if parts[1] == "angstrom":
#                 wl2 = parts[-2]
#                 wl1 = parts[-3]

#                 long_name = optics_long_names["scatter_angstrom"]
#                 long_name = long_name.replace("<wl1>", wl1)
#                 long_name = long_name.replace("<wl2>", wl2)
#             elif parts[1] == "rh":
#                 long_name = optics_long_names["scatter_rh"]
#             else:
#                 if parts[1] == "fRH":
#                     long_name = optics_long_names["scatter_fRH"]
#                 else:
#                     long_name = optics_long_names["scatter"]

#                 wl = parts[-2]
#                 long_name = long_name.replace("<wl>", wl)

#             size = "1.1"
#             if fraction == "sub10":
#                 size = "10"

#             long_name = long_name.replace("<size>", size)
#             variable_map[name]["attributes"]["long_name"] = long_name
#         elif "ssa_" in name:
#             parts = name.split("_")
#             fraction = parts[-1]
#             wl = parts[-2]
#             size = "1.1"
#             if fraction == "sub10":
#                 size = "10"
#             long_name = optics_long_names["ssa"]
#             long_name = long_name.replace("<wl>", wl)
#             long_name = long_name.replace("<size>", size)
#             variable_map[name]["attributes"]["long_name"] = long_name


#     return variable_map

# def create_atomic_dataset_templates():
#     for dataset in dataset_map:
#         create_atomic_dataset_meta(dataset=dataset)

# def create_atomic_dataset_meta(dataset: str):
#     # load variable_map
#     project = "ATOMIC"
#     variable_map = dict()
#     input_path = os.path.join(base_path, "input", project)
#     output_path = os.path.join(base_path, "output", project)
#     with open(os.path.join(output_path, f"{project}_variable_list.csv"), "r") as f:
#         f.readline()
#         for line in f:
#             parts = line.strip().split(",")
#             if parts[0] not in variable_map:
#                 variable_map[parts[0]] = {"attributes": {}}
#             variable_map[parts[0]]["attributes"]["dataset"] = parts[1]
#             variable_map[parts[0]]["attributes"]["convert"] = parts[2]

#     variable_map["duration"] = {
#         "dataset": "all",
#         "convert": ""
#     }

#     for var in ["time", "trajectory_id", "latitude", "longitude"]:
#         if var in variable_map:
#             variable_map[var]["attributes"]["dataset"] = "all"

#     dataset_meta = {
#         "attributes": {},
#         "dimensions": {},
#         "variables": {},
#     }

#     dataset_meta["cdm_data_type"] = {"type":  "string", "data": "Trajectory"}
#     dataset_meta["cdm_trajectory_variables"] = {"type":  "string", "data": "trajectory_id"}
#     for attr in common_global_atts:
#         dataset_meta["attributes"][attr] = {"type":  "string", "data": ""}

#     dataset_meta["variables"]["time"] = {
#         # "type":  "string",
#         "attributes": {
#             "units": {"type":  "string", "data": "seconds since 1970-01-01T00:00:00Z"},
#         },
#         "data": [],
#     }
#     dataset_meta["variables"]["trajectory_id"] = {
#         "type":  "string",
#         "shape": ["time"],
#         "attributes": {
#             "cf_role": {"type":  "string", "data": "trajectory_id"},
#             "long_name": {"type":  "string", "data": "Trajectory ID"},
#         },
#         "data": [],
#     }

#     dataset_meta["variables"]["duration"] = {
#         "type": "int",
#         "shape": ["time"],
#         "attributes": {
#             "long_name": {"type":  "string", "data": "Duration"},
#             "units": {"type":  "string", "data": "second"}
#         },
#         "data": [],
#     }

#     atomic_meta = get_atomic_variables()
#     pass
#     for name, var in variable_map.items():
#         if name not in ["time", "trajectory_id", "duration"]:
#             if name in atomic_meta["variables"]:
#                 if var["attributes"]["dataset"] in dataset_map[dataset]:
#                     if name not in dataset_meta["variables"]:
#                         dataset_meta["variables"][name] = {
#                             "type": "double",
#                             "shape": ["time"],
#                             "attributes": {},
#                             "data": [],
#                         }

#                         # common_var_atts = {
#                         #     "long_name": {"type":  "string", "data": ""},
#                         #     "units": {"type":  "string", "data": ""},
#                         #     "instrument": {"type":  "string", "data": ""},
#                         #     "source": {"type":  "string", "data": "surface observation"},
#                         #     "valid_min": {"type": "double", "data": None},
#                         #     "valid_max": {"type": "double", "data": None},
#                         #     "uncertainty": {"type":  "string", "data": ""},
#                         #     "standard_name": {"type":  "string", "data": ""},
#                         #     # "ioos_category": {"type":  "string", "data": "Unknown"},
#                         #     "history": {"type":  "string", "data": ""},
#                         #     "comment": {"type":  "string", "data": ""},
#                         #     "description": {"type":  "string", "data": ""},
#                         # }

#                         for vattname, vatt in common_var_atts.items():

#                             dataset_meta["variables"][name]["attributes"][vattname] = vatt
#                             # if vattname in var["attributes"]:
#                             if vattname in atomic_meta["variables"][name]["attributes"]:
#                                 value = atomic_meta["variables"][name]["attributes"][vattname]["data"]
#                                 if type(value) == str:
#                                     value = value.strip().replace('"', '')
#                                 dataset_meta["variables"][name]["attributes"][vattname][
#                                     "data"
#                                 ] = value
#                             else:
#                                 pass


#     with open(os.path.join(output_path,f"{project}_dataset_tmpl_{dataset}.json"), "w") as f:
#         json.dump(dataset_meta, f)

#     with open(os.path.join(output_path,f"{project}_dataset_tmpl_{dataset}.csv"), "w") as f:
#         f.write("variable,attribute_name, attribute_value\n")
#         for name, gvar in dataset_meta["attributes"].items():
#             f.write(f"GLOBAL,{name},{gvar['data']}\n")
#         for name, var in dataset_meta["variables"].items():
#             for attname, varatt in var["attributes"].items():
#                 val = varatt['data']
#                 if type(val) == str:
#                     val = f'"{val}"'
#                 f.write(f"{name},{attname},{val}\n")

# def create_dataset_templates():
#     for dataset in dataset_map:
#         create_dataset_meta(project="CALNEX", dataset=dataset)

# def create_dataset_meta_old(project: str, dataset: str):
#     # load variable_map
#     variable_map = dict()
#     input_path = os.path.join(base_path, "input", project)
#     output_path = os.path.join(base_path, "output", project)
#     with open(os.path.join(output_path, f"{project}_variable_map.csv"), "r") as f:
#         f.readline()
#         for line in f:
#             parts = line.strip().split(",")
#             if parts[0] not in variable_map:
#                 variable_map[parts[0]] = {"old_name": parts[1], "attributes": {}}
#             variable_map[parts[0]]["attributes"][parts[2]] = parts[3]

#     for var in ["time", "trajectory_id", "latitude", "longitude"]:
#         if var in variable_map:
#             variable_map[var]["attributes"]["dataset"] = "all"

#     dataset_meta = {
#         "attributes": {},
#         "dimensions": {},
#         "variables": {},
#     }

#     dataset_meta["cdm_data_type"] = {"type":  "string", "data": "Trajectory"}
#     dataset_meta["cdm_trajectory_variables"] = {"type":  "string", "data": "trajectory_id"}
#     for attr in common_global_atts:
#         dataset_meta["attributes"][attr] = {"type":  "string", "data": ""}

#     dataset_meta["variables"]["time"] = {
#         # "type":  "string",
#         "attributes": {
#             "units": {"type":  "string", "data": "seconds since 1970-01-01T00:00:00Z"},
#         },
#         "data": [],
#     }
#     dataset_meta["variables"]["trajectory_id"] = {
#         "type":  "string",
#         "shape": ["time"],
#         "attributes": {
#             "cf_role": {"type":  "string", "data": "trajectory_id"},
#             "long_name": {"type":  "string", "data": "Trajectory ID"},
#         },
#         "data": [],
#     }

#     dataset_meta["variables"]["duration"] = {
#         "type": "int",
#         "shape": ["time"],
#         "attributes": {
#             "long_name": {"type":  "string", "data": "Duration"},
#             "units": {"type":  "string", "data": "second"}
#         },
#         "data": [],
#     }

#     for name, var in variable_map.items():
#         if name not in ["time", "trajectory_id", "duration"]:
#             if var["attributes"]["dataset"] in dataset_map[dataset]:
#                 if name not in dataset_meta["variables"]:
#                     dataset_meta["variables"][name] = {
#                         "type": "double",
#                         "shape": ["time"],
#                         "attributes": {},
#                         "data": [],
#                     }

#                     # common_var_atts = {
#                     #     "long_name": {"type":  "string", "data": ""},
#                     #     "units": {"type":  "string", "data": ""},
#                     #     "instrument": {"type":  "string", "data": ""},
#                     #     "source": {"type":  "string", "data": "surface observation"},
#                     #     "valid_min": {"type": "double", "data": None},
#                     #     "valid_max": {"type": "double", "data": None},
#                     #     "uncertainty": {"type":  "string", "data": ""},
#                     #     "standard_name": {"type":  "string", "data": ""},
#                     #     # "ioos_category": {"type":  "string", "data": "Unknown"},
#                     #     "history": {"type":  "string", "data": ""},
#                     #     "comment": {"type":  "string", "data": ""},
#                     #     "description": {"type":  "string", "data": ""},
#                     # }

#                     for vattname, vatt in common_var_atts.items():
#                         dataset_meta["variables"][name]["attributes"][vattname] = vatt
#                         if vattname in var["attributes"]:
#                             value = var["attributes"][vattname]
#                             if type(value) == str:
#                                 value = value.strip().replace('"', '')
#                             dataset_meta["variables"][name]["attributes"][vattname][
#                                 "data"
#                             ] = value


#     with open(os.path.join(output_path,f"{project}_dataset_tmpl_{dataset}.json"), "w") as f:
#         json.dump(dataset_meta, f)

#     with open(os.path.join(output_path,f"{project}_dataset_tmpl_{dataset}.csv"), "w") as f:
#         f.write("variable,attribute_name, attribute_value\n")
#         for name, gvar in dataset_meta["attributes"].items():
#             f.write(f"GLOBAL,{name},{gvar['data']}\n")
#         for name, var in dataset_meta["variables"].items():
#             for attname, varatt in var["attributes"].items():
#                 f.write(f"{name},{attname},{varatt['data']}\n")


# def create_dataset_meta(project: str, dataset: str):
#     # load variable_map
#     # variable_map = dict()
#     input_path = os.path.join(base_path, "input", project)
#     output_path = os.path.join(base_path, "output", project)
#     # with open(os.path.join(output_path, f"{project}_variable_map_V1.csv"), "r") as f:
#     #     f.readline()
#     #     for line in f:
#     #         parts = line.strip().split(",")
#     #         if parts[0] not in variable_map:
#     #             variable_map[parts[0]] = {"old_name": parts[1], "attributes": {}}
#     #         variable_map[parts[0]]["attributes"][parts[2]] = parts[3]

#     # for var in ["time", "trajectory_id", "latitude", "longitude"]:
#     #     if var in variable_map:
#     #         variable_map[var]["attributes"]["dataset"] = "all"

#     variable_map = rewrite_variable_map(project)

#     dataset_meta = {
#         "attributes": {},
#         "dimensions": {},
#         "variables": {},
#     }

#     dataset_meta["cdm_data_type"] = {"type":  "string", "data": "Trajectory"}
#     dataset_meta["cdm_trajectory_variables"] = {"type":  "string", "data": "trajectory_id"}
#     for attr in common_global_atts:
#         dataset_meta["attributes"][attr] = {"type":  "string", "data": ""}

#     dataset_meta["variables"]["time"] = {
#         # "type":  "string",
#         "attributes": {
#             "units": {"type":  "string", "data": "seconds since 1970-01-01T00:00:00Z"},
#         },
#         "data": [],
#     }
#     dataset_meta["variables"]["trajectory_id"] = {
#         "type":  "string",
#         "shape": ["time"],
#         "attributes": {
#             "cf_role": {"type":  "string", "data": "trajectory_id"},
#             "long_name": {"type":  "string", "data": "Trajectory ID"},
#         },
#         "data": [],
#     }

#     dataset_meta["variables"]["duration"] = {
#         "type": "int",
#         "shape": ["time"],
#         "attributes": {
#             "long_name": {"type":  "string", "data": "Duration"},
#             "units": {"type":  "string", "data": "second"}
#         },
#         "data": [],
#     }

#     for name, var in variable_map.items():
#         if name not in ["time", "trajectory_id", "duration"]:
#             if var["attributes"]["dataset"] in dataset_config[dataset]["map"]:
#                 if name not in dataset_meta["variables"]:
#                     dataset_meta["variables"][name] = {
#                         "type": "double",
#                         "shape": ["time"],
#                         "attributes": {},
#                         "data": [],
#                     }

#                     # common_var_atts = {
#                     #     "long_name": {"type":  "string", "data": ""},
#                     #     "units": {"type":  "string", "data": ""},
#                     #     "instrument": {"type":  "string", "data": ""},
#                     #     "source": {"type":  "string", "data": "surface observation"},
#                     #     "valid_min": {"type": "double", "data": None},
#                     #     "valid_max": {"type": "double", "data": None},
#                     #     "uncertainty": {"type":  "string", "data": ""},
#                     #     "standard_name": {"type":  "string", "data": ""},
#                     #     # "ioos_category": {"type":  "string", "data": "Unknown"},
#                     #     "history": {"type":  "string", "data": ""},
#                     #     "comment": {"type":  "string", "data": ""},
#                     #     "description": {"type":  "string", "data": ""},
#                     # }

#                     for vattname, vatt in common_var_atts.items():
#                         dataset_meta["variables"][name]["attributes"][vattname] = vatt.copy()
#                         if vattname in var["attributes"]:
#                             value = var["attributes"][vattname]
#                             if type(value) == str:
#                                 value = value.strip().replace('"', '')
#                             dataset_meta["variables"][name]["attributes"][vattname][
#                                 "data"
#                             ] = value


#     with open(os.path.join(output_path,f"{project}_dataset_tmpl_{dataset}.json"), "w") as f:
#         json.dump(dataset_meta, f)

#     with open(os.path.join(output_path,f"{project}_dataset_tmpl_{dataset}.csv"), "w") as f:
#         f.write("variable,attribute_name, attribute_value\n")
#         for name, gvar in dataset_meta["attributes"].items():
#             value = gvar["data"]
#             if type(value)  == str:
#                 value = f'"{value.strip()}"'
#             # f.write(f"GLOBAL,{name},{gvar['data']}\n")
#             f.write(f"GLOBAL,{name},{value}\n")
#         for name, var in dataset_meta["variables"].items():
#             for attname, varatt in var["attributes"].items():
#                 value = varatt["data"]
#                 if type(value)  == str:
#                     value = f'"{value.strip()}"'
#                 # f.write(f"{name},{attname},{varatt['data']}\n")
#                 f.write(f"{name},{attname},{value}\n")

# '''
# time,*DATA_TYPE*,String
# time,_CoordinateAxisType,Time
# time,axis,T
# time,ioos_category,Time
# time,long_name,Datetime UTC
# time,standard_name,time
# time,source_name,datetime_utc
# time,time_origin,01/01/1970 00:00
# time,time_precision,1970-01-01 00:00
# time,units,yyyy-MM-dd HH:mm
# '''

# dataset_config_all = {
#     "main": {
#         "title": "Main",
#         "map": ["all", "nav", "met", "microphys"],
#         "conversions": {},
#         "replace_map": {},
#     },
#     "inorganic_ion_chemistry": {
#         "title": "Inorganic Ion Chemistry",
#         "map": ["all", "inorganic_ion_chemistry"],
#         "conversions": {
#             "sub10": {
#                 "components": ["sub1", "super1", "add"],
#                 "long_name": "Particulate <ion> Concentration for Dp < 10 um, ug m-3"
#                 },
#         },
#         "replace_map": {
#             "Concentration in Dp < 1.1um": "Particulate <ion> Concentration for Dp < 1.1 um, ug m-3",
#         },
#     },
#     "trace_element_chemistry": {
#         "title": "Trace Element Chemistry",
#         "map": ["all", "trace_element_chemistry"],
#         "conversions": {
#             "sub10": {
#                 "components": ["sub1", "super1", "add"],
#                 "long_name": "Particulate <ion> Concentration for Dp < 10 um, ug m-3"
#                 },
#         },
#         "replace_map": {
#             "Concentration in Dp < 1.1um": "Particulate <ion> Concentration for Dp < 1.1 um, ug m-3",
#         },

#     },
#     "total_mass": {
#         "map": ["all", "total_mass"],
#         "conversions": {
#             "sub10": {
#                 "components": ["sub1", "super1", "add"],
#                 "long_name": "Total aerosol mass for Dp < 10 um, ug m-3"
#                 },
#         },
#         "replace_map": {},
#     },
#     "non-refractory_chemistry": {
#         "map": ["all", "non_refractory_chemistry"],
#         "conversions": {
#             "sub10": {},
#         },
#         "replace_map": {},
#     },
#     "gas_chemistry": {
#         "map": ["all", "gas_chemistry"],
#         "conversions": {},
#         "replace_map": {},
#     },
#     "carbon_chemistry": {
#         "map": ["all", "carbon_chemistry"],
#         "conversions": {},
#         "replace_map": {},
#     },
#     "aod": {
#         "map": ["all", "aod"],
#         "conversions": {},
#         "replace_map": {},
#     },
#     "ccn": {
#         "map": ["all", "ccn"],
#         "conversions": {},
#         "replace_map": {},
#     },
#     "radon": {
#         "map": ["all", "radon"],
#         "conversions": {},
#         "replace_map": {},
#     },
#     "optics": {
#         "map": ["all", "optics_scatter", "optics_absorb"],
#         "conversions": {},
#         "replace_map": {},
#     },
#     "optics_intensive": {
#         "map": ["all", "optics_scatter_angstrom", "optics_absorb_angstrom", "optics_ssa"],
#         "conversions": {},
#         "replace_map": {},
#     },
#     "optics_frh": {
#         "map": ["all", "optics_frh"],
#         "conversions": {},
#         "replace_map": {},
#     },
#     "dms": {
#         "map": ["all", "dms"],
#         "conversions": {},
#         "replace_map": {},
#     },
#     "seawater": {
#         "map": ["all", "seawater"],
#         "conversions": {},
#         "replace_map": {},
#     },

# }

# def create_main_dataset_templates():

#     main_meta = {"attributes": {}, "variables": {}}
#     variable_names = dict()

#     main_input_path = os.path.join(base_path, "templates","input")
#     main_output_path = os.path.join(base_path, "templates","output")
#     calnex_input_path = os.path.join(base_path, "input", "CALNEX")
#     calnex_output_path = os.path.join(base_path, "output", "CALNEX")
#     atomic_input_path = os.path.join(base_path, "input", "ATOMIC")
#     atomic_output_path = os.path.join(base_path, "output", "ATOMIC")


#     # read in main variable map
#     with open(os.path.join(main_input_path,f"MAIN_variable_names_map.csv"), "r") as f:
#         f.readline()
#         for line in f:
#             parts = line.strip().split(",")
#             if parts[0] not in variable_names:
#                 variable_names[parts[0]] = {
#                     "old_name": parts[1],
#                     "dataset": parts[2]
#                 }

#             # if parts[0] not in variable_map:
#             #     variable_map[parts[0]] = {"old_name": parts[1], "attributes": {}}
#             # variable_map[parts[0]]["attributes"][parts[2]] = parts[3]


#     # use atomic/calnex to start the main template
#     variable_map = rewrite_variable_map("CALNEX")

#     # create time, trajectory_id, duration
#     main_meta["variables"]["time"] = {
#         "type":  "string",
#         "attributes": {
#             "_CoordinateAxisType": {"type":  "string", "data": "Time"},
#             "axis": {"type":  "string", "data": "T"},
#             "ioos_category": {"type":  "string", "data": "Time"},
#             "long_name": {"type":  "string", "data": "Datetime UTC"},
#             "standard_name": {"type":  "string", "data": "time"},
#             "source_name": {"type":  "string", "data": "datetime_utc"},
#             "time_origin": {"type":  "string", "data": "01/01/1970 00:00"},
#             "time_precision": {"type":  "string", "data": "1970-01-01T00:00:00Z"},
#             "units": {"type":  "string", "data": "yyyy-MM-ddTHH:MM:ssZ"},
#         },
#         "data": [],
#     }
#     main_meta["variables"]["trajectory_id"] = {
#         "type":  "string",
#         "shape": ["time"],
#         "attributes": {
#             "cf_role": {"type":  "string", "data": "trajectory_id"},
#             "ioos_category": {"type":  "string", "data": "Identifier"},
#             "long_name": {"type":  "string", "data": "Trajectory ID"},
#         },
#         "data": [],
#     }

#     # main_meta["variables"]["latitude"] = {
#     #     "type":  "string",
#     #     "attributes": {
#     #         "_CoordinateAxisType": {"type":  "string", "data": "Lat"},
#     #         "axis": {"type":  "string", "data": "Y"},
#     #         "ioos_category": {"type":  "string", "data": "Location"},
#     #         "long_name": {"type":  "string", "data": "Latitude"},
#     #         "standard_name": {"type":  "string", "data": "latitude"},
#     #         "units": {"type":  "string", "data": "degrees_north"},
#     #         "valid_max": {"type": "double", "data": "90.0"},
#     #         "valid_min": {"type": "double", "data": "-90.0"},
#     #     },
#     #     "data": [],
#     # }

#     main_meta["variables"]["duration"] = {
#         "type": "int",
#         "shape": ["time"],
#         "attributes": {
#             "long_name": {"type":  "string", "data": "Duration"},
#             "units": {"type":  "string", "data": "second"}
#         },
#         "data": [],
#     }

#     #

#     for name, var in variable_map.items():
#         if name not in ["time", "trajectory_id", "duration"]:

#             for listname, listvar in variable_names.items():
#                 try:
#                     if var["old_name"] == listvar["old_name"]:
#                         if name not in main_meta["variables"]:
#                             main_meta["variables"][name] = {
#                                 "type": "double",
#                                 "shape": ["time"],
#                                 "attributes": {},
#                                 "data": [],
#                         }
#                         break
#                 except KeyError:
#                     continue

#             for vattname, vatt in common_var_atts.items():
#                 main_meta["variables"][name]["attributes"][vattname] = vatt.copy()
#                 if vattname in var["attributes"]:
#                     value = var["attributes"][vattname]
#                     if vattname == "units" and value == "unitless":
#                         continue
#                     if type(value) == str:
#                         value = value.strip().replace('"', '')
#                     main_meta["variables"][name]["attributes"][vattname][
#                         "data"
#                     ] = value

#     # add common global attributes

#     main_meta["attributes"]["cdm_data_type"] = {"type":  "string", "data": "Trajectory"}
#     main_meta["attributes"]["cdm_trajectory_variables"] = {"type":  "string", "data": "trajectory_id"}
#     for attr,_ in common_global_atts.items():
#         main_meta["attributes"][attr] = {"type":  "string", "data": ""}
#         if attr == "contributor_name":
#             main_meta["attributes"][attr]["data"] = "<SOURCE>"
#         elif attr == "creator_name":
#             main_meta["attributes"][attr]["data"] = "Johnson, James"
#         elif attr == "creator_email":
#             main_meta["attributes"][attr]["data"] = "james.e.johnson@noaa.gov"
#         elif attr == "platform":
#             main_meta["attributes"][attr]["data"] = "<PLATFORM>"
#         elif attr == "product_version":
#             main_meta["attributes"][attr]["data"] = "<VERSION>"
#         elif attr == "project":
#             main_meta["attributes"][attr]["data"] = "<PROJECT>"
#         elif attr == "source_url":
#             main_meta["attributes"][attr]["data"] = "https://saga.pmel.noaa.gov/data/"
#         elif attr == "title":
#             main_meta["attributes"][attr]["data"] = "PMEL Atmospheric Chemistry <PROJECT> <DATASET> data"


#     with open(os.path.join(main_output_path,f"MAIN_dataset_tmpl_all.json"), "w") as f:
#         json.dump(main_meta, f)

#     with open(os.path.join(main_output_path,f"MAIN_dataset_tmpl_all.csv"), "w") as f:
#         f.write("variable,attribute_name, attribute_value\n")
#         for name, gvar in main_meta["attributes"].items():
#             value = gvar["data"]
#             if type(value)  == str:
#                 value = f'"{value.strip()}"'
#             # f.write(f"GLOBAL,{name},{gvar['data']}\n")
#             f.write(f"GLOBAL,{name},{value}\n")
#         for name, var in main_meta["variables"].items():
#             for attname, varatt in var["attributes"].items():
#                 value = varatt["data"]
#                 if type(value)  == str:
#                     value = f'"{value.strip()}"'
#                 # f.write(f"{name},{attname},{varatt['data']}\n")
#                 f.write(f"{name},{attname},{value}\n")

#     pass

# def save_main_tmpl_as_json():
#     tmpl_input_path = os.path.join(base_path, "templates","input")
#     # tmpl_output_path = os.path.join(base_path, "templates","input")
#     # main_input_path = os.path.join(base_path, "templates","input")
#     # main_output_path = os.path.join(base_path, "templates","output")
#     # calnex_input_path = os.path.join(base_path, "input", "CALNEX")
#     # calnex_output_path = os.path.join(base_path, "output", "CALNEX")
#     # atomic_input_path = os.path.join(base_path, "input", "ATOMIC")
#     # atomic_output_path = os.path.join(base_path, "output", "ATOMIC")

#     data_types = {
#         "time": "string",
#         "trajectory_id": "string",
#         "duration": "int",

#     }

#     tmpl = {"attributes": {}, "dimensions": {}, "variables": {}}

#     tmpl["variables"]["time"] = {
#         "type": "string",
#         "attributes": {
#             "_CoordinateAxisType": {"type": "string", "data": "Time"},
#             "axis": {"type": "string", "data": "T"},
#             "ioos_category": {"type": "string", "data": "Time"},
#             "long_name": {"type": "string", "data": "Datetime UTC"},
#             "standard_name": {"type": "string", "data": "time"},
#             "source_name": {"type": "string", "data": "datetime_utc"},
#             "time_origin": {"type": "string", "data": "01/01/1970 00:00"},
#             "time_precision": {"type": "string", "data": "1970-01-01T00:00:00Z"},
#             "units": {"type": "string", "data": "yyyy-MM-ddTHH:MM:ssZ"},
#         },
#         "data": [],
#     }
#     tmpl["variables"]["trajectory_id"] = {
#         "type": "string",
#         "shape": ["time"],
#         "attributes": {
#             "cf_role": {"type": "string", "data": "trajectory_id"},
#             "ioos_category": {"type": "string", "data": "Identifier"},
#             "long_name": {"type": "string", "data": "Trajectory ID"},
#         },
#         "data": [],
#     }

#     tmpl["variables"]["duration"] = {
#         "type": "int",
#         "shape": ["time"],
#         "attributes": {
#             "long_name": {"type": "string", "data": "Duration"},
#             "units": {"type": "string", "data": "second"}
#         },
#         "data": [],
#     }

#     with open(os.path.join(tmpl_input_path,f"MAIN_dataset_tmpl_all.csv"), "r") as f:
#         f.readline()
#         for line in f:
#             parts = line.strip().split(",")
#             if len(parts) > 3:
#                 parts[2] = ",".join(parts[2:])
#             if parts[0] in ["time", "trajectory_id", "duration"]:
#                 continue
#             if parts[0] == "GLOBAL":
#                 tmpl["attributes"][parts[1]] = {"type": "string", "data": parts[2]}
#             else:
#                 if parts[0] not in tmpl["variables"]:
#                     tmpl["variables"][parts[0]] = {
#                         "type": "double",
#                         "shape": ["time"],
#                         "attributes": {},
#                         "data": [],
#                     }
#                 value = parts[2]

#                 if type(value) == str:
#                     value = value.replace('"', '').strip()
#                     dtype = "string"
#                 elif type(value) == int:
#                     dtype = "int"
#                 elif type(value) == float:
#                     dtype = "double"

#                 if parts[1] in ["valid_min", "valid_max"]:
#                     dtype = "double"
#                     try:
#                         value = float(value)
#                     except ValueError:
#                         pass

#                 tmpl["variables"][parts[0]]["attributes"][parts[1]] = {
#                     "type": dtype,
#                     "data": value
#                 }

#     with open(os.path.join(tmpl_input_path,f"MAIN_dataset_tmpl_all.json"), "w") as f:
#         json.dump(tmpl, f)


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
    main_names = "MAIN_variable_names_map.csv"
    aod3774_names = "AOD3774_variable_names_map.csv"
    aod5355_names = "AOD5355_variable_names_map.csv"
    ace1_names = "ACE1_variable_names_map.csv"
    ace2_names = "ACE2_variable_names_map.csv"
    rits_names = "RITS_variable_names_map.csv"

    with open(os.path.join(tmpl_input_path, rits_names), "r") as f:
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
    target_sample_rh = project_config.get("target_sample_rh", "")
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

    if dataset in [
        "atm",
        "inorganic_chemistry",
        "trace_element_chemistry",
        "total_mass",
        "carbon_chemistry",
        "ccn",
        "optics",
        "optics_intensive",
        "optics_frh",
    ]:
        if target_sample_rh:
            data["attributes"]["target_sample_rh"] = {
                "type": "string",
                "data": target_sample_rh,
            }

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

    json_output = os.path.join(output_path,"json")
    os.makedirs(json_output, exist_ok=True)
    with open(
        os.path.join(
            json_output, f"{project}_{platform}_{dataset}_v{product_version}.json"
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

    # create_dataset(project_id="RITS94", dataset="aod")

    # # write_project_config()
    # exit()

    projects = [
        # "ATOMIC",
        # "NAAMES4",
        # "NAAMES3",
        # "NAAMES2",
        # "NAAMES1",
        # "WACS2014",
        # "WACS2012",
        # "DYNAMO", # frh still wrong
        "CALNEX",
        # "VOCALS",
        # "ICEALOT",
        # "TEXAQS2006",
        # "NEAQS2004",  ###
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
    for proj in projects:
        try:
            print(f"Project: {proj}...")
            create_project_datasets(project_id=proj)
            print(f"Project: {proj}...done")
        # create_project_datasets(project_id="NAAMES4")
        except Exception as e:
            print(f"error: {proj} - {e}")
            pass
    # TODO
    # Create project config: project, platform, events?, trajectory_id and ??
    # One trajectory per file
    # Can use ncCSV or netCDF
