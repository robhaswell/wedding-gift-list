#!/usr/bin/env python3
"""
Generate carousel HTML.
"""
import os.path

import oyaml as yaml


def main():
    """
    Main program.
    """
    with open("carousel.yaml") as fp:
        piclist = yaml.load(fp)

        print(piclist)


if __name__ == "__main__":
    main()
