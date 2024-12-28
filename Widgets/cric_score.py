import requests
import pandas as pd
import json

API_TOKEN = '46PpY7xpOLUwKJz30z7NLDhpdnM8G00vK4CfJtilI7hbCMxszalZDwwct2IN'

response = requests.get(f"https://cricket.sportmonks.com/api/v2.0/livescores?api_token={API_TOKEN}")

json_data = json.dumps(response.json(),indent=4)

print(json_data)