

Postgres Setup:

create scheme gsbtb
create user django PASSWORD 'iloveberlin';
GRANT ALL ON SCHEMA gsbtb TO django;
grant all on all tables in schema gsbtb to django;

Install Python module for Potsgres:

sudo apt-get install libpq-dev python-dev
pip install psycopg2


