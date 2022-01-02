from bs4 import BeautifulSoup
import requests
import requests_html

from requests_html import HTMLSession
 
WEB_PAGE = "https://www.timeanddate.com/holidays/myanmar/"
WEB_FILE = "./myanmar_holidays.html"

holidays = []
 
# Using requests_html to render JavaScript
def get_web_page():
    # create an HTML Session object
    session = HTMLSession()
    # Use the object above to connect to needed webpage
    response = session.get(WEB_PAGE)
    # Run JavaScript code on webpage
    response.html.render()
 
    # Save web page to file
    with open(WEB_FILE, mode="w", encoding="utf-8") as fp:
        fp.write(response.html.html)
 
def read_web_file():
    try:
        open(WEB_FILE)
    except FileNotFoundError:
        get_web_page()
    finally:
        # Read the web page from file
        with open(WEB_FILE, mode="r", encoding="utf-8") as fp:
            content = fp.read()
        return BeautifulSoup(content, "html.parser")
 
# Read web file if it exists, load from internet if it doesn't exist
result = read_web_file()
all_holidays = result.find("tr", {"class": "showrow"})

# Adding the h3.name to the list
for holiday in all_holidays:
    all_holidays.append(holiday.string)

# Renaming the last value in a movie list
# temp = all_movies[-1]
# all_movies[-1] = f"1)" + temp

# Reverse the movie list
# all_movies.reverse()

# Create a movie.txt
with open("all holidays", mode="w", encoding="utf-8") as fp:
    for holiday in all_holidays:
        fp.writelines(holiday.string)