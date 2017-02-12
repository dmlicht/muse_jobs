import json
import sqlite3

DATABASE = 'jobs.db'

ADD_COMPANY_SQL = """
INSERT OR IGNORE INTO companies (id, name, short_name) VALUES (?, ?, ?)
"""

ADD_LOCATION_SQL = """
INSERT OR IGNORE INTO locations (name) VALUES  (?)"""

ADD_JOB_SQL = """
INSERT INTO jobs (id, contents, name, publication_date, short_name, model_type, company_id)
VALUES (?, ?, ?, ?, ?, ?, ?)"""


def main():
    with open('example_job.json') as data_file:
        jobs = json.load(data_file)

    for job in jobs:
        add_job(job)


def add_job(job):
    # TODO: Add other data
    # Set up db
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Add company
    company = job['company']
    cursor.execute(ADD_COMPANY_SQL, (company['id'], company['name'], company['short_name'],))

    # Add job
    cursor.execute(ADD_JOB_SQL, (job["id"], job["contents"], job["name"], job["publication_date"], job["short_name"], job["model_type"], company["id"],))


    # Add locations
    for location in job['locations']:
        cursor.execute(ADD_LOCATION_SQL, (location["name"],))

    # Commit db
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
