#!/home/martin/anaconda3/bin/python
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 14:34:47 2018

@author: martin
"""
import sys
import string

def make_word_list1():
    """Reads lines from a file and builds a list using append."""
    t = []
    fin = open(wordsFile)
    for line in fin:
        word = line.strip()
        t.append(word)
    return t

def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header
   
    returns: map from each word to the number of times it appears.
    """
    hist = {} # This is an empty dictionary
    fp = open(filename)

    if skip_header:
        skip_gutenberg_header(fp)

    for line in fp:
        process_line(line, hist)

    return hist

def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.
    
    RMK: You just have to look at the Gutenberg format. That is
    how you would know how to write such a function. This had to
    be changed.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*** START OF TH'):
            break

def process_line(line, hist):
    """Adds the words in the line to the histogram.

    Modifies hist.
    
    RMK: This is not *pure* function. It modifies
    one of its arguments. This is frowned upon
    in many circles, but it is one way to do things.

    line: string
    hist: histogram (map from word to frequency)
    """
    # replace hyphens with spaces before splitting
    line = line.replace('-', ' ')
    strippables = string.punctuation + string.whitespace

    for word in line.split():
        # remove punctuation and convert to lowercase
        word = word.strip(strippables)
        word = word.lower()

        # update the histogram
        hist[word] = hist.get(word, 0) + 1
    
def total_words(hist):
    """Returns the total of the frequencies in a histogram."""
    return sum(hist.values())

def different_words(hist):
    """Returns the number of different words in a histogram."""
    return len(hist)

def most_common(hist):
    """Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """
    t = []
    for key, value in hist.items():
        t.append((value, key))

    t.sort()
    t.reverse()
    return t


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.
    
    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    t = most_common(hist)
    print("There are {0:d} words in the word list".format(len(make_word_list1())))
    print("\n")
    print("There are {0:d} unique words used by Austen".format(different_words(hist)))
    print("\n")
    print('The most common words are:')
    for freq, word in t[:num]:
        print(word, '\t', freq)



# What to do when the file is being fun as a script.
if __name__ == '__main__':
    # Get name of exhaustive list file
    # from command line.
    wordsFile = sys.argv[1]
    # Get user input
    bookFile = input("What book would you like to analyze? ")
    hist = process_file(bookFile, skip_header=True)
    print_most_common(hist)










