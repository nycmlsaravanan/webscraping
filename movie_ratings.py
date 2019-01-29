# Import Libraries
from bs4 import BeautifulSoup
from requests import get
from random import randint
from warnings import warn
from time import sleep
from time import time
from IPython.core.display import clear_output
import pandas as pd

def populate_movie():
    # Webscraping the moviename
    name = container.h3.a.text
    movie_names.append(name)
    
    # Webscraping the year
    year = container.h3.find('span', class_ = 'lister-item-year').text
    movie_years.append(year)
   
    # Webscraping the IMDB rating
    imdb = float(container.strong.text)
    movie_imdb_ratings.append(imdb)
                
    # Webscraping the Metascore
    m_score = container.find('span', class_ = 'metascore').text
    movie_metascores.append(int(m_score))
                
    #WebScraping the number of votes
    vote = container.find('span', attrs = {'name':'nv'})['data-value']
    movie_votes.append(int(vote))

def populate_movie_ratings_dataframe():
    movie_ratings = pd.DataFrame({'movie': movie_names,
                              'year': movie_years,
                              'imdb': movie_imdb_ratings,
                              'metascore': movie_metascores,
                              'votes': movie_votes})
    return(movie_ratings)

def basic_info(movie_ratings):
    print(movie_ratings.info())
    print(movie_ratings.head(10))
    rows,columns=movie_ratings.shape
    print("there are ",rows," rows and ",columns," columns in the dataset mined from webscraping")
    movie_ratings = movie_ratings[['movie', 'year', 'imdb', 'metascore', 'votes']]
    movie_ratings.head()
    return(movie_ratings)

def write_to_csv(movie_ratings):
    movie_ratings.to_csv('movie_ratings.csv')

def basic_stats(movie_ratings):
     print('There are ',movie_ratings['year'].nunique(),' unique values of the years of the movies mined which are \n',movie_ratings['year'].unique(),' \n and the     distribution is \n',movie_ratings['year'].value_counts())
     print('There are ',movie_ratings['imdb'].nunique(),' unique values of the imdbs of the movies mined which are \n',movie_ratings['imdb'].unique(),' \n and the     distribution is \n',movie_ratings['imdb'].value_counts())
     print('There are ',movie_ratings['metascore'].nunique(),' unique values of the metascores of the movies mined which are \n',movie_ratings['metascore'].unique     (),' \n and the distribution is \n',movie_ratings['metascore'].value_counts())
     print('There are ',movie_ratings['votes'].nunique(),' unique values of the votess of the movies mined which are \n',movie_ratings['votes'].unique(),' \n and      the distribution is \n',movie_ratings['votes'].value_counts())
     print('The total number of null values for votes are ',movie_ratings['votes'].isnull().sum())
     print('The total number of null values for metascore are ',movie_ratings['metascore'].isnull().sum())
     print('The total number of null values for imdb are ',movie_ratings['imdb'].isnull().sum())
     print('The total number of null values for moviename  are ',movie_ratings['movie'].isnull().sum())
     movie_ratings.loc[:, 'year'] = movie_ratings['year'].str[-5:-1].astype(int)
     print('There are ',movie_ratings['year'].nunique(),' unique values of the years of the movies mined which are \n',movie_ratings['year'].unique(),' \n and the     distribution is \n',movie_ratings['year'].value_counts())
     #print(movie_ratings.agg({'imdb' : ['min','max','median','mean','std'], 'metascore' : ['min', 'max','median','mean','std'], 'votes' : ['min', 'max','median','     mean','std']}))
     movie_ratings['n_imdb'] = movie_ratings['imdb'] * 10
     movie_ratings.head(3)
     return(movie_ratings)

pages = [str(pg) for pg in range(1,6)]
headers = {"Accept-Language": "en-US, en;q=0.5"}
url_years = [str(yr) for yr in range(1999,2018)]
# Redeclaring the lists to store data in
movie_years = []
movie_names = []
movie_metascores = []
movie_imdb_ratings = []
movie_votes = []


# Preparing the monitoring of the loop
start_time = time()
requests = 0

# Loop through years in the interval 1999-2017
for year_url in url_years:

    # Page Loop 1-4
    for page in pages:

        # Get request 
        response = get('http://www.imdb.com/search/title?release_date=' + year_url + 
        '&sort=num_votes,desc&page=' + page, headers = headers)

        # Method for pausing the Loop
        sleep(randint(8,15))

        # Monitor the requests
        requests += 1
        elapsed_time = time() - start_time
        print('Request:{}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
        clear_output(wait = True)

        # non-200 status code check and Warning
        if response.status_code != 200:
            warn('Request: {}; Status code: {}'.format(requests, response.status_code))

        # Check for  number of requests  greater than expected which is 95
        if requests > 96:
            warn('Number of requests was greater than expected.')  
            break 

        # use beutifulsoup to Parse
        page_html = BeautifulSoup(response.text, 'html.parser')

        # Select all the 50 movie containers from this selected page
        mv_containers = page_html.find_all('div', class_ = 'lister-item mode-advanced')

        # For every movie of these 50
        for container in mv_containers:
            # If the movie has a Metascore, then:
            if container.find('div', class_ = 'ratings-metascore') is not None:

                #Webscraping the fields via the function populate_movie
                populate_movie()
# Create the dataframe with the five Lists via function populate_movie_ratings_dataframe
movie_ratings=populate_movie_ratings_dataframe()
# Get me the columnar information about the Dataframe via basic_info function
movie_ratings=basic_info(movie_ratings)
# Get me the next level of information like null values , unique values and value counts 
basic_stats(movie_ratings)

# Write the dataframe to csv file
write_to_csv(movie_ratings)
