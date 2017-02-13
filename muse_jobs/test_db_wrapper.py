import json

import pytest

from muse_jobs.db import DB

TEST_DB_PATH = 'test.db'


@pytest.fixture
def db():
    db = DB(TEST_DB_PATH)
    db.reset()
    return db


@pytest.fixture
def jobs():
    with open('muse_jobs/example_job.json') as data_file:
        return json.load(data_file)


def test_count_in_ny(db, jobs):
    for job in jobs:
        db.add_job(job)

    EXPECTED_JOBS_IN_NYC = 3
    LOCATION = "New York City Metro Area"

    assert db.count_in_region(LOCATION) == EXPECTED_JOBS_IN_NYC
