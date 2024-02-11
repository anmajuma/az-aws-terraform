 
# Python program to read
# json file
 
import json
import pandas as pd
 
# Opening JSON file
f = open('input/config.json')
 
# returns JSON object as 
# a dictionary
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
    counter = counter + 1
f.close()