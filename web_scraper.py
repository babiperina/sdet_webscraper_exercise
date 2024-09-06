from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import re
from datetime import datetime  # Adicione esta linha
from date_utils import parse_date

def initialize_driver():
    driver = webdriver.Chrome()  # Ensure chromedriver is in your PATH or provide executable_path
    return driver

def search_qa_tools(driver):
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("QA Automation Tools")
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

    more_items = driver.find_element(By.XPATH, "//span[contains(@aria-label, 'outros itens')]")
    more_items.click()

    tools = []
    search_results = driver.find_elements(By.XPATH, "//*[@data-attrid='BreadthFirstSRP']")
    for result in search_results:
        tool_name = result.text
        tools.append(tool_name)

    tools = [item for item in tools if item != '']
    if len(tools) > 10:
        tools = tools[:10]

    return tools

def collect_news(driver, three_months_ago):
    news_tab = driver.find_element(By.XPATH, "//a[.//div[text()='Notícias']]")
    news_tab.click()
    time.sleep(3)

    news_articles = driver.find_elements(By.XPATH, "//*[@role='heading']/parent::*")
    pattern = re.compile(r"""
        ^[\w\-\.]+[\n\r]
        [\w\s,\'\-:&\.\(\)]+[\n\r]
        [\w\s,\'\-:&\.\(\)]+[\n\r]*
        \.\n
        (\d{1,2}\sde\s(?:jan|fev|mar|abr|mai|jun|jul|ago|set|out|nov|dez)\.\sde\s\d{4}|\d+\s\w+\satrás)$
        """, re.VERBOSE)

    filtered_articles = []
    for article in news_articles:
        article_text = article.text.strip()
        match = pattern.search(article_text)
        if match:
            date_str = match.group(1)
            article_date = parse_date(date_str, datetime.now())
            if article_date and article_date >= three_months_ago:
                filtered_articles.append(article_text)

    return filtered_articles
