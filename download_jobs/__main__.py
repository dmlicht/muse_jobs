import argparse
from download_jobs.download_muse_jobs import download_muse_jobs


def main():
    parser = argparse.ArgumentParser(
        description='Download jobs from a the muse'
    )
    parser.add_argument('--pages',
                        type=int,
                        default=None,
                        help='The number of pages to download from the muse jobs page')

    args = parser.parse_args()
    for job in download_muse_jobs(args.pages):
        print(job)


if __name__ == '__main__':
    main()
