-- Join: list books with author names
SELECT b.book_id,
       b.title,
       b.year_published,
       a.first || ' ' || a.last AS author_name
FROM books b
INNER JOIN authors a ON a.author_id = b.author_id
ORDER BY author_name ASC, b.title ASC;
