-- Group by: number of books per author
SELECT a.first || ' ' || a.last AS author_name,
       COUNT(b.book_id)         AS books_count
FROM authors a
LEFT JOIN books b ON b.author_id = a.author_id
GROUP BY a.author_id
ORDER BY books_count DESC, author_name ASC;
