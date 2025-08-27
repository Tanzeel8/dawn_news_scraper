import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Output folder
if not os.path.exists("output"):
    os.makedirs("output")

URL = "https://www.dawn.com/latest-news"
response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")

headlines = []

for item in soup.select("article h2 a"):
    title = item.get_text(strip=True)
    link = item["href"]
    if title and link:
        headlines.append({"title": title, "link": link})

df = pd.DataFrame(headlines)

# Save CSV
df.to_csv("output/news.csv", index=False, encoding="utf-8")

# Save Excel
df.to_excel("output/news.xlsx", index=False, engine="openpyxl")

print(f"✅ {len(headlines)} headlines scraped and saved to output/news.csv & output/news.xlsx")
