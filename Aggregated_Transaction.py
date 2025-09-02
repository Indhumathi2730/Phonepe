import pandas as pd
import json
import os

# Path to your aggregated transaction data
path = r"C:\Users\luna love\Downloads\Phonepe\pulse\data\aggregated\transaction\country\india\state"
Agg_state_list = os.listdir(path)
print("States found:", Agg_state_list)

# Data dictionary
clm = {
    'State': [],
    'Year': [],
    'Quarter': [],
    'Transaction_type': [],
    'Transaction_count': [],
    'Transaction_amount': []
}

# Loop through states, years, quarters
for i in Agg_state_list:
    p_i = os.path.join(path, i)
    Agg_yr = os.listdir(p_i)
    for j in Agg_yr:
        p_j = os.path.join(p_i, j)
        Agg_yr_list = os.listdir(p_j)
        for k in Agg_yr_list:
            p_k = os.path.join(p_j, k)
            with open(p_k, 'r') as Data:
                D = json.load(Data)
                if D['data']['transactionData']:  # ensure it's not empty
                    for z in D['data']['transactionData']:
                        Name = z['name']
                        count = z['paymentInstruments'][0]['count']
                        amount = z['paymentInstruments'][0]['amount']

                        clm['Transaction_type'].append(Name)
                        clm['Transaction_count'].append(count)
                        clm['Transaction_amount'].append(amount)
                        clm['State'].append(i)
                        clm['Year'].append(int(j))
                        clm['Quarter'].append(int(k.strip('.json')))

# Create DataFrame
Agg_Trans = pd.DataFrame(clm)

# Just print the DataFrame
print(" Aggregated Transaction Data:")
print(Agg_Trans)
