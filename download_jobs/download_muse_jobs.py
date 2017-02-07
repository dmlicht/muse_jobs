from typing import Mapping

import requests

MUSE_JOBS_URL = "https://api-v2.themuse.com/jobs"
PAGE_COUNT_KEY = 'page_count'


def download_muse_jobs(n_pages_requested=None):
    """ Return Job descriptions from The Muse for n_pages_requested """
    n_pages_possible = _find_n_pages()

    n_pages = n_pages_requested
    if n_pages_requested is None:
        n_pages = n_pages_possible
    elif n_pages_requested > n_pages_possible:
        raise Exception("User asked for too many pages")  # TODO: make a better error

    for page_number in range(n_pages):  # TODO: should be possible to make these parallel
        response_json = _get_page(page_number)
        jobs = response_json['results']
        for job in jobs:
            yield job


def _find_n_pages() -> int:
    """ Ask the server for the total number of pages """
    result = _get_page(1)
    return result[PAGE_COUNT_KEY]


def _get_page(page_number: int) -> Mapping:
    """ Downloads a jobs page with the given page number and returns the json result """
    get_params = {
        'page': page_number
    }
    response = requests.get(MUSE_JOBS_URL, params=get_params)
    # TODO: should we do some kind of check?
    return response.json()
