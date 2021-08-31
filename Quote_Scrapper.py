from playwright.sync_api import sync_playwright
import time


with sync_playwright() as p:
    start = time.time()
    
    browser = p.chromium.launch()
    
    page = browser.new_page()
    
    page.goto("https://www.42frases.com.br/frases-curtas/")
    
    time.sleep(0.7)

    quote = []
    
    for i in range(1,31):
        elementHandle = page.query_selector("id=frases-"+ str(i))
        time.sleep(0.7)
        quote.append(elementHandle.inner_text())
        time.sleep(0.7)
        
    browser.close()
    end = time.time()

    print(quote)

    with open('quotes.txt', 'w') as file:
        for element in quote:
            file.write(element + "\n")

    print('Exec time: ', end - start)
