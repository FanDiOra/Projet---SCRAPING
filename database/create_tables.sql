-- create_tables.sql

CREATE TABLE products (
    product_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    model VARCHAR(255),
    color VARCHAR(255)
);

CREATE TABLE reviews (
    review_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    product_id INT REFERENCES products(product_id),
    review_text TEXT NOT NULL,
    rating INT CHECK (rating >= 1 AND rating <= 5),
    review_date DATE NOT NULL,
    author VARCHAR(255),
    review_title VARCHAR(255),
    source VARCHAR(255),
    likes INT,
    verified_purchase BOOLEAN,
    responses TEXT[],
    advantages TEXT[],
    disadvantages TEXT[]
);
