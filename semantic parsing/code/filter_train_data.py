# -*- coding: utf-8 -*- #
import sys
import argparse
import re
import os
import random
from collections import defaultdict

def get_args():
    parser = argparse.ArgumentParser(description = "Mondat elemzes")
    parser.add_argument("train_file_name", type = str, help = "file path")
    parser.add_argument("pos_first", type = str, help = "Elso postag")
    parser.add_argument("pos_second", type = str, help = "Masodik postag")
    parser.add_argument("edge", type = str, help="edge name")
    parser.add_argument("output", type = str, help=" output")
    return parser.parse_args()
    

def get_posttags(train_file, pos_first, pos_second, edge, output):
    sentences = 0
    datas = []
    sentence = []

    with open(train_file, "r", encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if line == "\n":
                sentences += 1
                datas.append(sentence)
                sentence = []
            if line.startswith("#"):
                continue
            if line!="\n":
                fields = line.split("\t")
                word_id = fields[0]
                lemma = fields[1]
                word = fields[2]
                tree_pos = fields[3]
                ud_pos = fields[4]
                mor = fields[5]
                head = fields[6]
                ud_edge = fields[7]
                comp_edge = fields[8]
                space_after = fields[9]

                data = {'word_id': word_id,'lemma': lemma,  'word': word, 'tree_pos' : tree_pos, 'ud_pos' : ud_pos, 'mor': mor, 'head': head, 'ud_edge': ud_edge, 'comp_edge':comp_edge, 'space_after': space_after}
                sentence.append(data)

    for i in range(0, len(datas)):
        for j in range(0, len(datas[i])):
            for k in range (0, len(datas[i])):
                if ((datas[i][j]['head'] == datas[i][k]['word_id']) and (datas[i][j]['ud_edge'] == edge)): # and (datas[i][j]['word_id']< datas[i][k]['word_id'])
                    datas[i][j]['head'] = datas[i][k]['tree_pos']
                    datas[i][j]['mor'] = datas[i][k]['lemma']

    number = 0
    for i in range(0, len(datas)):
            for j in range(0, len(datas[i])):
                if ((datas[i][j]['tree_pos'] == (pos_first.upper())) and (datas[i][j]['head'] == (pos_second.upper()))):
                    number = number+1


    with open(output,  "w", encoding='utf-8') as g:
        g.write('Sum:' + str(number) + '\n\n')
        for i in range(0, len(datas)):
            for j in range(0, len(datas[i])):
                if ((datas[i][j]['tree_pos'] == (pos_first.upper())) and (datas[i][j]['head'] == (pos_second.upper()))):
                    g.write(str(i+1)+' ' +datas[i][j]['lemma']+ ' ' + datas[i][j]['tree_pos']+ ' '+ datas[i][j]['mor'] + ' ' + datas[i][j]['head']  + ' ' + datas[i][j]['ud_edge'] + '\n')


def main():
    args = get_args()
    get_posttags(args.train_file_name, args.pos_first, args.pos_second, args.edge, args.output)

if __name__ == "__main__":
    main()