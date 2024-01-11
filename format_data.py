

"""
There are several formats that the repo is built to handle. 

"""


import os
from argparse import ArgumentParser


if __name__ == "__main__":
    
    parser = ArgumentParser()
    parser.add_argument("--data_dir", type=str, default = None)

    args = parser.parse_args()

    if args.data_dir:
        print(os.listdir(args.data_dir))
    
    print("\nData formatted.")
