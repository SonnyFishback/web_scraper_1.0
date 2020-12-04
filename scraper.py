import requests
from bs4 import BeautifulSoup

url = "https://ca.finance.yahoo.com/u/yahoo-finance/watchlists/the-berkshire-hathaway-portfolio"

# Initialize requests object.
r = requests.get(url)
# Initialize beautiful soup object.
soup = BeautifulSoup(r.content, "html.parser")

# Select all stocks.
stocks = soup.select(".cwl-symbols tbody tr")
# Select one stock by index.
stock = stocks[0]

# Select stock details.
company_name = stock.select_one(".data-col1").text.strip()
last_price = stock.select_one(".data-col2").text.strip()
change = stock.select_one(".data-col3").text.strip()
percent_change = stock.select_one(".data-col4").text.strip()
market_time = stock.select_one(".data-col5").text.strip()
volume = stock.select_one(".data-col6").text.strip()
average_volume_3_months = stock.select_one(".data-col7").text.strip()
market_cap = stock.select_one(".data-col8").text.strip()
stock_details_link_route = stock.select_one(".data-col0 a")["href"]
stock_details_link = f"https://ca.finance.yahoo.com{stock_details_link_route}"



print(company_name, last_price, change, percent_change, market_time, volume, average_volume_3_months, market_cap, stock_details_link)


