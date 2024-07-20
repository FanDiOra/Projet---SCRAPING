# scripts/utils.py

import psycopg2
from database.db_config import config

def save_product(product_name, model, color):
    params = config()
    conn = psycopg2.connect(**params)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO products (product_name, model, color)
        VALUES (%s, %s, %s) RETURNING product_id
    """, (product_name, model, color))
    product_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return product_id

def save_review(data):
    params = config()
    conn = psycopg2.connect(**params)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO reviews (
            product_id, review_text, rating, review_date, author,
            review_title, source, likes, verified_purchase, responses,
            advantages, disadvantages)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        data['product_id'],
        data['review_text'],
        data['rating'],
        data['review_date'],
        data['author'],
        data['review_title'],
        data['source'],
        data['likes'],
        data['verified_purchase'],
        data['responses'],
        data['advantages'],
        data['disadvantages']
    ))
    conn.commit()
    cursor.close()
    conn.close()
