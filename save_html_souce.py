# save_html_source.py

import requests

# def save_html_source(url, file_path):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1'
#     }
#     response = requests.get(url, headers=headers)

#     if response.status_code == 200:
#         with open(file_path, 'w', encoding='utf-8') as file:
#             file.write(response.text)
#         print(f"HTML source saved to {file_path}")
#     else:
#         print(f"Failed to retrieve the page. Status code: {response.status_code}")

# if __name__ == '__main__':
#     # url = 'https://www.bestbuy.com/site/apple-iphone-15-pro-max-256gb-natural-titanium-at-t/6525423.p?skuId=6525423#tabbed-customerreviews'
#     url = 'https://www.bestbuy.com/site/reviews/apple-iphone-15-pro-max-256gb-natural-titanium-at-t/6525423?variant=A'
#     # url = 'https://www.amazon.com/Apple-iPhone-14-Pro-Max/dp/B0BYLZV28Y/ref=sr_1_1?crid=GQZ99ZMEVY2J&dib=eyJ2IjoiMSJ9.NTcG-E59ZcmRFFiNov6_M5J5Y0HTSJXbmApGS7TRT57Lyyt4GJsdK18sXvl8ku6VHjoBl1DrLOBrZbYwuABLig.EJLZDrlacxJuvbBz4oFlToNIBs_5E_LHdodUIbDpGZw&dib_tag=se&keywords=iphone%2B15%2Bpro%2Bmax&qid=1721510004&refinements=p_123%3A110955&rnid=85457740011&s=wireless&sprefix=iphone%2B15%2Bpro%2Bmax%2Caps%2C201&sr=1-1&th=1'
#     file_path = 'bestbuy_iphone15_pro_max.html'
#     save_html_source(url, file_path)

# Making a GET request 
r = requests.get('https://www.bestbuy.com/site/reviews/apple-iphone-15-pro-max-256gb-natural-titanium-at-t/6525423?variant=A') 
  
# check status code for response received 
# success code - 200 
print(r) 
  
# print content of request 
print(r.content) 