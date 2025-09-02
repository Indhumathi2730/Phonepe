import pandas as pd
import json
import os

# Path to your aggregated user data
path = r"C:\Users\luna love\Downloads\Phonepe\pulse\data\aggregated\user\country\india\state"
Agg_user_state_list = os.listdir(path)
#print("States found:", Agg_user_state_list)
# Data dictionary
clm = {
    'State': [],
    'Year': [],
    'Quarter': [],
    'Brand': [],
    'User_count': [],
    'User_percentage': [],
    'RegisteredUsers': [],
    'AppOpens': []
}

# Loop through states, years, quarters
for i in Agg_user_state_list:
    p_i = os.path.join(path, i)
    Agg_yr = os.listdir(p_i)
    for j in Agg_yr:
        p_j = os.path.join(p_i, j)
        Agg_yr_list = os.listdir(p_j)
        for k in Agg_yr_list:
            p_k = os.path.join(p_j, k)
            with open(p_k, 'r') as Data:
                D = json.load(Data)

                # Get totals (registered users, app opens)
                registeredUsers = D["data"]["aggregated"]["registeredUsers"]
                appOpens = D["data"]["aggregated"]["appOpens"]

                # For each device brand
                if D["data"]["usersByDevice"]:
                    for z in D["data"]["usersByDevice"]:
                        brand = z["brand"]
                        count = z["count"]
                        percentage = z["percentage"]

                        clm['State'].append(i)
                        clm['Year'].append(int(j))
                        clm['Quarter'].append(int(k.strip('.json')))
                        clm['Brand'].append(brand)
                        clm['User_count'].append(count)
                        clm['User_percentage'].append(percentage)
                        clm['RegisteredUsers'].append(registeredUsers)
                        clm['AppOpens'].append(appOpens)

# Create DataFrame
Agg_User = pd.DataFrame(clm)

#  Print result
print("Aggregated User Data:")
print(Agg_User) 
