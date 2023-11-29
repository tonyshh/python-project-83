from flask import Flask, request, redirect, url_for, flash, render_template
import os
import psycopg2
from dotenv import load_dotenv
import validators

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url_name = request.form['url']
        
        # Валидация URL
        if not validators.url(url_name):
            flash('Введите валидный URL.', 'danger')
        elif len(url_name) > 255:
            flash('URL не должен превышать 255 символов.', 'danger')
        else:
            # Если URL валидный, продолжаем с добавлением в базу данных
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
            # Перенаправление на главную страницу
            return redirect(url_for('index'))
    # Отображение главной страницы
    return render_template('index.html')


@app.route('/urls/<int:url_id>')
def url_details(url_id):
    database_url = os.getenv('DATABASE_URL')
    with psycopg2.connect(database_url) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM urls WHERE id = %s", (url_id,))
            url = cur.fetchone()
    if url is not None:
        return render_template('url_details.html', url=url)
    else:
        flash('URL с таким ID не найден.', 'danger')
        return redirect(url_for('index'))


@app.route('/urls')
def url_list():
    database_url = os.getenv('DATABASE_URL')
    with psycopg2.connect(database_url) as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM urls ORDER BY created_at DESC")
            urls = cur.fetchall()
    return render_template('url_list.html', urls=urls)


if __name__ == '__main__':
    app.run(debug=True)
