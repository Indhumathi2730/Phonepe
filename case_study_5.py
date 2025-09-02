import pandas as pd
from sqlalchemy import create_engine

# Database connection
user = "root"
password = "Ponnusamy%402730"   # use %40 instead of @
host = "localhost"
database = "phonepe"

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")
print("MySQL connection successful!\n")

def case_study_6():
    print(" Case Study 6: District-Level Growth Hotspots")
    
    query = """
        SELECT 
            State,
            District,
            SUM(Transaction_count) AS total_transactions,
            SUM(Transaction_amount) AS total_amount
        FROM map_transaction
        GROUP BY State, District
        ORDER BY total_amount DESC
        LIMIT 20;
    """
    
    df = pd.read_sql(query, engine)
    print(df)
    return df

if __name__ == "__main__":
    case_study_6()
