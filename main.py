import requests
from bs4 import BeautifulSoup

user_input = input("Wich year do you want to travel to? Type the data in this format YYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{user_input}"

response = requests.get(URL)
billboard_page = response.text

soup = BeautifulSoup(billboard_page, 'html.parser')
all_songs = soup.find_all(name="h3", class_="a-no-trucate")
all_titles = [song.getText().strip() for song in all_songs]
print(all_titles)