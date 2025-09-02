import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# Database connection
user = "root"
password = quote_plus("Ponnusamy@2730")  # Encoded to handle '@'
host = "localhost"
database = "phonepe"

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")
print("MySQL connection successful!\n")

def case_study_2():
    print(" Case Study 2: Device Dominance and User Engagement Analysis")
    
    query = """
        SELECT 
            State,
            SUM(RegisteredUsers) AS total_users,
            SUM(AppOpens) AS total_app_opens
        FROM aggregated_user
        GROUP BY State
        ORDER BY total_users DESC;
    """
    
    df = pd.read_sql(query, engine)
    print(df)
    return df

if __name__ == "__main__":
    case_study_2()
