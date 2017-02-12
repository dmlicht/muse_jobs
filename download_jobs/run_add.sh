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
sqlite3 jobs.db "SELECT * FROM jobs;"