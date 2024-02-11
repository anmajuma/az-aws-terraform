import os
import json
import pandas as pd
from jinja2 import Environment, PackageLoader, select_autoescape

jinja_env = Environment(
    loader = PackageLoader("main"),
    autoescape = select_autoescape()
)

def generate_template(_template, _data):
    return _template.render(_data)

if __name__ == "__main__":

    vs_template = generate_template(
        _template = jinja_env.get_template("az_rm_template.jinja2"),
        _data = {
            }
    )

    # Write template to file

    with open(os.getcwd() + "/main.tf", "w") as fd:
        fd.write("\n")
        fd.write(vs_template)

# Opening JSON file
    f = open('input/config.json')
    data = json.load(f)
    resourceList = list(data['resourceConfig'].keys())
    counter = 0
    lookupDF = pd.read_csv("ref/lookup.csv")
    while counter < len(resourceList):
        rslt_df = lookupDF[lookupDF['resource_type'] == resourceList[counter]]['template_name']
        print(rslt_df.iloc[0])
        az_config = data['resourceConfig'][resourceList[counter]]
        for az_rs in az_config:
            print(az_rs)
            vs_template = generate_template(
            _template = jinja_env.get_template(rslt_df.iloc[0]),
            _data = az_rs
    )
    # Write template to file
        with open(os.getcwd() + "/main.tf", "a") as fd:
            fd.write("\n")
            fd.write(vs_template)
            print(rslt_df.iloc[0] + "-terraform script created")
            counter = counter + 1
    f.close()        

    # vs_template = generate_template(
    #     _template = jinja_env.get_template("az_rg_template.jinja2"),
    #     _data = az_config
    #     # {
    #     #     "rg_module_name" : "resource_group_network",
    #     #     "rg_name" : "lexcorp-dev",
    #     #     "rg_location": "North Europe"
    #     #     }
    # )

    # # Write template to file

    # with open(os.getcwd() + "/main.tf", "a") as fd:
    #     fd.write("\n")
    #     fd.write(vs_template)

    # vs_template = generate_template(
    #     _template = jinja_env.get_template("az_vnet_template.jinja2"),
    #     _data = {
    #         "vnet_name": "lexcorp-dev",
    #         "vnet_location": "North Europe",
    #         "vnet_module_name" : "virtual_network"
    #         }
    # )

    # # Write template to file

    # with open(os.getcwd() + "/main.tf", "a") as fd:
    #     fd.write("\n")
    #     fd.write(vs_template)

    # vs_template = generate_template(
    #     _template = jinja_env.get_template("az_subnet_template.jinja2"),
    #     _data = {
    #         "subnet_name": "lexcorp-dev",
    #         "snet_module_name" : "subnet_default"
    #         }
    # )

    # # Write template to file

    # with open(os.getcwd() + "/main.tf", "a") as fd:
    #     fd.write("\n")
    #     fd.write(vs_template)