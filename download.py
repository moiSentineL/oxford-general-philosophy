#!usr/bin/env python

from urllib.request import urlretrieve
import re
import sys
import argparse
import os

class GenPhilDownloader:
    def __init__(self, text, ext):
        self.text = text
        self.ext = ext

    def show_progress(self, block_num, block_size, total_size):
        progress= int(round(((block_num * block_size) / total_size) * 100, 2))
        print(f"{progress}% {"=" * (progress//4)}>{" " * (25-(progress//4))}|", end="\r")
        sys.stdout.flush()

    def mkdir(self, type):
        if os.path.exists(f"{type}"):
            self.reg(type)
        else:
            os.mkdir(f"{type}")
            self.reg(type)
        
    def reg(self, type):
        with open(self.text, 'r') as f:
            for l in f.readlines():
                match = re.search(r'(https?:\/\/[^\s]+)\s*;\s*(.*)', l)
                print(match.group(2).strip())
                urlretrieve(match.group(1), f"{type}/{match.group(2).strip()}.{self.ext}", self.show_progress)
                print("\ndone!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='gen-phil-2009',
                    description='This is where you can download the lectures, slides and handouts for offline use.',
                    epilog='Visit repo at https://github.com/moiSentineL/oxford-general-philosophy-2009')
    parser.add_argument('content', help="choose between lectures/slides")
    args = parser.parse_args()
    
    if args.content == "lectures":
        print("Downloading lectures...")
        GenPhilDownloader("lectures.txt", ".mp4").mkdir("lectures")
    elif args.content == "slides":
        print("Downloading lectures...")
        GenPhilDownloader("slides.txt", ".pdf").mkdir("slides")
    else:
        print("Please choose a correct option (lectures/slides)")
    # GenPhilDownloader("lectures.txt", ".mp4").mkdir("lectures")