from playwright.sync_api import sync_playwright
import time
import requests

with sync_playwright() as p:
    start = time.time()
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.google.com.br/imghp?hl=en&authuser=0&ogbl")
    page.fill('//*[@id="sbtc"]/div/div[2]/input', 'Stallone')
    page.keyboard.press('Enter')
    time.sleep(1)
    page.mouse.click(145,376)
    time.sleep(0.7)

    url = []

    for i in range(0,30):
        element = page.query_selector('#Sva75c > div > div > div.pxAole > div.tvh9oe.BIB1wf > c-wiz > div > div.OUZ5W > div.zjoqD > div.qdnLaf.isv-id > div.v4dQwb > a > img')
        time.sleep(0.7)
        temp = element.get_attribute('src')
        if 'https' in temp:
            url.append(temp)
        time.sleep(0.7)
        page.keyboard.press('ArrowRight')


    browser.close()
print(url)
    
#Salva imagem
#f = open('01.jpg', 'wb')
#f.write(requests.get(url1).content)
#f.close()
#print('file saved')

end = time.time()

print('exec time is:',end-start)