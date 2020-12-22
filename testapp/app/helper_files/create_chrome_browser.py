from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import *

import time

def get_browser(PROXY):

    import os
    luminati_host = os.environ.get('LUMINATI_HOST')
    luminati_port = os.environ.get('LUMINATI_PORT')
    PROXY = 'http://' + luminati_host + ':' + luminati_port
    print(PROXY)

    proxy = Proxy()
    proxy.http_proxy = PROXY
    proxy.ftp_proxy = PROXY
    proxy.sslProxy = PROXY
    proxy.no_proxy = "localhost" #etc... ;)
    proxy.proxy_type = ProxyType.MANUAL

    capabilities = webdriver.DesiredCapabilities.CHROME

    proxy.add_to_capabilities(capabilities)
    # path = '/home/balu/balu/work/Courses/luminati+selinium/testapp/app/helper_files/chromedriver'
    # driver = webdriver.Chrome(executable_path = path, desired_capabilities=capabilities)
    
    driver = webdriver.Remote("http://172.20.128.1:4444/wd/hub", desired_capabilities=capabilities)
    url = 'https://lumtest.com/myip.json'
    driver.get(url)
    print(driver.page_source)
    
    return driver