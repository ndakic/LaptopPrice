from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from config import settings


def get_chrome_options():

	user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
					'Chrome/60.0.3112.113 Safari/537.36'

	chrome_options = Options()
	chrome_options.add_argument('user-agent=%s' % user_agent)
	chrome_options.add_argument("--headless")
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('start-maximized')
	chrome_options.add_argument('disable-infobars')
	chrome_options.add_argument("--disable-extensions")
	chrome_options.add_argument('--dns-prefetch-disable')
	chrome_options.add_argument("--disable-dev-shm-usage")

	return chrome_options


def get_webdriver():

	driver = webdriver.Chrome(
		executable_path=settings.scripts_root_path + "scraper/chromedriver",
		chrome_options=get_chrome_options())
	driver.set_page_load_timeout(30)

	return driver
