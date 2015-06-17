'''
Pandas Homework with IMDB data
'''

'''
BASIC LEVEL
'''
import pandas as pd

# read in 'imdb_1000.csv' and store it in a DataFrame named movies
movies = pd.read_csv('imdb_1000.csv')

# check the number of rows and columns
movies.shape
# check the data type of each column
movies.dtypes
# calculate the average movie duration
movies.describe()
# sort the DataFrame by duration to find the shortest and longest movies
movies.sort('duration').head(1) # freaks
movies.sort('duration').tail(1) # Hamlet
'''
INTERMEDIATE LEVEL
'''

# count how many movies have each of the content ratings
movies.groupby('content_rating').content_rating.count()
# convert the following content ratings to "UNRATED": NOT RATED, APPROVED, PASSED, GP
movies.content_rating.replace('NOT RATED','UNRATED', inplace=True)
movies.content_rating.replace('APPROVED','UNRATED', inplace=True)
movies.content_rating.replace('PASSED','UNRATED', inplace=True)
movies.content_rating.replace('GP','UNRATED', inplace=True)
# convert the following content ratings to "NC-17": X, TV-MA
movies.content_rating.replace('X','NC-17', inplace=True)
movies.content_rating.replace('TV-MA','NC-17', inplace=True)

# count the number of missing values in each column
movies.isnull().sum() # only content rating, 3 of them
# if there are missing values: examine them, then fill them in with "reasonable" values
movies[movies.content_rating.isnull()]
movies.content_rating.value_counts()
movies.content_rating.fillna(value='UNRATED', inplace=True)
# calculate the average star rating for movies 2 hours or longer,
movies[movies.duration>=120].star_rating.mean()
# and compare that with the average star rating for movies shorter than 2 hours
movies[movies.duration<120].star_rating.mean()
# not much diffence only 7.95 for the longer and 7.84 for the shorter

# calculate the average duration for each genre
movies.groupby('genre').duration.mean().order() # History the shortest
'''
ADVANCED LEVEL
'''
movies.title.duplicated().sum() # yes 4
# check if there are multiple movies with the same title, and if so, determine if they are the same movie
movies.duplicated().sum() # but the rows are different
# calculate the average star rating for each genre, but only include genres with at least 10 movies

'''
BONUS
'''

# Figure out something "interesting" using the actors data!
