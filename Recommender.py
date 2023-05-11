import requests
import lxml.html
from lxml import objectify
from bs4 import BeautifulSoup

# List for storing urls
urls_final = []
# Extract the metadata of the page
for i in range(1):

    url = 'https://online.datasciencedojo.com/blogs/?blogpage=' + str(i)
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'lxml')
    # Temporary lists for storing temporary data
    urls_temp_1 = []
    urls_temp_2 = []
    temp = []
    # From the metadata, get the relevant information.
    for h in soup.find_all('a'):
        a = h.get('href')
        # print(a)
        #print(a)
        urls_temp_1.append(a)
        #print(urls_temp_1)
    for i in urls_temp_1:
        if i != None:
            if 'blogs' in i:
                if 'blogpage' in i:
                    None
                else:
                    if 'auth' in i:
                        None
                    else:
                        urls_temp_2.append(i)
                        [temp.append(x) for x in urls_temp_2 if x not in temp]
                        #print("#############################################")
                        #print(temp)
                        for i in temp:
                            if i == 'https://online.datasciencedojo.com/blogs/':
                                None
                            else:
                                urls_final.append(i)
print(urls_final)
