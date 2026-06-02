import requests
from bs4 import BeautifulSoup

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

url = 'https://habr.com/ru/articles/'
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('article', class_='tm-articles-list__item')

for article in articles:
    title_elem = article.find('h2', class_='tm-title tm-title_h2')
    title = title_elem.get_text(strip=True) if title_elem else ''
    
    link_elem = title_elem.find('a', class_='tm-title__link') if title_elem else None
    link = f'https://habr.com{link_elem["href"]}' if link_elem and link_elem.has_attr('href') else ''
    
    date_elem = article.find('span', class_='tm-article-snippet__datetime-published')
    date = date_elem.get_text(strip=True) if date_elem else ''
    
    article_html = str(article)
    
    found = False
    for word in KEYWORDS:
        if word.lower() in article_html.lower():
            found = True
            break
    
    if found:
        print(f'{date} – {title} – {link}')
