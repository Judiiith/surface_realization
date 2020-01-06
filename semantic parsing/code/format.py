# -*- coding: utf-8 -*- #
import sys
import argparse
import re
import os
import random
from collections import defaultdict

def get_args():
    parser = argparse.ArgumentParser(description = "Mondat elemzes")
    parser.add_argument("file", type = str, help = "file path")
    parser.add_argument("penn_file", type = str, help = "file path")
    return parser.parse_args()

def change(t_file, penn_file):
    sentences = 0
    datas = []
    datas_sentence = []
    with open(t_file, "r", encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if line == "\n":
                sentences += 1
                datas_sentence.append(datas)
                datas=[]
            if line.startswith("#"):
                continue
            if line!="\n":
                fields = line.split("\t")
                word = fields[1]
        
                datas.append(word+' ')

    datas_irtg = []
    datas_irtg_sentence = []
    with open(penn_file, "r", encoding='utf-8') as h:
        lines = h.readlines()
        for line in lines:
            if line == "\n":
                datas_irtg_sentence.append(datas_irtg)
                datas_irtg=[]
            if line.startswith("#"):
                continue
            if line!="\n":
                fields = line.split("\t")
                lemma = fields[1]
        
                datas_irtg.append(lemma+' ')

    with open('gold_sentence', "w", encoding='utf-8') as g:
        for i in range(0, len(datas_sentence)):
            for j in range(0, len(datas_sentence[i])):
                g.write(str(datas_sentence[i][j]))
            g.write('\n')
            g.write('\n')
    
    with open('irtg_sentence', "w", encoding='utf-8') as k:
        for j in range(0, len(datas_irtg_sentence)):
            for h in range(0, len(datas_irtg_sentence[j])):
                k.write(str(datas_irtg_sentence[j][h]))
            k.write('\n')
            k.write('\n')

def main():
    args = get_args()
    change(args.file, args.penn_file)

if __name__ == "__main__":
    main()