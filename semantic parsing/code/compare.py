# -*- coding: utf-8 -*- #
import sys
import argparse
import re
import os
import random
from collections import defaultdict

def get_args():
    parser = argparse.ArgumentParser(description = "Mondat elemzes")
    parser.add_argument("gold_file", type = str, help = "gold file path")
    #parser.add_argument("irtg_file", type = str, help = "irtg file path")
    return parser.parse_args()

def compare(gold_file):
    gold_sentences = []
    irtg_sentences = []

    with open(gold_file, "r", encoding='utf-8') as g:
        lines = g.readlines()
        for line in lines:
            if line !='\n' :
                gold_sentences.append(line)

 ###   with open(irtg_file, "r", encoding='utf-8') as f:
  #      lines = f.readlines()
  #      for line in lines:
  #          if line!='\n':
  #              irtg_sentences.append(line)

    with open('compare_result', "w", encoding = 'utf-8') as l:
        for i in range (0, len(gold_sentences)):
            l.write( str(i) + '. mondat: ' + '\n')
            l.write(gold_sentences[i])
            #l.write(irtg_sentences[i])
            l.write("\n")

def main():
    args = get_args()
    compare(args.gold_file)

if __name__ == "__main__":
    main()