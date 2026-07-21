import requests
from bs4 import BeautifulSoup
import pandas as pd
import time  # <-- Anti-blocking delay ke liye time import kiya
import random

# Khali list jisme saare pages ka data jama hoga
all_products_data = []

# Hum pehle 3 pages ka data nikalenge (Aap is range ko 50 tak bhi barha sakte hain!)
for page_num in range(1, 4):
    
    # 1. Dynamic URL: Har loop mein page number badal jayega
    url = f"https://books.toscrape.com/catalogue/page-{page_num}.html"
    print(f"🚀 Scraping Page {page_num}: {url}")
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    
    if response.status_code != 200:
        print(f"❌ Page {page_num} load nahi ho saka. Skipping...")
        continue
        
    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.select('article.product_pod')
    
    # 2. Inner Loop: Is page ke saare products ka data nikalna
    for product in products:
        title = product.select_one('h3 a')['title']
        price = product.select_one('p.price_color').text
        
        # New Feature: Stock status nikalna (In Stock hai ya Out of Stock)
        stock_status = product.select_one('p.instock.availability').text.strip()
        
        product_info = {
            "Page No.": page_num,
            "Product Name": title,
            "Price": price,
            "Stock Status": stock_status
        }
        all_products_data.append(product_info)
    
    # 3. Defensive Scraping: Har page ke baad break lena taake server block na kare
    delay = random.uniform(2.0, 4.0)
    print(f"😴 Server ko tang nahi karna, isliye {delay:.2f} seconds ka break...\n")
    time.sleep(delay)

# ==========================================
# --- PANDAS SE EXPORT & EXCEL SHEET BANANA ---
# ==========================================
df = pd.DataFrame(all_products_data)

# Data Cleaning: Price se extra symbols saaf karna
df['Price'] = df['Price'].str.replace('Â', '', regex=False)

# Final report save karna
df.to_csv("ecommerce_multipage_portfolio.csv", index=False, encoding='utf-8-sig')
print(f"🎉 Completion Alert! Total {len(df)} products ka clean data 'ecommerce_multipage_portfolio.csv' mein save ho gaya!")