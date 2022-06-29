from fileinput import filename
from re import A
from tkinter import image_names
from tqdm import tqdm
from bs4 import BeautifulSoup
from typing import List

import re
import requests
import os.path



def get_season_races() -> List[str]:
    """

    DESCRIPTION:
        Returns the links of every race category specified from the users input.

    PARARMETERS:
        user_input (str): URL from user.

    RETURNS:
        race_links (str): List of URLS which have been fetched
    
    EXAMPLE: 
        Enter link: https://www.f1-fansite.com/f1-wallpapers/
    
    """

    # user_input = input("Please enter the F1: ")

    base_link = 'https://www.f1-fansite.com/f1-wallpapers/'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}
    r = requests.get(base_link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    race_links = [e.get('href') for e in soup.select('ul.grid_list.col5 li a')]
    return race_links

################################################################################

def create_race_folders(links):
    for link in links:
        base_link = link
        name = re.split(r'\s|-', str(base_link))
        title = [name[-3]]

        for name in title:
            curent_dir = os.getcwd()
            check_dir = os.getcwd() + "/" + name


            if not os.path.exists(check_dir):
                os.mkdir(curent_dir+ "/" + name)

            SAVE_FOLDER = curent_dir + "/" + name




# # Create connection and fetch items
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}
# r = requests.get(base_link, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')

# links = set(e.get('href') for e in soup.select('.gallery-item a'))

# # Create new list for links
# a_link = [link for link in links]

# # Create connection and download
# for link in tqdm(a_link):
#     respone = requests.get(link, headers=headers)

#     file_name = link.split('/')[-1]    
#     image_name = SAVE_FOLDER + '/' + file_name

#     with open(image_name, 'wb') as file:
#         file.write(respone.content)

# user_input = input("Please enter the F1: ")

get_season_races()
links = get_season_races()
create_race_folders(links)

