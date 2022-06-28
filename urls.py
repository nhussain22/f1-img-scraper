from fileinput import filename
from re import A
from tkinter import image_names
from tqdm import tqdm
from bs4 import BeautifulSoup

import re
import requests
import os.path


base_link = 'https://www.f1-fansite.com/f1-wallpaper/wallpaper-photos-2022-miami-f1-gp/'
name = re.split(r'/\s|-', base_link)
title = name[-3]


curent_dir = os.getcwd()
check_dir = os.getcwd() + "/" + title


if not os.path.exists(check_dir):
    os.mkdir(curent_dir+ "/" + title)

SAVE_FOLDER = curent_dir + "/" + title

# Create connection and fetch items
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}
r = requests.get(base_link, headers=headers)
soup = BeautifulSoup(r.content, 'lxml')

links = set(e.get('href') for e in soup.select('.gallery-item a'))

# Create new list for links
a_link = [link for link in links]

# Create connection and download
for link in tqdm(a_link):
    respone = requests.get(link, headers=headers)

    file_name = link.split('/')[-1]    
    image_name = SAVE_FOLDER + '/' + file_name

    with open(image_name, 'wb') as file:
        file.write(respone.content)


