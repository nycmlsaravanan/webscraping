# webscraping
Webscrape http://www.imdb.com/search/title and derive value for imdb scores and metascores 

The python code scrapes http://www.imdb.com/search/title by appending Year and pages to the base URL.
For every year , five (5) pages are scraped .
Movies for 19 years are chosen from 1999-2018 .
So in Total 19X5 = 95 pages are scraped 
Five attributes are chosen viz name , imdb , metascore , votes and Year 
The crawl rate is controlled by the function sleep(randint(8,15)) which asks the program to sleep randomly from 8 to 15 seconds
The request rate is also monitored . 

Five  lists are defined and initialized and they are populated after scraping the attributes name , imdb , metascore , votes and Year 
After all 95 pages are scraped , the lists are used to populate the dataframe which is then also written to csv file

The dataframe is mined to get value out of the columns 


