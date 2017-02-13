rm jobs.db
sqlite3 jobs.db < db.schema

python add_to_db.py

echo "companies: "
sqlite3 jobs.db "SELECT * FROM companies;"

echo ""
echo "locations: "
sqlite3 jobs.db "SELECT * FROM locations;"

echo ""
echo "jobs: "
sqlite3 jobs.db "SELECT name FROM jobs;"

echo ""
echo "jobs in nyc metro area: "
sqlite3 jobs.db "SELECT count(name) FROM jobs WHERE id IN (SELECT job_id from jobs_locations where location_name='New York City Metro Area');"
sqlite3 jobs.db "SELECT name FROM jobs WHERE id IN (SELECT job_id from jobs_locations where location_name='New York City Metro Area');"
