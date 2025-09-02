import pymysql
from sqlalchemy import create_engine

# Import your 9 DataFrames from their files
from Aggregated_Transaction import Agg_Trans
from Aggregated_User import Agg_User
from Aggregated_Insurance import Agg_Ins
from Map_Transaction import Map_Trans
from Map_User import Map_User
from Map_Insurance import Map_Ins
from Top_Transaction import Top_Trans
from Top_User import Top_User
from Top_Insurance import Top_Ins

# MySQL login details
user = "root"
password = "Ponnusamy@2730"
host = "localhost"
port = 3306

# Since the password contains '@', encode it as %40
password_safe = password.replace("@", "%40")

# Step 1: Create database if it doesn't exist
conn = pymysql.connect(host=host, user=user, password=password, port=port)
cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS phonepe")
cursor.close()
conn.close()

# Step 2: Create SQLAlchemy engine for phonepe DB
engine = create_engine(f"mysql+pymysql://{user}:{password_safe}@{host}:{port}/phonepe")

# Step 3: Load DataFrames into MySQL tables
Agg_Trans.to_sql("aggregated_transaction", con=engine, if_exists="replace", index=False)
Agg_User.to_sql("aggregated_user", con=engine, if_exists="replace", index=False)
Agg_Ins.to_sql("aggregated_insurance", con=engine, if_exists="replace", index=False)

Map_Trans.to_sql("map_transaction", con=engine, if_exists="replace", index=False)
Map_User.to_sql("map_user", con=engine, if_exists="replace", index=False)
Map_Ins.to_sql("map_insurance", con=engine, if_exists="replace", index=False)

Top_Trans.to_sql("top_transaction", con=engine, if_exists="replace", index=False)
Top_User.to_sql("top_user", con=engine, if_exists="replace", index=False)
Top_Ins.to_sql("top_insurance", con=engine, if_exists="replace", index=False)

print(" All 9 DataFrames loaded into MySQL successfully!")
