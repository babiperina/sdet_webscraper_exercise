from selenium import webdriver
from datetime import datetime
from dateutil.relativedelta import relativedelta
from web_scraper import initialize_driver, search_qa_tools, collect_news

def main():
    today = datetime(2024, 9, 5)
    three_months_ago = today - relativedelta(months=3)

    driver = initialize_driver()
    
    print("Searching for QA Automation Tools...")
    tools = search_qa_tools(driver)
    print("\nTop 10 QA Automation Tools (Based on Google Search):")
    for idx, tool in enumerate(tools, start=1):
        print(f"{idx}. {tool}")

    print("\nCollecting news from the last 3 months...")
    filtered_articles = collect_news(driver, three_months_ago)
    print("\nNews Headlines from the last 3 months:")
    for idx, article in enumerate(filtered_articles, start=1):
        print(f"\nHeadline {idx}:")
        print(article)

    driver.quit()

if __name__ == "__main__":
    main()
