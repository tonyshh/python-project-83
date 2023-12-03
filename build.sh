# Install dependencies
make install

# Apply database migrations
psql -a -d $DATABASE_URL -f database.sql