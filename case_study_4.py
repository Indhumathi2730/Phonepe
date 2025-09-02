import pandas as pd
from sqlalchemy import create_engine

# Database connection
user = "root"
password = "Ponnusamy%402730"   # use %40 instead of @
host = "localhost"
database = "phonepe"

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")
print("MySQL connection successful!\n")

def case_study_5():
    print(" Case Study 5: User Engagement and Growth Strategy")
    
    query = """
        SELECT 
            State,
            SUM(RegisteredUsers) AS total_users,
            SUM(AppOpens) AS total_app_opens,
            (SUM(AppOpens) / NULLIF(SUM(RegisteredUsers), 0)) AS engagement_ratio
        FROM aggregated_user
        GROUP BY State
        ORDER BY engagement_ratio DESC;
    """
    
    df = pd.read_sql(query, engine)
    print(df)
    return df

if __name__ == "__main__":
    case_study_5()
