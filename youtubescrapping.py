import os
import sys
# import beautiful soup
from bs4 import BeautifulSoup
import requests
import json
# import plotting library from matplotlib
import matplotlib.pyplot as plt

def get_list_of_titles():
    """Ask the user to enter the list of books,one per line"""
    books = []
    while True:
        title = input("Enter a book title: ")
        if title == "":
            break
        books.append(title)
    return books
# Get the GoodReads API key from the environment variable
# If it's not set, use the default key
api_key = os.environ.get("GOODREADS_API_KEY")
if api_key is None:
    # print an error message and exit
    print("Error: GoodReads API key not found")
    sys.exit()

def scrape_goodreads(titles):
    """get the avaerage ratig of each books from GoodReads and return it in an array"""
    # create an empty list to store the ratings
    ratings = []
    # loop through the list of books
    for title in titles:
        # get the url for the book
        url = "https://www.goodreads.com/search/index.xml"
        # get the response from the url
        response = requests.get(url, params={"key": api_key, "q": title})
        # check if the response is successful
        if response.status_code != 200:
            print("Error: {}".format(response.status_code))
            break
        # parse the response as xml
        xml = BeautifulSoup(response.text, "xml")
        # get the average rating from the xml
        rating = float(xml.find("average_rating").text)
        # append the rating to the list
        ratings.append(rating)
    return ratings
def show_ratings(titles,ratings):
    """show the ratings in a bar chart"""
    # create a bar chart
    plt.bar(titles,ratings)
    # show the chart
    plt.show()

titles=get_list_of_titles()
ratings=scrape_goodreads(titles)
show_ratings(titles,ratings)



