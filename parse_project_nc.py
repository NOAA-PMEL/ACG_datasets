import glob
# from operator import inv
import os

from netCDF4 import Dataset, date2num
import numpy as np
import pandas as pd
import xarray as xr


# ds = xr.open_dataset("/home/derek/Software/python/doi_project/data/input/NAAMES1/NAAMES1_NAVWIND_v0.cdf")

# for name, attr in ds.attrs.items():
#     print(f"{name}: {attr}")

# for name,variable in ds.variables.items():
#     print(f"{name}: {variable.attrs.keys()}")

projects = [
    # "ACE1",
    # "ACE2",
    # "ACEASIA",
    # "AEROSOLS_INDOEX99",
    "ATOMIC",
    # "CALNEX",
    # "DYNAMO",
    # "ICEALOT",
    # "MAGE92",
    # "NAAMES1",
    # "NAURU99",
    # "NEAQS2002",
    # "NEAQS2004",
    # "RITS93",
    # "RITS94",
    # "TEXAQS2006",
    # "TEXAQSS2006",
    # # "UBWOS",
    # # "UBWOS-2013",
    # # "UBWOS2014",
    # "VOCALS",
    # "WACS2012",
    # "WACS2014",
]

base_path = os.path.join(os.getcwd(), "data")

def parse_nc_files():

    for project in projects:

        input_path = os.path.join(base_path, "input", project)
        output_path = os.path.join(base_path, "output", project)
        files = glob.glob(os.path.join(input_path, "*.cdf"))

        os.makedirs(output_path, exist_ok=True)

        for file in files:
            ds = xr.open_dataset(file)
            
            outname = os.path.basename(file).replace("cdf", "csv")
            with open(os.path.join(output_path, outname), "w") as f:

                f.write("**VARIABLE_MAP**\n")
                f.write("Old Name,New Name\n")
                for name,_ in ds.variables.items():
                    if name == "time":
                        continue
                    f.write(f"{name},\n")

                f.write("\n**ATTRIBUTES**\n")
                f.write("Type, Name, Value\n")
                for name, attr in ds.attrs.items():
                    if type(attr) == str:
                        f.write(f'GLOBAL,{name},"{attr}"\n')
                    else:
                        f.write(f"GLOBAL,{name},{attr}\n")
                    # print(f"{name}: {attr}")
                
                # f.write("VARIABLES\n")
                for name,variable in ds.variables.items():
                    for attname, attr in variable.attrs.items():
                        if type(attr) == str:
                            # print("string")
                            f.write(f'{name},{attname},"{attr}"\n')
                        else:
                            f.write(f"{name},{attname},{attr}\n")

            # break

if __name__ == "__main__":
    parse_nc_files()