# 1. Import packages
import glob
import os
import pandas as pd
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

# 2. Working directory
current_path_s = os.getcwd()
path_s = current_path_s + "/html_files"
os.chdir(path_s)

tld_d = {"facebook_html_de_3320": "facebook.de", "Ebay-kleinanzeigen": "Ebay-kleinanzeigen.de"}

for file in glob.glob("*.html"):
    print(file)
    filename_s = os.path.splitext(file)[0]
    domain_and_tld_s = re.findall("^\w*.[a-zA-Z]*", filename_s)[0]
    if domain_and_tld_s in tld_d.keys():
        domain_and_tld_s = tld_d[domain_and_tld_s]
    with open(file) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
        link_l = []
        for link in soup.find_all('a'):
            href_link = link.get('href')
            if href_link is not None \
                    and href_link.startswith("#") is not True \
                    and "mailto" not in href_link:
                    if href_link.startswith("/"):
                        href_link = domain_and_tld_s + href_link
                    link_l.append(href_link)

                # href_link = urljoin(page.url, href_link)
                # if domain.replace("www.", "") in urlparse(href_link)[1]:
                    # print(href_link.strip())
                    # all_links.add((href_link.strip()))
                    # this_page_links.add(href_link.strip())
                    # references[href_link.strip()] = repr(page.url)

        textfile = open(filename_s + ".txt", "w")
        for link in link_l:
            if link is not None:
                textfile.write(link + "\n")
        textfile.close()