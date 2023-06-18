# -*- coding: utf-8 -*-
"""
Created on Tue May  9 21:44:35 2023

@author: User
"""

import pandas as pd
from notion_client import Client


# 設定 Notion API Token 和 Database ID
notion = Client(auth="Your Notion Token")

database_id = "779c80efc94b483eaf6f5c6f653ef517"
               
# 取得資料庫中的所有資料
results = notion.databases.query(database_id).get("results")

# 將 Notion 資料轉換成 Pandas DataFrame
data = []
for item in results:
    try:
        date = item["properties"]["日期期間"]["select"]["name"]
    except:
        date = None
    try:
        name = item["properties"]["露營名稱"]["title"][0]["text"]["content"]
    except:
        name = None
    try:
        features = [option["name"] for option in item["properties"]["特點"]["multi_select"]]
    except:
        features = None
    try:
        drawbacks = [option["name"] for option in item["properties"]["缺點"]["multi_select"]]
    except:
        drawbacks = None
    try:
        location = item["properties"]["地點"]["select"]["name"]
    except:
        location = None
    try:
        visited = item["properties"]["去過"]["checkbox"]
    except:
        visited = None

    data.append([date, name, features, drawbacks, location, visited])

df = pd.DataFrame(data, columns=["日期期間", "露營名稱", "特點", "缺點", "地點", "去過"])

# 儲存成 CSV 格式
df.to_csv('camping_dataframe.csv', index=False)



