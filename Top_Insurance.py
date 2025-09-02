import pandas as pd
import json
import os

# Path to your top insurance data
path = r"C:\Users\luna love\Downloads\Phonepe\pulse\data\top\insurance\country\india\state"
top_ins_state_list = os.listdir(path)
#print("States found:", top_ins_state_list)

# Data dictionary
clm = {
    'State': [],
    'Year': [],
    'Quarter': [],
    'Entity_type': [],
    'Entity_name': [],
    'Insurance_count': [],
    'Insurance_amount': []
}

# Loop through states, years, quarters
for i in top_ins_state_list:
    p_i = os.path.join(path, i)
    Agg_yr = os.listdir(p_i)
    for j in Agg_yr:
        p_j = os.path.join(p_i, j)
        Agg_yr_list = os.listdir(p_j)
        for k in Agg_yr_list:
            p_k = os.path.join(p_j, k)
            with open(p_k, 'r') as Data:
                D = json.load(Data)

                # STATES
                if D["data"]["states"]:
                    for z in D["data"]["states"]:
                        clm['State'].append(i)
                        clm['Year'].append(int(j))
                        clm['Quarter'].append(int(k.strip('.json')))
                        clm['Entity_type'].append("State")
                        clm['Entity_name'].append(z["entityName"])
                        clm['Insurance_count'].append(z["metric"]["count"])
                        clm['Insurance_amount'].append(z["metric"]["amount"])

                # DISTRICTS
                if D["data"]["districts"]:
                    for z in D["data"]["districts"]:
                        clm['State'].append(i)
                        clm['Year'].append(int(j))
                        clm['Quarter'].append(int(k.strip('.json')))
                        clm['Entity_type'].append("District")
                        clm['Entity_name'].append(z["entityName"])
                        clm['Insurance_count'].append(z["metric"]["count"])
                        clm['Insurance_amount'].append(z["metric"]["amount"])

                # PINCODES
                if D["data"]["pincodes"]:
                    for z in D["data"]["pincodes"]:
                        clm['State'].append(i)
                        clm['Year'].append(int(j))
                        clm['Quarter'].append(int(k.strip('.json')))
                        clm['Entity_type'].append("Pincode")
                        clm['Entity_name'].append(z["entityName"])
                        clm['Insurance_count'].append(z["metric"]["count"])
                        clm['Insurance_amount'].append(z["metric"]["amount"])

# Create DataFrame
Top_Ins = pd.DataFrame(clm)

# Print result
print(" Top Insurance Data:")
print(Top_Ins.head(20))
