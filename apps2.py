import streamlit as st
import pandas as pd
import plotly.express as px
import json
from sqlalchemy import create_engine

# -------------------
# Database connection
# -------------------
user = "root"
password = "Ponnusamy%402730"   # encode @ as %40
host = "localhost"
database = "phonepe"
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")

# -------------------
# Load India GeoJSON
# -------------------
with open("india_states.geojson", "r", encoding="utf-8") as f:
    india_states = json.load(f)

# -------------------
# State Name Mapping
# -------------------
state_mapping = {
    "andaman-&-nicobar-islands": "Andaman & Nicobar",
    "andhra-pradesh": "Andhra Pradesh",
    "arunachal-pradesh": "Arunanchal Pradesh",
    "assam": "Assam",
    "bihar": "Bihar",
    "chandigarh": "Chandigarh",
    "chhattisgarh": "Chhattisgarh",
    "dadra-&-nagar-haveli-&-daman-&-diu": "Dadra and Nagar Haveli",
    "delhi": "NCT of Delhi",
    "goa": "Goa",
    "gujarat": "Gujarat",
    "haryana": "Haryana",
    "himachal-pradesh": "Himachal Pradesh",
    "jammu-&-kashmir": "Jammu & Kashmir",
    "jharkhand": "Jharkhand",
    "karnataka": "Karnataka",
    "kerala": "Kerala",
    "ladakh": "Ladakh",
    "lakshadweep": "Lakshadweep",
    "madhya-pradesh": "Madhya Pradesh",
    "maharashtra": "Maharashtra",
    "manipur": "Manipur",
    "meghalaya": "Meghalaya",
    "mizoram": "Mizoram",
    "nagaland": "Nagaland",
    "odisha": "Orissa",
    "puducherry": "Puducherry",
    "punjab": "Punjab",
    "rajasthan": "Rajasthan",
    "sikkim": "Sikkim",
    "tamil-nadu": "Tamil Nadu",
    "telangana": "Telangana",
    "tripura": "Tripura",
    "uttar-pradesh": "Uttar Pradesh",
    "uttarakhand": "Uttarakhand",
    "west-bengal": "West Bengal"
}

def clean_state_name(x):
    return state_mapping.get(x.lower().replace(" ", "-"), x.title())

# -------------------
# Streamlit Layout
# -------------------
st.set_page_config(page_title="PhonePe Pulse Dashboard", layout="wide")

# Dark theme styling
st.markdown("""
    <style>
        body { background-color: #0e1117; color: #fafafa; }
        .stMetric { background-color: #1e222d; border-radius: 10px; padding: 10px; }
    </style>
""", unsafe_allow_html=True)

st.title("PhonePe Pulse Dashboard")
st.markdown("### Dark Theme Analytics | Transactions • Users • Insurance • Growth")

# Sidebar for case study selection
case = st.sidebar.selectbox(
    "📌 Select Case Study",
    ["Case Study 2: Device Dominance",
     "Case Study 3: Insurance Growth",
     "Case Study 4: Transactions Analysis",
     "Case Study 5: User Engagement",
     "Case Study 6: District Hotspots"]
)

# -------------------
# Case Study 2
# -------------------
if "Case Study 2" in case:
    query = """
        SELECT State, SUM(RegisteredUsers) AS total_users, SUM(AppOpens) AS total_app_opens
        FROM aggregated_user
        GROUP BY State
        ORDER BY total_users DESC;
    """
    df = pd.read_sql(query, engine)
    df["State"] = df["State"].apply(clean_state_name)

    col1, col2 = st.columns(2)
    col1.metric(" Total Registered Users", f"{df['total_users'].sum():,}")
    col2.metric(" Total App Opens", f"{df['total_app_opens'].sum():,}")

    # Bar Chart
    fig_bar = px.bar(df.head(10), x="State", y="total_users",
                     color="total_users", text="total_users",
                     title="Top 10 States by Registered Users",
                     template="plotly_dark")
    fig_bar.update_traces(texttemplate='%{text:,}', textposition="outside")
    st.plotly_chart(fig_bar, use_container_width=True)

    # Map
    fig_map = px.choropleth(df, geojson=india_states, locations="State",
                            featureidkey="properties.ST_NM",
                            color="total_users",
                            hover_data={"total_users": True, "total_app_opens": True},
                            color_continuous_scale="Plasma",
                            title="Registered Users Across States",
                            template="plotly_dark")
    fig_map.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig_map, use_container_width=True)

