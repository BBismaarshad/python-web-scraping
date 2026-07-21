import random
import time  # Imported time for anti-blocking delay
from bs4 import BeautifulSoup
import pandas as pd
import requests

# Empty list to store data from all pages
all_products_data = []

# Scraping data from the first 3 pages (you can increase this range up to 50!)
for page_num in range(1, 4):

    # 1. Dynamic URL: Page number changes automatically in each loop iteration
    url = f"https://books.toscrape.com/catalogue/page-{page_num}.html"
    print(f"🚀 Scraping Page {page_num}: {url}")

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            " (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"

    if response.status_code != 200:
        print(f"❌ Failed to load Page {page_num}. Skipping...")
        continue

    soup = BeautifulSoup(response.text, "html.parser")
    products = soup.select("article.product_pod")

    # 2. Inner Loop: Extracting data for all products on the current page
    for product in products:
        title = product.select_one("h3 a")["title"]
        price = product.select_one("p.price_color").text

        # New Feature: Extract stock status (In Stock or Out of Stock)
        stock_status = product.select_one(
            "p.instock.availability"
        ).text.strip()

        product_info = {
            "Page No.": page_num,
            "Product Name": title,
            "Price": price,
            "Stock Status": stock_status,
        }
        all_products_data.append(product_info)

    # 3. Defensive Scraping: Pause after each page to avoid hitting server rate limits
    delay = random.uniform(2.0, 4.0)
    print(
        f"😴 Pausing for {delay:.2f} seconds to avoid overloading the"
        " server...\n"
    )
    time.sleep(delay)

# ==========================================
# --- EXPORT DATA & CREATE EXCEL/CSV WITH PANDAS ---
# ==========================================
df = pd.DataFrame(all_products_data)

# Data Cleaning: Removing extra symbols from the price column
df["Price"] = df["Price"].str.replace("Â", "", regex=False)

# Saving the final report
df.to_csv(
    "ecommerce_multipage_portfolio.csv", index=False, encoding="utf-8-sig"
)
print(
    f"🎉 Completion Alert! Clean data for a total of {len(df)} products saved to"
    " 'ecommerce_multipage_portfolio.csv'!"
)
