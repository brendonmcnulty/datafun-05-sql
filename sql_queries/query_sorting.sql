-- Sort: by year then title
SELECT book_id, title, year_published
FROM books
ORDER BY year_published ASC, title ASC;
