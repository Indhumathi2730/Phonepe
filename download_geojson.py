import requests

url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"

r = requests.get(url)
r.raise_for_status()  # will error if link is broken

with open("india_states.geojson", "w", encoding="utf-8") as f:
    f.write(r.text)

print("✅ india_states.geojson downloaded successfully")
