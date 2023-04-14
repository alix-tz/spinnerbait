"""
This script insures that we have correctly formed pairs of TXT and PNG files
to feed Kraken for training a recognizer. 
"""

import os
import sys

    

data_dir = "./data/"

txt_files = [f for f in os.listdir(data_dir) if f.endswith('.txt')]
png_files = [f for f in os.listdir(data_dir) if f.endswith('.png')]
txt_files_with_png = [f for f in txt_files if f.replace('.txt', '.png') in png_files or f.replace('.gt.txt', '.png') in png_files]
png_files_with_txt = [f for f in png_files if f.replace('.png', '.txt') in txt_files or f.replace('.png', '.gt.txt') in txt_files]

files_with_both = list(set(txt_files_with_png + png_files_with_txt))
print("Identifying paired elements - DONE")

# count how many files are not paired
unpaired = 0
for f in txt_files:
    if f not in files_with_both:
        unpaired += 1

# Get the user's approval before continuing
print("WARNING - This script will remove {} file(s) from the 'data/' directory.".format(unpaired))
approval = input("Are you sure you want to continue? [y/n]")

if not approval in ["y", "yes"]:
    print("Ok, let's stop here then.")
    sys.exit()

removed = 0
for f in txt_files:
    if f not in files_with_both:
        os.remove(os.path.join(data_dir, f))
        removed += 1
print("Removing unpaired elements - DONE")

# now let's rename all the remaining txt files such as 0000.txt becomes 0000.gt.txt
for f in txt_files:
    if f in files_with_both:
        if f.endswith('.gt.txt'):
            continue
        else:
            os.rename(f, f.replace('.txt', '.gt.txt'))
print("Renaming .txt files to .gt.txt when necessary - DONE")