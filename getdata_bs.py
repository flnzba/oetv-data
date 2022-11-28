from bs4 import BeautifulSoup
import requests

url = 'https://www.oetv.at/rangliste/itn.html'

result = requests.get(url, timeout=20)

site = BeautifulSoup(result.text, "html.parser")
print(site.table.prettify)

# itn = site.find(text="ITN")
# parent_itn = itn[0].parent
# print(site.prettify)
# header = parent_itn.find("header")
# print(header.string) #print what was found within the first parent in the header of the table?