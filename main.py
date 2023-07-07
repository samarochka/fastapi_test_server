from fastapi_test_server import run

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--port', default=1488, required=False)


if __name__ == '__main__':
    args = parser.parse_args()
    run(int(args.port))
