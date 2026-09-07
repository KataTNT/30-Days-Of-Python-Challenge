"""
Project: 30 Days Of Python challenge
Author (Original): Asabeneh Yetayeh (https://github.com/Asabeneh/30-Days-Of-Python)
Day: 26 - Python for web (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/26_Day_Python_web/26_python_web.md)
Challenger: KataTNT
"""

from flask import Flask, render_template, request, redirect, url_for
import os
from collections import Counter
from collections import Counter
from string import punctuation
import nltk

app = Flask(__name__)
# to stop caching static file
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def home ():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming'
    return render_template('home.html', techs=techs, name = name, title = 'Home')

@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name = name, title = 'About Us')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/post', methods= ['GET','POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
        return render_template('post.html', name = name, title = name)
    if request.method =='POST':
        content = request.form['content']

        words = [word.strip(punctuation) for word in content.lower().split() if word.strip(punctuation)]
            
        char_count = len(content)
        word_count = len(words)
        word_counter = Counter(words).most_common()
        most_frequent = word_counter[0][0]

        nltk.download('averaged_perceptron_tagger_eng', quiet=True)
        words_pos_tags = nltk.pos_tag(words)
        lexical_tags = {'NN', 'VB', 'JJ', 'RB'}
        lexical_words = [word for word, tag in words_pos_tags if tag in lexical_tags]
        lexical_density = round((len(lexical_words) / word_count) * 100, 2)

        return render_template(
            'result.html',
            content=content,
            char_count=char_count,
            word_count=word_count,
            word_counter=word_counter,
            most_frequent=most_frequent,
            lexical_density=lexical_density
        )

if __name__ == '__main__':
    http_port = int(os.environ.get("HTTP_PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=http_port)