-- Example updates (match your existing schema)

-- 1) Fix a title typo (just an example update)
UPDATE books
SET title = 'Harry Potter and the Philosopher''s Stone'
WHERE book_id = 'b10';

-- 2) Bump a publication year (demonstration of numeric update)
UPDATE books
SET year_published = 1950
WHERE book_id = 'b02';  -- 1984
