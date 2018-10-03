#!/usr/bin/env python3
"""
Generate carousel HTML.
"""
import datetime
import html
import json
import os.path

import oyaml as yaml
from PIL import Image  # uses pillow


def main():
    """
    Main program.
    """
    with open("carousel.yaml") as fp:
        piclist = yaml.load(fp)

    altered = False
    first = True
    output = []
    for basename, entry in piclist.items():
        path = os.path.join("img", "house", basename + ".jpg")
        desc = entry['desc']
        try:
            date = entry['date']
        except (TypeError, KeyError):
            date = datetime.datetime.fromtimestamp(os.path.getmtime(path))
            entry = dict(
                desc=entry,
                date=date
            )
            piclist[basename] = entry
            altered = True

        im = Image.open(path)
        width, height = im.size

        output.append(dict(src=path, w=width, h=height, title=desc))

    print("var items = %s" % (json.dumps(output),))
    if altered:
        with open("carousel.yaml", "w") as fp:
            output = yaml.dump(piclist)
            fp.write(output)


if __name__ == "__main__":
    main()
