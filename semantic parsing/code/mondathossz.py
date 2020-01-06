# -*- coding: utf-8 -*- #
import sys
import argparse
import re
import os
import random
from collections import defaultdict

def get_args():
    parser = argparse.ArgumentParser(description = "Mondat elemzes")
    parser.add_argument("result_file", type = str, help = "file path")
    return parser.parse_args()

def hossz(result_file):
    sentence = []

    with open(result_file, "r", encoding='utf-8') as f:
        lines = f.readlines()
        for i in range(0, len(lines)):
            if lines[i] == '\n':
                continue
            if lines[i] != '\n':
                fields = lines[i].split(' ')
                if (len(fields) <= 14):
                    sentence.append(lines[i])

    
    sentence_real = []
    for i in range(0, len(sentence)-2):
        #if ((re.match('[0-9]{1,3}. mondat', sentence[i]) is not None)):
        #    continue
        if ((re.match('[0-9]{1,3}. mondat', sentence[i]) is not None) and (re.match('[0-9]{1,3}. mondat', sentence[i+1]) is not None)):
            #sentence_real.append(sentence[i])
            continue
        elif ((re.match('[0-9]{1,3}. mondat', sentence[i]) is not None) and (re.match('[0-9]{1,3}. mondat', sentence[i+1]) is None)):
            sentence_real.append(sentence[i])
            sentence_real.append(sentence[i+1] + '\n')

    with open('mondat_14_hosszu', "w", encoding='utf-8') as g:
        for i in range (0, len(sentence_real)):
            g.write(sentence_real[i])


def main():
    args = get_args()
    hossz(args.result_file)

if __name__ == "__main__":
    main()