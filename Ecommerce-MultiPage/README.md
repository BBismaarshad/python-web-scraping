# 🛍️ Multi-Page E-commerce Product & Stock Scraper

An advanced, production-ready Python web scraping engine built to navigate through paginated e-commerce websites, extract multi-field product details, and implement defensive scraping mechanisms.

## ✨ Advanced Features
*   **Automated Pagination (Dynamic Looping):** Programmatically constructs and traverses multiple page URLs without requiring hardcoded lists.
*   **Defensive Scraping Architecture:** Integrates `time.sleep()` with `random.uniform()` to inject human-like random delays (2.0 to 4.0 seconds) between requests, effectively bypassing IP rate-limits and blocks.
*   **Multi-Field Extraction:** Captures not just titles and prices, but also deeply nested structural data like **Stock Availability Status**.
*   **Data Normalization:** Uses Pandas to sanitize scraped text, strip trailing whitespaces, and eliminate corrupt currency symbols.

## 🛠️ Tech Stack & Libraries
*   **Python 3** (Isolated via Virtual Environment `venv`)
*   **Requests:** For handling HTTP handshakes and page retrieval.
*   **BeautifulSoup4:** For advanced DOM traversing using CSS Selectors.
*   **Pandas:** For structural data organization, cleaning, and `.csv` compilation.

## 📊 Sample Dataset Preview

| Page No. | Product Name | Price | Stock Status |
| :--- | :--- | :--- | :--- |
| 1 | A Light in the Attic | £51.77 | In stock |
| 1 | Tipping the Velvet | £53.74 | In stock |
| 2 | In Her Wake | £12.84 | In stock |

## ⚙️ How to Run Locally

1. Activate your virtual environment:
   ```bash
   venv\Scripts\activate