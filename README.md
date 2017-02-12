# Download Jobs
Download jobs from The Muse's Jobs Api

## Usage
sort a directory:

    python muse download --pages 10 # download 10 pages of jobs from the muse api
    python muse show --location "New York City Metro Area"

Init database (From the root dir):

    cd download_jobs
    sqlite3 jobs.db < db.schema
    cd -

Run JSON to Database code on example jobs json:

    sh run_add_script.sh

Get help:

    python muse -h

## Installation

From the root directory:

    pip install -e .

## Run Tests

## Dependencies

Runtime:
* python 3
* requests

Test:
* pytest

## Roadmap
#### Should do
[ ] Dump api results into a local database
[ ] CLI
[ ] Write SQL query

#### Could do
[ ] Add the ability to start from a page that isn't the first page
[ ] Parallel Downloads

