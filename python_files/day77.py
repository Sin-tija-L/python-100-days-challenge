from flask import Flask, render_template, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Template for blog entries
@app.route('/blog1')
def blog1():
    return render_template('blog_template.html', 
                           heading="Celebrating Latvia's Birthday - A Nation's Journey", 
                           date=datetime.now().strftime("%Y-%m-%d"), 
                           content="""
                           On November 18th, Latvia proudly celebrated its 105th birthday, marking a significant milestone in the nation's history. This Baltic gem has a rich and vibrant culture, and its journey from independence to occupation and back to sovereignty is a testament to the resilience of its people.

    In this blog post, we delve into Latvia's fascinating history, exploring its cultural heritage, traditions, and the struggles it has overcome. From the beautiful landscapes of the Latvian countryside to the bustling streets of Riga, we'll take you on a virtual journey to this enchanting nation.

    Join us as we raise a toast to Latvia's enduring spirit and celebrate its remarkable 105 years of independence.
                           """)

@app.route('/blog2')
def blog2():
    return render_template('blog_template.html', 
                           heading="Python: The Swiss Army Knife of Programming Languages", 
                           date=datetime.now().strftime("%Y-%m-%d"), 
                           content="""
                           Python, often referred to as the "Swiss Army Knife" of programming languages, has become an indispensable tool for developers and data scientists worldwide. Its simplicity, versatility, and an extensive library ecosystem make it a powerhouse in the modern tech landscape.

    In this blog post, we dive into the world of Python, exploring its origins, growth, and practical applications. Whether you're a beginner looking to learn your first programming language or a seasoned developer seeking a powerful tool for web development, data analysis, or machine learning, Python has got you covered.

    Join us as we unravel the mysteries of Python and discover why it has earned a place as one of the most popular and beloved programming languages on the planet.
                           """)

# Shortened redirects
@app.route('/first-post')
def first_post():
    return redirect(url_for('blog1'))

@app.route('/second-post')
def second_post():
    return redirect(url_for('blog2'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
