import pandas as pd
from sqlalchemy import create_engine

# Database connection (with encoded @ in password)
user = "root"
password = "Ponnusamy%402730"   # @ replaced with %40
host = "localhost"
database = "phonepe"

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")
print("MySQL connection successful!\n")

def case_study_4():
    print(" Case Study 4: Transaction Analysis for Market Expansion")
    
    query = """
        SELECT 
            State,
            SUM(Transaction_count) AS total_transactions,
            SUM(Transaction_amount) AS total_amount
        FROM aggregated_transaction
        GROUP BY State
        ORDER BY total_transactions DESC;
    """
    
    df = pd.read_sql(query, engine)
    print(df)
    return df

if __name__ == "__main__":
    case_study_4()
