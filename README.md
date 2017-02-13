# Muse Jobs
Download and count jobs from The Muse's Jobs Api

## Usage
sort a directory:

    python muse_jobs download --pages 10 # download 10 pages of jobs from the muse api
    python muse_jobs count "New York City Metro Area" # Counts jobs in NYC

Get help:

    python muse -h

If you'd like to query the database for the jobs count using raw sql:

    sqlite3 jobs.db "SELECT count(name) FROM jobs WHERE id IN (SELECT job_id from jobs_locations where location_name='New York City Metro Area');"

## Installation

From the root directory:

    pip install -e .

## Run Tests

    pytest

## Dependencies

Runtime:
* python 3
* requests
* sqlite3

Test:
* pytest

## Notes and improvements
Database inserts are running super slow. This is likely because I'm inserting
one row and a time and opening and closing a connection for each payload. With more time
I would batch these writes.
There is some data that I am not storing because we are not using it for the counting
or filtering by location. If we planned to go further with this dataset I would
make the effort to store it.
Write more automated tests. I wrote one end to end test to check the core functionality.


## Roadmap
#### Should do
[X] Dump api results into a local database
[X] CLI
[X] Write SQL query

#### Could do
[ ] Add the ability to start from a page that isn't the first page
[ ] Parallel Downloads

