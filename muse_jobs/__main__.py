import argparse
from pprint import pprint

from muse_jobs.db import DB
from muse_jobs.download_muse_jobs import download_muse_jobs


DOWNLOAD = 'download'
COUNT = "count"

def main():
    parser = argparse.ArgumentParser(
        description='Download jobs from a the muse'
    )
    subparsers = parser.add_subparsers(dest='action')
    dl_parser = subparsers.add_parser(DOWNLOAD, help="Download jobs from the muse jobs page")
    dl_parser.add_argument('--pages',
                        type=int,
                        default=None,
                        help='The number of pages to download from the muse jobs page')

    count_parser = subparsers.add_parser(COUNT, help="Count jobs in a given region")
    count_parser.add_argument("region", help="The region to count jobs in")

    args = parser.parse_args()

    if args.action == DOWNLOAD:
        db = DB()
        db.reset()
        for job in download_muse_jobs(args.pages):
            db.add_job(job)

    if args.action == COUNT:
        db = DB()
        try:
            print(db.count_in_region(args.region))
        except Exception:
            print("Error: Jobs not downloaded, please call `download` first.")



if __name__ == '__main__':
    main()
