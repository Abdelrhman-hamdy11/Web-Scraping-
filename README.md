# 🌐 Web Scraping Project


This project aims to scrape product data, including names and prices, of **Apple** products from **Jumia** and **Amazon** websites using **Python** and the **Cloudscraper** library. The collected data is then saved into CSV files for easy analysis and comparison between the two e-commerce platforms.

---

## 📊 Project Overview

The purpose of this project is to gather details about **Apple** products available on **Jumia** and **Amazon** platforms. By scraping product data such as names and prices, we can compare products across different e-commerce sites and analyze market trends. The data will be collected from multiple pages on both platforms to ensure a wide sample of available Apple products.

---

## 🧹 Web Scraping Process

### Websites Scraped:

1. **Jumia**  
   URL: `https://www.jumia.com.eg/catalog/?q=apple&page={i}#catalog-listing`  
   Scraping **Apple** products available for sale on Jumia Egypt.

2. **Amazon**  
   URL: `https://www.amazon.eg/s?k=apple&page={i}&language=en_AE`  
   Scraping **Apple** products available on Amazon Egypt.

### Data Collected:

- **Product Name**: Name of the Apple product.
- **Price**: Price of the Apple product.
- **Website**: Source website (either Jumia or Amazon).

### Pages Scraped:

- **Jumia**: Data is scraped from the first 14 pages (can be adjusted as needed).
- **Amazon**: Data is scraped from the first 19 pages (can be adjusted as needed).

---

## 🚀 Tools & Libraries Used

- **Python** 🐍: Main programming language.
- **Cloudscraper**: To bypass anti-bot protections while scraping the websites.
- **BeautifulSoup**: For parsing HTML and extracting relevant data.
- **csv**: To save the scraped data into CSV format.
- **Threading**: For parallel scraping of data from both platforms, speeding up the process.

---

## 📝 Functionality

The project consists of two functions:

1. **`scrape_amazon`**: Scrapes product details from Amazon.
2. **`scrape_jumia`**: Scrapes product details from Jumia.

Both functions are run concurrently using **threading**, which allows for efficient scraping of multiple pages from both platforms.

---

## 📂 Output Files

- **`apple_products.csv`**  
  This file contains the product data scraped from both Jumia and Amazon. It has the following columns:
  - **Product**: The name of the product.
  - **Price**: The price of the product.
  - **Website**: The platform from which the data was scraped (either Jumia or Amazon).

---
## 🧑‍💼 Author

**Abdelrhman Hamdy**  
[LinkedIn Profile](https://www.linkedin.com/in/abdelrahman-hamdii/)
