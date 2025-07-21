from flask import Flask, render_template, request
from bs4 import BeautifulSoup
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.secret_key = b'8x84nzaa262u2pf8e9^i'
csrf = CSRFProtect(app) 

def remove_unnecessary_tags(html):
    soup = BeautifulSoup(html, 'html.parser')

    tags_to_keep = ["table", "tr", "td", "th", "thead", "tbody", "a", "p", "br", "h1", "h2", "h3", "h4"]

    all_tags = soup.find_all()

    for tag in all_tags:
        if tag.name not in tags_to_keep:
            tag.unwrap()

    for tag in soup():
        for attribute in request.form.getlist('tags'):
            del tag[attribute]

    cleaned_html = str(soup)

    return cleaned_html

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        html_code = request.form['html_code']

        cleaned_html = remove_unnecessary_tags(html_code)

        return render_template('index.html', html_code=html_code, cleaned_html=cleaned_html)

    return render_template('index.html', html_code='', cleaned_html='')

if __name__ == '__main__':
    app.run(debug=True)