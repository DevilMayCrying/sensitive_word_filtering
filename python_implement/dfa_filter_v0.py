#!/usr/bin/python2.6
# -*- coding: utf-8 -*-
import time
import pandas as pd
df=pd.read_csv('/Users/ozintel/Downloads/网站敏感词检测/网站敏感词库/JasonYSU的敏感词库/敏感词库表统计.txt',
               delimiter='\t',encoding='gbk')
print(df['SENSITIVEWORDS'].tail(20))



class Node(object):
    def __init__(self):
        self.children = None


# The encode of word is UTF-8
def add_word(root, word):
    node = root
    for i in range(len(word)):
        if node.children == None:
            node.children = {}
            node.children[word[i]] = Node()

        elif word[i] not in node.children:
            node.children[word[i]] = Node()

        node = node.children[word[i]]


# def init(path):
#     root = Node()
#     fp = open(path, 'r')
#     for line in fp:
#         print('line', line)
#         line = line[0:-1]
#         # print len(line)
#         print ('line',line)
#         # print type(line)
#         add_word(root, line)
#     fp.close()
#     return root

def init(path=None):
    root=Node()
    for index,each in df.iterrows():
        add_word(root,each['SENSITIVEWORDS'])
    return root




# The encode of word is UTF-8
# The encode of message is UTF-8
def is_contain(message, root):
    for i in range(len(message)):
        p = root
        j = i
        while (j < len(message) and p.children != None and message[j] in p.children):
            p = p.children[message[j]]
            j = j + 1

        if p.children == None:
            # print '---word---',message[i:j]
            return True

    return False


def dfa():
    print('----------------dfa-----------')

    root = init('word.txt')

    message = '你是傻逼把，四处乱咬乱吠，吓得家中11岁的女儿躲在屋里不敢出来，直到辖区派出所民警赶到后，才将孩子从屋中救出。最后在征得主人同意后，民警和村民合力将这只发疯的狗打死'
    # message = '不顾'
    print('***message***', len(message))

    start_time = time.time()
    for i in range(1000):
        res = is_contain(message, root)
    print( 'res',res)
    end_time = time.time()
    print(end_time - start_time)


def is_contain2(message, word_list):
    for item in word_list:
        if message.find(item) != -1:
            return True
    return False


def normal():
    print('------------normal--------------')

    path = 'word.txt'
    fp = open(path, 'r')
    word_list = []
    message = '四处乱咬乱吠，吓得家中11岁的女儿躲在屋里不敢出来，直到辖区派出所民警赶到后，才将孩子从屋中救出。最后在征得主人同意后，民警和村民合力将这只发疯的狗打死'
    print('***message***', len(message))

    for line in fp:
        line = line[0:-1]
        word_list.append(line)
    fp.close()
    print('The count of word:', len(word_list))

    start_time = time.time()
    for i in range(1000):
        res = is_contain2(message, word_list)
    print('res',res)
    end_time = time.time()
    print(end_time - start_time)


if __name__ == '__main__':
    pass
    dfa()
    # normal()

