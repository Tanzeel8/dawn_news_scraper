# Dawn News Scraper

A Python web scraper that collects the latest headlines from
[Dawn News](https://www.dawn.com/latest-news) and saves them to CSV and Excel files.

## Features
- Fetches the latest headlines and article links from Dawn News
- Removes duplicate headlines
- Saves the data to CSV and Excel
- Stops with a clear error if the website request fails

## Tools used
Python, Requests, BeautifulSoup, pandas, openpyxl

## How to run
```bash
# 1. Clone this repository
git clone https://github.com/Tanzeel8/dawn_news_scraper.git
cd dawn_news_scraper

# 2. Install the libraries
pip install -r requirements.txt

# 3. Run the scraper
python news_scraper.py
```

## Output
The script creates an `output` folder with `news.csv` and `news.xlsx`.
A short sample is included in [`sample_output.csv`](sample_output.csv).

| title | link |
|-------|------|
| Another suspect arrested in Raiwind murder video case | https://www.dawn.com/news/1937681/another-suspect-arrested-in-raiwind-murder-video-case |
| Afghanistan bus crash kills 25, injures 27: authorities | https://www.dawn.com/news/1937671/afghanistan-bus-crash-kills-25-injures-27-authorities |

## Note
The website layout may change over time, so the scraper may need small updates later.

## License
MIT
