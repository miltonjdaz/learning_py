""" Practice 1: List your books """

# In this first step, create a table to store your list of books. 
# It should have columns for id, name, and rating.

CREATE TABLE books (id INTEGER PRIMARY KEY, name TEXT, rating INTEGER);

# Now, add three of your favorite books into the table.

INSERT INTO books VALUES (1, "Harry Potter", 1);
INSERT INTO books VALUES (2, "Becoming a SELECT star", 2);
INSERT INTO books VALUES (3, "Lies My Teacher Told Me", 3);

""" Practice 2: Box office hits """"

CREATE TABLE movies (id INTEGER PRIMARY KEY, name TEXT, release_year INTEGER);
INSERT INTO movies VALUES (1, "Avatar", 2009);
INSERT INTO movies VALUES (2, "Titanic", 1997);
INSERT INTO movies VALUES (3, "Star Wars: Episode IV - A New Hope", 1977);
INSERT INTO movies VALUES (4, "Shrek 2", 2004);
INSERT INTO movies VALUES (5, "The Lion King", 1994);
INSERT INTO movies VALUES (6, "Disney's Up", 2009);

# This database contains an incomplete list of box office hits and their release year. 
# In this first step, just select all the movies.

SELECT * FROM movies; 

# Now, add a second query after the first, that retrieves only the movies that were released in the year 2000 or later, not before.
# Sort the results so that the earlier movies are listed first. 

SELECT * FROM movies WHERE release_year > 2000 ORDER BY release_year;