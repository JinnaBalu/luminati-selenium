from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

def get_browser(proxy):

    import os
    luminati_host = os.environ.get('LUMINATI_HOST')
    luminati_port = os.environ.get('LUMINATI_PORT')
    # proxy = 'http://' + luminati_host + ':' + luminati_port
    # proxy = 'http://127.0.0.1:24000'
    proxy = 'http://zproxy.lum-superproxy.io:22225'
    print(proxy)
    # proxy=None
    try:
        chrome_options = webdriver.ChromeOptions()

        # disable images to speed up the page loading
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        
        if proxy not in ['None', None]:
            webdriver.DesiredCapabilities.CHROME['proxy'] = {
                "httpProxy":proxy,
                "ftpProxy":proxy,
                "sslProxy":proxy,
                "proxyType":"MANUAL"
            }
    except Exception as e:
        print(e, '!!!!!!!!!!')

    path = '/home/balu/balu/work/Courses/infinite-stack/luminati+selinium/job_funnel/app/helper_files/chromedriver'
    chrome = webdriver.Chrome(executable_path = path, options=chrome_options)
    # chrome = webdriver.Remote("http://"+ os.environ.get('STANDALONE_CHROME_HOST') + ":" + os.environ.get('STANDALONE_CHROME_PORT') + "/wd/hub", options=chrome_options)

    url = 'https://lumtest.com/myip.json'
    chrome.get(url)
    print(chrome.page_source)
    
    return chrome