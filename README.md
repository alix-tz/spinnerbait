# Spinnerbaits

## Cleaning script

You can use `remove_unpaired_elements.py` before committin news pairs of GT. The script doesn't need any dependency and will 1) remove .txt files and .png files that don't have a corresponding image or text file, and 2) rename text files to follow kraken's expectations ("NNNN.gt.txt" instead of "NNNN.txt").

Simply run: 
`python3 remove_unpaired_elements.py`

The script will ask you for a confirmation before removing any files.