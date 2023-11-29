from flask import Flask, request, redirect, url_for, flash, render_template
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url_name = request.form['url']
        database_url = os.getenv('DATABASE_URL')
        with psycopg2.connect(database_url) as conn:
            with conn.cursor() as cur:
                try:
                    cur.execute("INSERT INTO urls (name) VALUES (%s)", (url_name,))
                    conn.commit()
                    flash('URL успешно добавлен', 'success')
                except psycopg2.IntegrityError:
                    conn.rollback()
                    flash('URL уже существует', 'danger')
        return redirect(url_for('index'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
