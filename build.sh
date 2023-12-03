# Install dependencies
make install

# Apply database migrations
psql -a -d postgres://tonysh:aWq4BI4O1ZGeGZuUa0MTFPwe4Hu431dt@dpg-clm45b9fb9qs7397b2cg-a.singapore-postgres.render.com/page_analyzer_mvmf -f database.sql