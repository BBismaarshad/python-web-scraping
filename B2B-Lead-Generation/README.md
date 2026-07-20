# 🚀 B2B Lead Generation & Web Scraping Engine

A robust, production-ready Python web scraping pipeline designed to extract business details, clean inconsistent data, and compile structured leads into client-ready Excel/CSV reports.

## ✨ Features
*   **Anti-Blocking Architecture:** Mimics real-browser handshakes using rotating User-Agents and tailored headers.
*   **Encoding & Data Cleaning Pipeline:** Built-in character normalizer to auto-clean corrupt currency symbols (e.g., garbled `Â` characters).
*   **Pandas-Powered Export:** Outputs structured, deduplicated `.csv` sheets instantly compatible with Microsoft Excel and Google Sheets.

## 🛠️ Built With
*   **Python 3**
*   **Requests:** For reliable HTML source downloads.
*   **BeautifulSoup4:** For fast DOM parsing and node selection.
*   **Pandas:** For structural data cleaning and export.

## 📊 Sample Output (Before vs After Data Cleaning)

| Raw Scraped Price | Cleaned Price (After Pandas Normalization) |
| :--- | :--- |
| `Â£51.77` | `£51.77` |
| `Â£53.74` | `£53.74` |

## ⚙️ Quick Start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt