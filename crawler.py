from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach", True) # this will keep the browser open after the script is finished

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = options)
driver.get("https://www.nulled.to/")
driver.maximize_window()

'''
    allowed_domains =  ["nulled.to", # funziona male senza tor
                        # XSS
                        "0x00sec.org",
                        "altenens.is",
                        # Exelab
                        "forum.exetools.com",
                        "www.go4expert.com",
                        "kernelmode.info/forum", # FORSE, MEGLIO CHIEDERE
                        "wilderssecurity.com",
                        ] # those are the DOMAINS that we will crawl -> is the only domain allowed here; otherwise we will crawl all the internet
    
    targetURLs =  ["https://www.nulled.to/", # funziona male senza tor
                    "https://xss.is/"
                    "https://0x00sec.org/",
                    "https://altenens.is/",
                    "https://forum.exetools.com/",
                    "https://www.go4expert.com/",
                    "https://www.kernelmode.info/forum/", # FORSE, MEGLIO CHIEDERE
                    "https://www.wilderssecurity.com/",
                    ] # those are the base URL; our starting point; we will start crawling from those URL(one at a time), a crawler has to find all the links in this page, then follows those links, and so on
'''
