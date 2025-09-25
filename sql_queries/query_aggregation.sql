-- Aggregations: total books and earliest/latest publication years
SELECT 
  COUNT(*)            AS total_books,
  MIN(year_published) AS earliest_year,
  MAX(year_published) AS latest_year
FROM books;
