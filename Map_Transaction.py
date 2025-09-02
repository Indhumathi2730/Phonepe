import pandas as pd
import json
import os

# Path to your map transaction data
path = r"C:\Users\luna love\Downloads\Phonepe\pulse\data\map\transaction\hover\country\india\state"
map_trans_state_list = os.listdir(path)
#print("States found:", map_trans_state_list)

# Data dictionary
clm = {
    'State': [],
    'Year': [],
    'Quarter': [],
    'District': [],
    'Transaction_count': [],
    'Transaction_amount': []
}

# Loop through states, years, quarters
for i in map_trans_state_list:
    p_i = os.path.join(path, i)
    Agg_yr = os.listdir(p_i)
    for j in Agg_yr:
        p_j = os.path.join(p_i, j)
        Agg_yr_list = os.listdir(p_j)
        for k in Agg_yr_list:
            p_k = os.path.join(p_j, k)
            with open(p_k, 'r') as Data:
                D = json.load(Data)

                if D["data"]["hoverDataList"]:  # check not empty
                    for z in D["data"]["hoverDataList"]:
                        name = z["name"]
                        count = z["metric"][0]["count"]
                        amount = z["metric"][0]["amount"]

                        clm['State'].append(i)
                        clm['Year'].append(int(j))
                        clm['Quarter'].append(int(k.strip('.json')))
                        clm['District'].append(name)
                        clm['Transaction_count'].append(count)
                        clm['Transaction_amount'].append(amount)

# Create DataFrame
Map_Trans = pd.DataFrame(clm)

# Print result
print(" Map Transaction Data:")
print(Map_Trans)
