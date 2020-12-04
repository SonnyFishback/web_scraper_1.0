import requests
from bs4 import BeautifulSoup

url = "https://ca.finance.yahoo.com/u/yahoo-finance/watchlists/the-berkshire-hathaway-portfolio"

# Initialize requests object.
r = requests.get(url)
# Initialize beautiful soup object.
soup = BeautifulSoup(r.content, "html.parser")
# Select all stocks.
stocks = soup.select(".cwl-symbols tbody tr")
# Array to store each stocks details.
stock_data_array = []
# Variable to keep track of which index is being accessed.
stock_index_count = 0
# Loop through stocks.
for stock in stocks:
    stock_details_dictionary = dict()
    
    stock_details_dictionary["company_name"] = stock.select_one(".data-col1").text.strip()
    stock_details_dictionary["last_price]"] = stock.select_one(".data-col2").text.strip()
    stock_details_dictionary["change"] = stock.select_one(".data-col3").text.strip()
    stock_details_dictionary["percent_change"] = stock.select_one(".data-col4").text.strip()
    stock_details_dictionary["market_time"] = stock.select_one(".data-col5").text.strip()
    stock_details_dictionary["volume"] = stock.select_one(".data-col6").text.strip()
    stock_details_dictionary["average_volume_3_months"] = stock.select_one(".data-col7").text.strip()
    stock_details_dictionary["market_cap"] = stock.select_one(".data-col8").text.strip()
    # stock_details_dictionary["stock_details_link_route"] = stock.select_one(".data-col0 a"["href"]
    # stock_details_dictionary["stock_details_link"] = f"https://ca.finance.yahoo.com{stock_details_dictionary["stock_details_link_route"]}"
    
    # Store data in stock_data_array.
    stock_data_array.append(stock_details_dictionary)
    # Print results of each loop.
    print(stock_data_array[stock_index_count])
    # Add 1 to the index count
    stock_index_count += 1



