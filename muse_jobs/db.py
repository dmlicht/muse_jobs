import json
import sqlite3
from typing import Dict
from subprocess import call

DEFAULT_DATABASE = 'jobs.db'

ADD_COMPANY_SQL = """
INSERT OR IGNORE INTO companies (id, name, short_name) VALUES (?, ?, ?)
"""

ADD_LOCATION_SQL = """
INSERT OR IGNORE INTO locations (name) VALUES  (?)"""

ADD_JOB_SQL = """
INSERT INTO jobs (id, contents, name, publication_date, short_name, model_type, company_id)
VALUES (?, ?, ?, ?, ?, ?, ?)"""

ADD_JOBS_LOCATIONS_SQL = """
INSERT INTO jobs_locations (job_id, location_name) VALUES (?, ?)
"""

COUNT_JOBS_IN_REGION_SQL = """
SELECT count(name) FROM jobs WHERE id IN
  (SELECT job_id from jobs_locations where location_name=?);
"""


def main():
    db = DB("example.db")
    db.reset()
    with open('example_job.json') as data_file:
        jobs = json.load(data_file)

    for job in jobs:
        db.add_job(job)

    print(db.count_in_region("New York City Metro Area"))


class DB:
    def __init__(self, db_path=DEFAULT_DATABASE):
        self._db_path = db_path

    def reset(self):
        call(["rm", self._db_path])

        conn = sqlite3.connect(self._db_path)
        cursor = conn.cursor()
        create_tables = open('db.schema', 'r').read()
        cursor.executescript(create_tables)
        conn.commit()
        conn.close()

    def add_job(self, job: Dict):
        # TODO: Add additional data that we are not using for count of jobs in NY
        # Set up db
        conn = sqlite3.connect(self._db_path)
        cursor = conn.cursor()

        # Add company
        company = job['company']
        cursor.execute(ADD_COMPANY_SQL, (company['id'], company['name'], company['short_name'],))

        # Add job
        cursor.execute(ADD_JOB_SQL, (
            job["id"], job["contents"], job["name"], job["publication_date"], job["short_name"], job["model_type"],
            company["id"],))

        # Add locations
        for location in job['locations']:
            # TODO: actual it seems redundant to store locations AND jobs_locations. cleanup when mvp built
            cursor.execute(ADD_LOCATION_SQL, (location["name"],))
            cursor.execute(ADD_JOBS_LOCATIONS_SQL, (job["id"], location["name"],))

        # Commit db
        conn.commit()
        conn.close()

    def count_in_region(self, region: str) -> int:
        conn = sqlite3.connect(self._db_path)
        cursor = conn.cursor()

        count = cursor.execute(COUNT_JOBS_IN_REGION_SQL, (region,)).fetchone()[0]
        conn.close()
        return count


if __name__ == '__main__':
    main()
