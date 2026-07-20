import requests
from bs4 import BeautifulSoup
import pandas as pd

target_url = "https://books.toscrape.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print("Website se data laya ja raha hai... Please wait ⏳")
response = requests.get(target_url, headers=headers)

# 1. Encoding issue ko pehle hi seedha karne ke liye response ki encoding set karein
response.encoding = 'utf-8'

if response.status_code == 200:
    print("✅ Connection Successful! HTML download ho gaya.\n")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.select('article.product_pod')
    print(f"📦 Page par total {len(products)} leads mil gayin!\n")
    
    scraped_data = []
    
    for product in products:
        title = product.select_one('h3 a')['title']
        price = product.select_one('p.price_color').text
        
        data_row = {
            "Lead Name (Title)": title,
            "Price": price
        }
        scraped_data.append(data_row)
        
    # ==========================================
    # --- PANDAS & DATA CLEANING SHURU ---
    # ==========================================
    print("🧹 Data cleaning aur CSV generation shuru ho rahi hai...")
    
    # List ko DataFrame (Table) mein badlein
    df = pd.DataFrame(scraped_data)
    
    # Price column se garbled character 'Â' ko bilkul saaf karein
    df['Price'] = df['Price'].str.replace('Â', '', regex=False)
    
    # CSV file mein save karein (utf-8-sig Excel mein symbols ko kharab hone se bachata hai)
    output_file = "b2b_leads_portfolio.csv"
    df.to_csv(output_file, index=False, encoding='utf-8-sig')
    
    print(f"\n🎉 Mubarak Ho! Aapka clean data '{output_file}' mein save ho chuka hai!\n")
    
    # Terminal mein safai dekhne ke liye top 5 lines print karein
    print("--- PEHLI 5 CLEANED LEADS ---")
    print(df.head())
    
else:
    print(f"❌ Error aaya hai. Status Code: {response.status_code}")