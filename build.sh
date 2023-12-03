# Install dependencies
make install

# Apply database migrations
psql -a -d $DATABASE_URL -f /home/shalin/Документы/Dev/python-project-83/database.sql