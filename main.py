from flask import Flask, render_template
from flask_cache_buster import CacheBuster
import requests
import os

# App configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(12)

# Use of flask_cache_buster to update CSS files
config = {
     'extensions': ['.js', '.css', '.csv'],
     'hash_size': 10
}
cache_buster = CacheBuster(config=config)
cache_buster.register_cache_buster(app)


# Main page with all news
@app.route('/')
def tout():
    title = []
    image = []
    description = []
    link = []
    url = 'http://newsapi.org/v2/top-headlines?country=fr&apiKey=e33b738887c24ccfb1717c2c674f3b42'
    response = requests.get(url)
    content = response.json()
    for i in range(10):
        if content['articles'][i]['urlToImage'] is not None and content['articles'][i]['description'] is not None:
            title.append(content['articles'][i]['title'])
            image.append(content['articles'][i]['urlToImage'])
            description.append(content['articles'][i]['description'])
            link.append(content['articles'][i]['url'])
        else:
            title.append(content['articles'][i+5]['title'])
            image.append(content['articles'][i+5]['urlToImage'])
            description.append(content['articles'][i+5]['description'])
            link.append(content['articles'][i+5]['url'])
    return render_template('index.html', title=title, image=image, description=description, link=link)


# Business page
@app.route('/business')
def business():
    title = []
    image = []
    description = []
    link = []
    url = 'http://newsapi.org/v2/top-headlines?country=fr&category=business&apiKey=e33b738887c24ccfb1717c2c674f3b42'
    response = requests.get(url)
    content = response.json()
    for i in range(10):
        title.append(content['articles'][i]['title'])
        image.append(content['articles'][i]['urlToImage'])
        description.append(content['articles'][i]['description'])
        link.append(content['articles'][i]['url'])
    return render_template('index.html', title=title, image=image, description=description, link=link)


# Entertainment page
@app.route('/divertissement')
def divertissement():
    title = []
    image = []
    description = []
    link = []
    url = 'http://newsapi.org/v2/top-headlines?country=fr&category=entertainment&apiKey=e33b738887c24ccfb1717c2c674f3b42'
    response = requests.get(url)
    content = response.json()
    for i in range(10):
        title.append(content['articles'][i]['title'])
        image.append(content['articles'][i]['urlToImage'])
        description.append(content['articles'][i]['description'])
        link.append(content['articles'][i]['url'])
    return render_template('index.html', title=title, image=image, description=description, link=link)


# Health page
@app.route('/santé')
def santé():
    title = []
    image = []
    description = []
    link = []
    url = 'http://newsapi.org/v2/top-headlines?country=fr&category=health&apiKey=e33b738887c24ccfb1717c2c674f3b42'
    response = requests.get(url)
    content = response.json()
    for i in range(10):
        title.append(content['articles'][i]['title'])
        image.append(content['articles'][i]['urlToImage'])
        description.append(content['articles'][i]['description'])
        link.append(content['articles'][i]['url'])
    return render_template('index.html', title=title, image=image, description=description, link=link)


# Science page
@app.route('/science')
def science():
    title = []
    image = []
    description = []
    link = []
    url = 'http://newsapi.org/v2/top-headlines?country=fr&category=science&apiKey=e33b738887c24ccfb1717c2c674f3b42'
    response = requests.get(url)
    content = response.json()
    for i in range(10):
        title.append(content['articles'][i]['title'])
        image.append(content['articles'][i]['urlToImage'])
        description.append(content['articles'][i]['description'])
        link.append(content['articles'][i]['url'])
    return render_template('index.html', title=title, image=image, description=description, link=link)


# Sport page
@app.route('/sport')
def sport():
    title = []
    image = []
    description = []
    link = []
    url = 'http://newsapi.org/v2/top-headlines?country=fr&category=sport&apiKey=e33b738887c24ccfb1717c2c674f3b42'
    response = requests.get(url)
    content = response.json()
    for i in range(10):
        title.append(content['articles'][i]['title'])
        image.append(content['articles'][i]['urlToImage'])
        description.append(content['articles'][i]['description'])
        link.append(content['articles'][i]['url'])
    return render_template('index.html', title=title, image=image, description=description, link=link)


# Technology page
@app.route('/technologie')
def technologie():
    title = []
    image = []
    description = []
    link = []
    url = 'http://newsapi.org/v2/top-headlines?country=fr&category=technology&apiKey=e33b738887c24ccfb1717c2c674f3b42'
    response = requests.get(url)
    content = response.json()
    for i in range(10):
        title.append(content['articles'][i]['title'])
        image.append(content['articles'][i]['urlToImage'])
        description.append(content['articles'][i]['description'])
        link.append(content['articles'][i]['url'])
    return render_template('index.html', title=title, image=image, description=description, link=link)


# Run app
if __name__ == "__main__":
    app.run(debug=True)
