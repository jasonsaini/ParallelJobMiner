import argparse
import os
import subprocess

# Gets job title
def get_job():
    parser = argparse.ArgumentParser(description='Job Search CLI')
    parser.add_argument('job_title', type=str, help='Job title to search for')
    args = parser.parse_args()

    return args.job_title

def run_file(version: str, job_title: str):
    print(f'{version} Version')
    print('-' * 75)
    print(f'Searching for {job_title} on various job sites...')

    # Run file
    result = subprocess.run(
        ['python3', f'{version}.py', job_title],
        env={'JOB_TITLE': job_title},
        capture_output=True, text=True
    )
    print(result.stdout)
    print(result.stderr)

    print('\n\n')


if __name__ == "__main__":
    job_title = get_job()

    run_file('concurrent', job_title)
    run_file('sequential', job_title)
