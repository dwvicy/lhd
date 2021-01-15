from bs4 import BeautifulSoup
import requests
import pickle
import pprint
import json

# Take input from user
yeor = input(
    "What year of GSOC are you insterested in since 2016 to 2020?(YYYY): ")

response = requests.get(
    'https://summerofcode.withgoogle.com/archive/'+yeor+'/organizations/')

soup = BeautifulSoup(response.text, 'html.parser')

gsoc = []


orgs_names_all = soup.find_all('h4', class_='organization-card__name')
org_name = [name.getText() for name in orgs_names_all]
orgs_desc_all = soup.find_all('div', class_='organization-card__tagline')
org_desc = [desc.getText() for desc in orgs_desc_all]

for i in range(0, len(org_name)):
    gsoc.append({"org name": org_name[i], "org desc": org_desc[i]})

print(json.dumps(gsoc, indent=1))

# gsoc = {
#     "name": org_name,
#     "desc": org_desc
# }
print(type(org_name))


# gsoc_orgs = pprint.pformat(gsoc)
try:
    with open('gsoc_'+yeor+'.json', 'w') as json_file:
        json.dump(gsoc, json_file, indent=1)
except:
    print("Unable to open file")
