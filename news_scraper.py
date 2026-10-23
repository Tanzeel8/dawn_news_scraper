import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Make sure the output folder exists
os.makedirs("output", exist_ok=True)

URL = "https://www.dawn.com/latest-news"
response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=20)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")

headlines = []

for item in soup.select("article h2 a"):
    title = item.get_text(strip=True)
    link = item["href"]
    if title and link:
        headlines.append({"title": title, "link": link})

df = pd.DataFrame(headlines)

# Remove duplicate headlines
df = df.drop_duplicates(subset=["link"]).reset_index(drop=True)

# Save CSV (utf-8-sig so Excel shows special characters correctly)
df.to_csv("output/news.csv", index=False, encoding="utf-8-sig")

# Save Excel
df.to_excel("output/news.xlsx", index=False, engine="openpyxl")

print(f"✅ {len(df)} headlines scraped and saved to output/news.csv & output/news.xlsx")
