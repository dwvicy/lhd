from selenium import webdriver
import pickle
import pprint

# driver path
chrome_driver_path = '/Users/dwvicy/DevTools/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get('https://summerofcode.withgoogle.com/archive/2020/organizations/')

# Initializing orgs dictionary
orgs_by_year = {}
orgs_names = driver.find_elements_by_class_name('organization-card__name')
print(type(orgs_names))
orgs_desc = driver.find_elements_by_class_name('organization-card__tagline')

# adding the data into orgs_by_year

for i in range(len(orgs_names)):
    orgs_by_year[i] = {
        "desc of org": orgs_desc[i].text,
        "name of org": orgs_names[i].text,

    }

gsoc = pprint.pformat(orgs_by_year)

try:
    org_text = open('gsoc_orgs.txt', 'wt')
    org_text.write(gsoc)
    org_text.close()
except:
    print('Unable to open file')
