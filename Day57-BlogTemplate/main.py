from flask import Flask, render_template, request
import requests

app = Flask(__name__)
global blog_data
@app.route('/')
def home():
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    blog_data = response.json()
    return render_template("index.html", all_posts = blog_data)

@app.route('/blog/<num>')
def blog(num):
    number = int(num)
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(blog_url)
    blog_data = response.json()
    return render_template("post.html", number = number, all_posts = blog_data)

if __name__ == "__main__":
    app.run(debug=True)
