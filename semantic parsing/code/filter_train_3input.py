# -*- coding: utf-8 -*- #
import sys
import argparse
import re
import os
import random
from collections import defaultdict

def get_args():
    parser = argparse.ArgumentParser(description = "Mondat elemzes")
    parser.add_argument("a_file", type = str, help = "file path")
    parser.add_argument("b_file", type = str, help = "file path")
    parser.add_argument("output", type = str, help = "file path")
    return parser.parse_args()

def change(a_file, b_file, output):
    datas_sentence = []
    with open(a_file, "r", encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if line == "\n":
                continue
            if line.startswith("#"):
                continue
            if line.startswith("Sum:"):
                continue
            if line!="\n":
                field = line.split(" ")
                sid = field[0]
                word1 = field[1]
                pos1 = field[2]
                word2 = field[3]
                pos2 = field[4]
                edge = field[5]

                data = {'sid': sid, 'word1' : word1, 'pos1' : pos1, 'word2': word2, 'pos2': pos2, 'edge': edge}        
                datas_sentence.append(data)

    datas_sentence2 = []
    with open(b_file, "r", encoding='utf-8') as g:
        lines2 = g.readlines()
        for line2 in lines2:
            if line2 == "\n":
                continue
            if line2.startswith("#"):
                continue
            if line2.startswith("Sum:"):
                continue
            if line2!="\n":
                fieldb = line2.split(" ")
                sidb = fieldb[0]
                word1b = fieldb[1]
                pos1b = fieldb[2]
                word2b = fieldb[3]
                pos2b = fieldb[4]
                edgeb = fieldb[5]

                datab2 = {'sid': sidb, 'word1' : word1b, 'pos1' : pos1b, 'word2': word2b, 'pos2': pos2b, 'edge': edgeb}        
                datas_sentence2.append(datab2)

        
        datas_compare= []
        for i in range(0, len(datas_sentence)):
            for j in range(0, len(datas_sentence2)):
                if ((datas_sentence[i]['sid'] == datas_sentence2[j]['sid']) and (datas_sentence[i]['word2'] == datas_sentence2[j]['word2'])) :
                    datas_compare.append(datas_sentence[i]['sid'])
                    datas_compare.append(' ')
                    datas_compare.append(datas_sentence[i]['word1'])
                    datas_compare.append(' ')
                    datas_compare.append(datas_sentence[i]['word2'])
                    datas_compare.append(' ')
                    datas_compare.append(datas_sentence2[j]['word1'])
                    datas_compare.append(' ')
                    datas_compare.append(datas_sentence2[j]['word2'])
                    datas_compare.append('\n')
                        

    
    with open(output, "w", encoding='utf-8') as z:
       for i in range(0, len(datas_compare)):
            for j in range(0, len(datas_compare[i])):
                #z.write ('Sum:', len(datas_compare))
                z.write(datas_compare[i][j])
           

def main():
    args = get_args()
    change(args.a_file, args.b_file, args.output)

if __name__ == "__main__":
    main()