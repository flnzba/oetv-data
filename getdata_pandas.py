# requiered packages: pandas, lxml

import pandas as pd

url = 'https://www.oetv.at/rangliste/itn.html'
table = pd.read_html(url)
# pandas reads with read_html methode the url and saves all tables in a list

print(len(table)) # print the number of tables saved

print(table[0]) #print first table