""" Practice 13 The last one! """
""" Next step: Go over Julia Evan's book """

CREATE TABLE clothes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    design TEXT);
    
INSERT INTO clothes (type, design)
    VALUES ("dress", "pink polka dots");
INSERT INTO clothes (type, design)
    VALUES ("pants", "rainbow tie-dye");
INSERT INTO clothes (type, design)
    VALUES ("blazer", "black sequin");

# Use ALTER to add a 'price' column to the table. 
# Then select all the columns in each row to see what your table looks like now.

ALTER TABLE clothes 
ADD price INTEGER;
SELECT * 
FROM clothes;

# Now assign each item a price, using UPDATE
# item 1 should be $10, item 2 should be $20, item 3 should be $30
# SELECT of all the rows to check that it worked as expected

UPDATE clothes SET price = 10 WHERE type = "dress";
UPDATE clothes SET price = 20 WHERE type = "pants";
UPDATE clothes SET price = 30 WHERE type = "blazer";

SELECT * FROM clothes

# Now insert a new item into the table that has all three attributes filled in, including 'price'. 
# Do one final SELECT of all the rows to check it worked.

INSERT INTO clothes (type, design, price) 
VALUES ("shirt", "red", 15);

SELECT * FROM clothes;