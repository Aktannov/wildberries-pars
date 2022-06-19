import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument(f'user-agent=Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)'
                     f' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Mobile Safari/537.36')
options.add_argument("--headless")

driver = webdriver.Chrome(
    executable_path='/home/aktai/wild/chromedriver/chromedriver',
    options=options
)


def get_parse(articul):
    driver.get(url=f'https://www.wildberries.ru/catalog/{articul}/detail.aspx?targetUrl=GP')
    time.sleep(3)
    data = driver.find_elements(By.CLASS_NAME, value='product-page__header')
    a = ''
    for i in data:
        a = i.text.split('\n')
    brend = a[0]
    product_name = a[1]
    try:
        seller_info = driver.find_element(By.CLASS_NAME, value='seller-info__name.seller-info__name--link').text
    except Exception:
        seller_info = brend
    fullprice = driver.find_element(By.CLASS_NAME,
                                    'price-block__old-price.j-final-saving.j-wba-card-item-show').text
    price = driver.find_element(By.CLASS_NAME, value='price-block__final-price').text
    product_data = {'brend': brend, 'product_name': product_name,
                    'fullprice': fullprice.replace(" ", ""), 'price': price.replace(" ", ""),
                    'seller_info': seller_info}
    return product_data




