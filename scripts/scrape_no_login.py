# scripts/scrape_no_login.py

import requests
from bs4 import BeautifulSoup
import re
from utils import save_product, save_review

def scrape_amazon_product_reviews(url, product_name, model, color):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Enregistrer le produit et obtenir l'ID du produit
    product_id = save_product(product_name, model, color)

    reviews = soup.find_all('div', {'data-hook': 'review'})
    for review in reviews:
        review_text = review.find('span', {'data-hook': 'review-body'}).text.strip()
        rating = int(float(review.find('i', {'data-hook': 'review-star-rating'}).text.split()[0]))
        review_date = review.find('span', {'data-hook': 'review-date'}).text.strip()
        author = review.find('span', {'class': 'a-profile-name'}).text.strip()
        review_title = review.find('a', {'data-hook': 'review-title'}).text.strip()
        source = 'Amazon'
        likes = review.find('span', {'data-hook': 'helpful-vote-statement'}).text.strip() if review.find('span', {'data-hook': 'helpful-vote-statement'}) else '0'
        likes = int(re.search(r'\d+', likes.replace(',', '')).group()) if re.search(r'\d+', likes.replace(',', '')) else 0
        verified_purchase = bool(review.find('span', {'data-hook': 'avp-badge'}))
        responses = []
        advantages = []
        disadvantages = []

        data = {
            'product_id': product_id,
            'review_text': review_text,
            'rating': rating,
            'review_date': review_date,
            'author': author,
            'review_title': review_title,
            'source': source,
            'likes': likes,
            'verified_purchase': verified_purchase,
            'responses': responses,
            'advantages': advantages,
            'disadvantages': disadvantages
        }
        save_review(data)

if __name__ == '__main__':
    url = 'https://www.amazon.com/product-reviews/B09G9FPHY4/'  # Exemple d'URL pour les commentaires de l'iPhone 15 Pro Max
    product_name = 'iPhone 15 Pro Max'
    model = 'A2900'
    color = 'Space Black'
    scrape_amazon_product_reviews(url, product_name, model, color)
 
# scripts/scrape_bestbuy_reviews.py

import requests
from bs4 import BeautifulSoup
import re
from utils import save_product, save_review

def scrape_bestbuy_product_reviews(url, product_name, model, color):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Enregistrer le produit et obtenir l'ID du produit
    product_id = save_product(product_name, model, color)

    reviews_section = soup.find('div', {'class': 'reviews-content'})
    if not reviews_section:
        print("No reviews found")
        return

    reviews = reviews_section.find_all('div', {'class': 'ugc-review'})
    for review in reviews:
        review_text = review.find('p', {'class': 'pre-white-space'}).text.strip()
        rating = int(review.find('span', {'class': 'c-review-average'}).text.strip())
        review_date = review.find('time', {'class': 'submission-date'}).text.strip()
        author = review.find('span', {'class': 'submission-time'}).text.strip()
        review_title = review.find('h4', {'class': 'review-title'}).text.strip() if review.find('h4', {'class': 'ugc-review-title'}) else ''
        source = 'Best Buy'
        likes = review.find('button', {'class': 'like-count'}).text.strip() if review.find('button', {'class': 'like-count'}) else '0'
        likes = int(re.search(r'\d+', likes.replace(',', '')).group()) if re.search(r'\d+', likes.replace(',', '')) else 0
        verified_purchase = bool(review.find('div', {'class': 'verified-purchaser-mv-wapper'}))
        responses = []
        advantages = []
        disadvantages = []

        data = {
            'product_id': product_id,
            'review_text': review_text,
            'rating': rating,
            'review_date': review_date,
            'author': author,
            'review_title': review_title,
            'source': source,
            'likes': likes,
            'verified_purchase': verified_purchase,
            'responses': responses,
            'advantages': advantages,
            'disadvantages': disadvantages
        }
        save_review(data)

if __name__ == '__main__':
    url = 'https://www.bestbuy.com/site/apple-iphone-15-pro-max-256gb-natural-titanium-at-t/6525423.p?skuId=6525423#tabbed-customerreviews'  # URL pour les commentaires de l'iPhone 15 Pro Max sur Best Buy
    product_name = 'iPhone 15 Pro Max'
    model = 'A2900'
    color = 'Natural Titanium'
    scrape_bestbuy_product_reviews(url, product_name, model, color)