# -------------------
# Case Study 3
# -------------------
elif "Case Study 3" in case:
    query = """
        SELECT State,
               SUM(Insurance_count) AS total_policies,
               SUM(Insurance_amount) AS total_premium
        FROM aggregated_insurance
        GROUP BY State
        ORDER BY total_premium DESC;
    """
    df = pd.read_sql(query, engine)
    df["State"] = df["State"].apply(clean_state_name)

    col1, col2 = st.columns(2)
    col1.metric(" Total Policies Issued", f"{df['total_policies'].sum():,}")
    col2.metric(" Total Premium Collected", f"{df['total_premium'].sum():,.0f}")

    # Histogram
    fig_hist = px.histogram(df, x="total_premium", nbins=20,
                            title="Distribution of Insurance Premiums Across States",
                            template="plotly_dark", color_discrete_sequence=["#EF553B"])
    st.plotly_chart(fig_hist, use_container_width=True)

    # Pie Chart
    fig_pie = px.pie(df.head(5), names="State", values="total_premium",
                     title="Top 5 States by Insurance Premium",
                     hole=0.4, template="plotly_dark",
                     color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig_pie, use_container_width=True)

# -------------------
# Case Study 4
# -------------------
elif "Case Study 4" in case:
    query = """
        SELECT State,
               SUM(Transaction_count) AS total_transactions,
               SUM(Transaction_amount) AS total_amount
        FROM aggregated_transaction
        GROUP BY State
        ORDER BY total_transactions DESC;
    """
    df = pd.read_sql(query, engine)
    df["State"] = df["State"].apply(clean_state_name)

    col1, col2 = st.columns(2)
    col1.metric("🔄 Total Transactions", f"{df['total_transactions'].sum():,}")
    col2.metric("💰 Total Amount (₹)", f"{df['total_amount'].sum():,.0f}")

    fig_bar = px.bar(df.head(10), x="State", y="total_transactions",
                     color="total_transactions", text="total_transactions",
                     title="Top 10 States by Transactions",
                     template="plotly_dark")
    st.plotly_chart(fig_bar, use_container_width=True)

    fig_map = px.choropleth(df, geojson=india_states, locations="State",
                            featureidkey="properties.ST_NM",
                            color="total_amount",
                            hover_data={"total_transactions": True, "total_amount": True},
                            color_continuous_scale="Viridis",
                            title="Transaction Value Across States",
                            template="plotly_dark")
    fig_map.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig_map, use_container_width=True)

# -------------------
# Case Study 5
# -------------------
elif "Case Study 5" in case:
    query = """
        SELECT State,
               SUM(RegisteredUsers) AS total_users,
               SUM(AppOpens) AS total_app_opens,
               (SUM(AppOpens) / NULLIF(SUM(RegisteredUsers),0)) AS engagement_ratio
        FROM aggregated_user
        GROUP BY State
        ORDER BY engagement_ratio DESC;
    """
    df = pd.read_sql(query, engine)
    df["State"] = df["State"].apply(clean_state_name)

    st.metric("⚡ Highest Engagement State", df.iloc[0]["State"])

    fig_bar = px.bar(df.head(10), x="State", y="engagement_ratio",
                     color="engagement_ratio", text="engagement_ratio",
                     title="Top 10 States by Engagement Ratio",
                     template="plotly_dark")
    st.plotly_chart(fig_bar, use_container_width=True)

    fig_pie = px.pie(df.head(5), names="State", values="engagement_ratio",
                     title="Top 5 States by Engagement Share",
                     hole=0.3, template="plotly_dark")
    st.plotly_chart(fig_pie, use_container_width=True)

# -------------------
# Case Study 6
# -------------------
elif "Case Study 6" in case:
    query = """
        SELECT State, District,
               SUM(Transaction_count) AS total_transactions,
               SUM(Transaction_amount) AS total_amount
        FROM map_transaction
        GROUP BY State, District
        ORDER BY total_amount DESC
        LIMIT 20;
    """
    df = pd.read_sql(query, engine)
    df["State"] = df["State"].apply(clean_state_name)

    st.metric(" Top District", f"{df.iloc[0]['District']} ({df.iloc[0]['total_amount']:,})")

    fig_bar = px.bar(df, x="District", y="total_amount",
                     color="total_amount", text="total_amount",
                     title="Top 20 Districts by Transaction Value",
                     template="plotly_dark")
    st.plotly_chart(fig_bar, use_container_width=True)
