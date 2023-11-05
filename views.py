from flask import Blueprint, render_template

views = Blueprint(__name__, 'views')

# Default page
@views.route('/')
def home():
    return render_template('index.html')

# Submission page
@views.route('/original')
def original():
    return render_template('original.html')

# Submission page
@views.route('/story')
def story():
    return render_template('story.html')