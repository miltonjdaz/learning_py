""" Practice 1: List your books """

# In this first step, create a table to store your list of books. 
# It should have columns for id, name, and rating.

CREATE TABLE books (id INTEGER PRIMARY KEY, name TEXT, rating INTEGER);

# Now, add three of your favorite books into the table.

INSERT INTO books VALUES (1, "Harry Potter", 1);
INSERT INTO books VALUES (2, "Becoming a SELECT star", 2);
INSERT INTO books VALUES (3, "Lies My Teacher Told Me", 3);
