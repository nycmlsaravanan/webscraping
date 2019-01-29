import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
######Let us look at the pyplot frequency plots and the seaborn frequency plots as well
def pyplot_and_sns_plots(movie_ratings,column):
    plt.hist(movie_ratings[column])
    plt.xlabel(column)
    plt.ylabel("Frequency ")
    plt.title("Pyplot Plotting frequency ")
    plt.show()
    sns.distplot(movie_ratings[column],kde=True,bins=12)
    plt.xlabel(column)
    plt.ylabel("Frequency ")
    plt.title("sns Plotting frequency  ")
    plt.show()
    sns.boxplot(y=movie_ratings[column] )
    plt.savefig(column)

movie_ratings=pd.read_csv('movie_ratings.csv')
print(movie_ratings.info())
#movie_ratings = pd.DataFrame({'movie': movie_names,
#                              'year': movie_years,
#                              'imdb': movie_imdb_ratings,
#                              'metascore': movie_metascores,
#                              'votes': movie_votes})
pyplot_and_sns_plots(movie_ratings,'imdb')
pyplot_and_sns_plots(movie_ratings,'n_imdb')
pyplot_and_sns_plots(movie_ratings,'metascore')
pyplot_and_sns_plots(movie_ratings,'votes')
pyplot_and_sns_plots(movie_ratings,'year')
print(movie_ratings.info())
print(movie_ratings.head(10))
rows,columns=movie_ratings.shape
print("there are ",rows," rows and ",columns," columns in the dataset mined from webscraping")
movie_ratings = movie_ratings[['movie', 'year', 'imdb', 'metascore', 'votes']]
#######Let us now see how the Target variable's unique values varies against the Predictor variables
print(movie_ratings.groupby('imdb').mean())
print(movie_ratings.groupby('metascore').mean())
