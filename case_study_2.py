import pandas as pd
from sqlalchemy import create_engine

# Database connection (encoded @ as %40)
user = "root"
password = "Ponnusamy%402730"   # @ replaced with %40
host = "localhost"
database = "phonepe"

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")
print("MySQL connection successful!\n")

def case_study_3():
    print(" Case Study 3: Insurance Penetration and Growth Potential Analysis")
    
    query = """
        SELECT 
            State,
            Year,
            Quarter,
            SUM(Insurance_count) AS total_policies,
            SUM(Insurance_amount) AS total_premium
        FROM aggregated_insurance
        GROUP BY State, Year, Quarter
        ORDER BY Year, Quarter;
    """
    
    df = pd.read_sql(query, engine)
    print(df)
    return df

if __name__ == "__main__":
    case_study_3()
