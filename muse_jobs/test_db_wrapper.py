import json

from muse_jobs.db import DB


def test_db():
    db = DB('test.db')
    db.reset()
    with open('example_job.json') as data_file:
        jobs = json.load(data_file)

    for job in jobs:
        db.add_job(job)

    EXPECTED_JOBS_IN_NYC = 3
    LOCATION = "New York City Metro Area"

    assert db.count_in_region(LOCATION) == EXPECTED_JOBS_IN_NYC

