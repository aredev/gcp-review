import datetime

from flask import Flask, request, render_template, redirect
from flask_wtf.csrf import CSRFProtect
from models import Text, Review
from dotenv import load_dotenv
load_dotenv()
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
csrf = CSRFProtect(app)


@app.route('/', methods=['GET'])
def upload():
    texts = Text.select()
    return render_template('list.html', texts=texts)


@app.route('/approve', methods=['POST'])
def approve_text():
    if 'text_id' not in request.form:
        return redirect('/', code=302)
    text_id = int(request.form.get('text_id'))

    try:
        text = Text.get(Text.id == text_id)
    except Exception:
        return redirect('/', code=302)

    if text.review.exists():
        return redirect('/', code=302)

    Review.create(text=text)
    return redirect('/', code=302)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
