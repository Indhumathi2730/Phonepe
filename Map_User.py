import pandas as pd
import json
import os

# Path to your map user data
path = r"C:\Users\luna love\Downloads\Phonepe\pulse\data\map\user\hover\country\india\state"
map_user_state_list = os.listdir(path)
#print("States found:", map_user_state_list)

# Data dictionary
clm = {
    'State': [],
    'Year': [],
    'Quarter': [],
    'District': [],
    'RegisteredUsers': [],
    'AppOpens': []
}

# Loop through states, years, quarters
for i in map_user_state_list:
    p_i = os.path.join(path, i)
    Agg_yr = os.listdir(p_i)
    for j in Agg_yr:
        p_j = os.path.join(p_i, j)
        Agg_yr_list = os.listdir(p_j)
        for k in Agg_yr_list:
            p_k = os.path.join(p_j, k)
            with open(p_k, 'r') as Data:
                D = json.load(Data)

                if D["data"]["hoverData"]:  # check not empty
                    for district, values in D["data"]["hoverData"].items():
                        registered = values["registeredUsers"]
                        appopens = values["appOpens"]

                        clm['State'].append(i)
                        clm['Year'].append(int(j))
                        clm['Quarter'].append(int(k.strip('.json')))
                        clm['District'].append(district)
                        clm['RegisteredUsers'].append(registered)
                        clm['AppOpens'].append(appopens)

# Create DataFrame
Map_User = pd.DataFrame(clm)

# Print result
print(" Map User Data:")
print(Map_User)
