# Установка зависимостей
make install

# Применение миграций к базе данных
psql -a -d $DATABASE_URL -f database.sql