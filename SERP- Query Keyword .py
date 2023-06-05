#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup

# Query to search
query = 'app developer'

# Construct the URL for Google search
url = f"https://www.google.com/search?q={query}"

# Send a GET request to the URL
response = requests.get(url)

# Create BeautifulSoup object and specify the parser
soup = BeautifulSoup(response.text, 'html.parser')

# Find all search result links
search_results = soup.find_all('a')

# Process and print the search result links
for result in search_results:
    link = result.get('href')
    print(link)


# In[ ]:




