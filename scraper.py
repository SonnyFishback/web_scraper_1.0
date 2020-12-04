import requests
from bs4 import BeautifulSoup

url = "https://ca.finance.yahoo.com/u/yahoo-finance/watchlists/the-berkshire-hathaway-portfolio"

# Initialize requests object.
r = requests.get(url)
# Initialize beautiful soup object.
soup = BeautifulSoup(r.content, "html.parser")

stocks = soup.select(".cwl-symbols tbody")
stock = stocks[0]

company_name = stock.select_one(".data-col1").text.strip()
last_price = stock.select_one(".data-col2").text.strip()
change = stock.select_one(".data-col3").text.strip()
percent_change = stock.select_one(".data-col4").text.strip()
market_time = stock.select_one(".data-col5").text.strip()
volume = stock.select_one(".data-col6").text.strip()
average_volume_3_months = stock.select_one(".data-col7").text.strip()
market_cap = stock.select_one(".data-col8").text.strip()

print(company_name, last_price, change, percent_change, market_time, volume, average_volume_3_months, market_cap)
