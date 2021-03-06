from fileinput import filename
from re import A
from tkinter import image_names
from webbrowser import get
from tqdm import tqdm
from bs4 import BeautifulSoup
from typing import List
from collections import Counter


import re
import requests
import os.path
import os

def get_season_races() -> List[str]:
    """
    DESCRIPTION:
        Returns the links of every race category specified from the users input.

    PARARMETERS:
        user_input (str): URL from user.

    RETURNS:
        race_links (str): List of URLS which have been fetched.
    
    EXAMPLE: 
        Enter link: https://www.f1-fansite.com/f1-wallpapers/.
    
    """

    # user_input = input("Please enter the F1: ")

    base_link = 'https://www.f1-fansite.com/f1-wallpapers/'
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}
    r = requests.get(base_link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    race_links = [e.get('href') for e in soup.select('ul.grid_list.col5 li a')]
    return race_links

################################################################################

def retreive_names_for_folder(links)-> List[str]:
    """
    DESCRIPTION:
        Returns a list of the folder names based on the race.

    PARARMETERS:
        links (str): Takes in the indiv race links from the get_season_races() function.

    RETURNS:
        race_folder_names (str): List of folder names to be created.
    
    EXAMPLE: 
        List returned (str): ['f1', .... ,'canadian'].
    
    """
    race_folder_names = []

    for link in links:
        base_link = link
        name = re.split(r'\s|-', str(base_link))
        title = name[-3]
        
        race_folder_names.append(title)

    return race_folder_names


def create_folders(folder_names):
    """
    DESCRIPTION:
        Creates folders based on names given from the Folder_names list.

    PARARMETERS:
        folder_names str(List): Takes in the indiv race names from the retreive_names_for_folder() function.

    RETURNS:
         (str): Creates folders with names from list in current dir.
    
    EXAMPLE: 
        List returned (str): australian_01, australian_02.
    
    """
    curent_dir = os.getcwd()

    for folder_name, count in Counter(folder_names).items():
        if count == 1:
            os.makedirs(os.path.join(curent_dir, folder_name), exist_ok=True)
        else:
            for index in range(count):
                os.makedirs(os.path.join(curent_dir, f"{folder_name}_{index+1:02}"), exist_ok=True)


################################################################################


# Create connection and fetch items
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}
# r = requests.get(base_link, headers=headers)
# soup = BeautifulSoup(r.content, 'lxml')
# links = get_season_races() 
# links = set(e.get('href') for e in soup.select('.gallery-item a'))

a_link = get_season_races()

# Create new list for links

# Create connection and download
for link in tqdm(a_link):
    respone = requests.get(link)

    file_name = link.split('/')[-1]    
    image_name = SAVE_FOLDER + '/' + file_name

    with open(image_name, 'wb') as file:
        file.write(respone.content)

# user_input = input("Please enter the F1: ")

get_season_races()
links = get_season_races()
retreive_names_for_folder(links)
fnames = retreive_names_for_folder(links)
create_folders(fnames)


