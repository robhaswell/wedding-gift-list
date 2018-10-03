#!/usr/bin/env python3
"""
Generate carousel HTML.
"""
import datetime
import os.path

import oyaml as yaml


def main():
    """
    Main program.
    """
    with open("carousel.yaml") as fp:
        piclist = yaml.load(fp)

    altered = False
    for basename, entry in piclist.items():
        try:
            desc = entry['desc']
        except (TypeError, KeyError):
            path = os.path.join("img", "house", basename + ".jpg")
            mtime = datetime.datetime.fromtimestamp(os.path.getmtime(path))
            entry = dict(
                desc=entry,
                date=mtime
            )
            piclist[basename] = entry
            altered = True

    if altered:
        with open("carousel.yaml", "w") as fp:
            output = yaml.dump(piclist)
            fp.write(output)


if __name__ == "__main__":
    main()
