import pandas as pd
import json
import os

# Path to your aggregated insurance data
path = r"C:\Users\luna love\Downloads\Phonepe\pulse\data\aggregated\insurance\country\india\state"
Agg_ins_state_list = os.listdir(path)
#print("States found:", Agg_ins_state_list)

# Data dictionary
clm = {
    'State': [],
    'Year': [],
    'Quarter': [],
    'Insurance_type': [],
    'Insurance_count': [],
    'Insurance_amount': []
}

# Loop through states, years, quarters
for i in Agg_ins_state_list:
    p_i = os.path.join(path, i)
    Agg_yr = os.listdir(p_i)
    for j in Agg_yr:
        p_j = os.path.join(p_i, j)
        Agg_yr_list = os.listdir(p_j)
        for k in Agg_yr_list:
            p_k = os.path.join(p_j, k)
            with open(p_k, 'r') as Data:
                D = json.load(Data)

                if D["data"]["transactionData"]:  # check not empty
                    for z in D["data"]["transactionData"]:
                        name = z["name"]  # "Insurance"
                        count = z["paymentInstruments"][0]["count"]
                        amount = z["paymentInstruments"][0]["amount"]

                        clm['State'].append(i)
                        clm['Year'].append(int(j))
                        clm['Quarter'].append(int(k.strip('.json')))
                        clm['Insurance_type'].append(name)
                        clm['Insurance_count'].append(count)
                        clm['Insurance_amount'].append(amount)

# Create DataFrame
Agg_Ins = pd.DataFrame(clm)

# Print result
print("Aggregated Insurance Data:")
print(Agg_Ins)
