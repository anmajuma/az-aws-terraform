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
        _template = jinja_env.get_template("aws_provider_template.jinja2"),
        _data = { 'tf_version' : '~> 1.7.3',
                 'aws_version' : '>= 5.3.0'
            }
    )

    # Write template to file

    with open(os.getcwd() + "/main.tf", "w") as fd:
        fd.write("\n")
        fd.write(vs_template)

# Opening JSON file
    f = open('./aws-terraform/input/config.json')
    data = json.load(f)
    resourceList = list(data['resourceConfig'].keys())
    counter = 0
    lookupDF = pd.read_csv("./aws-terraform/ref/lookup.csv")
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
                vs_template =str(vs_template).replace("'", '"')
                fd.write("\n")
                fd.write(vs_template)
                print(rslt_df.iloc[0] + "-terraform script created")
            counter = counter + 1
    f.close()
