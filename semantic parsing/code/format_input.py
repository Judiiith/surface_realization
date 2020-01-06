# -*- coding: utf-8 -*- #
import sys
import argparse
import re
import os
import random
from collections import defaultdict

def get_args():
    parser = argparse.ArgumentParser(description = "Mondat elemzes")
    parser.add_argument("test_file_name", type = str, help = "file path")
    parser.add_argument("dev_file_name", type = str, help = "file path")
    return parser.parse_args()

def change_test(test_file):
    sentences = 0
    datas = []

    with open(test_file, "r", encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if line == "\n":
                sentences += 1
                datas.append('\n')
            #if line.startswith("# sent_id"):
            #    datas.append(line)
            #if line.startswith("# text"):
            #    datas.append(line)
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

                data = word_id + '\t'+ word + '\t' + lemma + '\t'+ tree_pos + '\t' + ud_pos + '\t' + mor + '\t' + head + '\t' + ud_edge+ '\t' +comp_edge+ '\t' +space_after
                datas.append(data)

    with open("changed_test_data", "w", encoding='utf-8') as g:
        for i in range(0, len(datas)):
            g.write(datas[i])
    

def change_dev(dev_file):
    sentences = 0
    datas = []
    sentence = []
    #sent_id = []
    #text_id = []

    with open(dev_file, "r", encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if line == "\n":
                sentences += 1
                datas.append(sentence)
                sentence = []
            #if line.startswith("# sent_id"):
            #    sent_id.append(line)
            #if line.startswith("# text"):
            #    text_id.append(line)
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
                if (datas[i][j]['head'] == datas[i][k]['word_id']):
                    datas[i][j]['head'] = datas[i][k]['word']
    
    for i in range(0, len(datas)):
        random.shuffle(datas[i]) 

    for i in range(0, len(datas)):
       for j in range(0, len(datas[i])):
            datas[i][j]['word_id'] = j+1
    
    for i in range(0, len(datas)):
        for j in range(0, len(datas[i])):
            for k in range(0, len(datas[i])):
                if (datas[i][j]['head']) == datas[i][k]['word']:
                    datas[i][j]['head'] = datas[i][k]['word_id']


    with open("changed_dev_data", "w", encoding='utf-8') as g:
        for i in range(0, len(datas)):
            #g.write(sent_id[i])
            #g.write(text_id[i])
            for j in range(0, len(datas[i])):
                g.write(str(datas[i][j]['word_id'])+ '\t' + str(datas[i][j]['word']) + '\t'+ '_'+'\t'+ str(datas[i][j]['tree_pos']) + '\t' + str(datas[i][j]['ud_pos'])+ '\t' + str(datas[i][j]['mor']) + '\t' + str(datas[i][j]['head']) + '\t' + str(datas[i][j]['ud_edge'])+ '\t' + str(datas[i][j]['comp_edge']) + '\t' + str(datas[i][j]['space_after']))
            g.write('\n')


def main():
    args = get_args()
    change_test(args.test_file_name)
    change_dev(args.dev_file_name)

if __name__ == "__main__":
    main()