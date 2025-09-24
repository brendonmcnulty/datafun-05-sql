-- Insert authors (matches: author_id, first, last)
INSERT INTO authors (author_id, first, last) VALUES
('a01','Harper','Lee'),
('a02','George','Orwell'),
('a03','F. Scott','Fitzgerald'),
('a04','Aldous','Huxley'),
('a05','J.D.','Salinger'),
('a06','Ray','Bradbury'),
('a07','Jane','Austen'),
('a08','J.R.R.','Tolkien'),
('a09','J.K.','Rowling'),
('a10','Mark','Twain');

-- Insert books (matches: book_id, title, year_published, author_id)
INSERT INTO books (book_id, title, year_published, author_id) VALUES
('b01','To Kill a Mockingbird',1960,'a01'),
('b02','1984',1949,'a02'),
('b03','The Great Gatsby',1925,'a03'),
('b04','Brave New World',1932,'a04'),
('b05','The Catcher in the Rye',1951,'a05'),
('b06','Fahrenheit 451',1953,'a06'),
('b07','Pride and Prejudice',1813,'a07'),
('b08','The Hobbit',1937,'a08'),
('b09','The Lord of the Rings',1954,'a08'),
('b10','Harry Potter and the Philosopher''s Stone',1997,'a09');
