from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import random
import requests
import json

from bs4 import BeautifulSoup
import time, os

driver = webdriver.Chrome('/Users/Rohit/chromedriver')
# time.sleep(20)

# capa = DesiredCapabilities.CHROME
# capa["pageLoadStrategy"] = "none"

# driver = webdriver.Chrome('/Users/Rohit/chromedriver', desired_capabilities=capa)
# wait = WebDriverWait(driver, 20)

driver.get('https://www.linkedin.com/')

# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#login-email')))

# driver.execute_script("window.stop();")
# driver.get('https://www.linkedin.com/')
email_box = driver.find_element_by_css_selector('#login-email')
email_box.send_keys(os.getenv('LINKEDIN_EMAIL'))
password_box = driver.find_element_by_css_selector('#login-password')
password_box.send_keys(os.getenv('LINKEDIN_PASSWORD'))
email_box.submit()

visited = []
to_visit = [(u'https://www.linkedin.com/in/dattascience', 'ROOT')]
while len(to_visit) > 0:
	url_tuple = to_visit.pop(0)
	url = url_tuple[0].rstrip('/')
	referrer = url_tuple[1].rstrip('/')
	visited.append(url)

	# get job and experience
	driver.get(url)

	time.sleep(random.random()*4+2)
	try:
		html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
		soup = BeautifulSoup(html, 'html.parser')
		name = soup.find('h1', attrs={'class': 'pv-top-card-section__name'}).text
		# print name
		experience_section = soup.find('section', attrs={"class":"experience-section"})
		current_exp = experience_section.find('div', attrs={'class': 'pv-entity__summary-info'})
		job = (current_exp.find('h3')).text.upper()
		company = current_exp.find('span', attrs={'class': 'pv-entity__secondary-title'}).text.upper()

		try:
			# browse through the list of others viewed
			list_of_others = soup.find('ul', attrs={'class': 'browsemap'})
			for li in list_of_others.findAll('li'):
				url_suffix = li.find('a')['href']
				full_url = 'https://www.linkedin.com%s' % url_suffix
				full_url = full_url.rstrip('/')
				if full_url not in visited:
					to_visit.append((full_url, url))
		except Exception as e:
			print('unable to parse list')

		try:
			location = current_exp.find('h4', attrs={'class': 'pv-entity__location'}).find('span', class_=lambda x: x != 'visually-hidden').text.upper()
		except Exception:
			print('No Location Info Found')

		if ',' in location and not location.lower().endswith('area'):
			city = location.split(',')[0].rstrip()
			state = location.split(',')[1].lstrip()
		else:
			truncated = location.lower()
			if location.lower().endswith('area'):
				if location.lower().startswith('greater'):
					truncated = truncated.split(' ', 1)[1]
				truncated = truncated.rsplit(' ', 1)[0]

			# query google maps places api
			r = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key={}'.format(truncated.replace(' ', '%20'), os.getenv('GOOGLE_MAPS_API_KEY')))
			formatted_addr = json.loads(r.text)['results'][0]['formatted_address']
			if not formatted_addr.endswith(', USA'):
				continue

			# print formatted_addr
			truncated = formatted_addr.rstrip(', USA')
			city = formatted_addr.split(',')[0].rstrip().upper()
			state = formatted_addr.split(',')[1].lstrip().upper()

			if 'San Francisco' in formatted_addr:
				city = 'SAN FRANCISCO'
				state = 'CA'

		with open("evonne.tsv", "a") as myfile:
			myfile.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(name, url, job, company, state, city, referrer))
			# myfile.write("{}\t{}\t{}\t{}\t{}\n".format(name, job, company, url, referrer))

	except Exception as e:
		print 'Failed to load properly for {}'.format(url)
		print e


time.sleep(10)
driver.quit()