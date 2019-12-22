# -*- coding: utf-8 -*-

import jieba
import jieba.posseg as pseg


sentence = '蛟龙600的机长是多少？'


class Word(object):
    def __init__(self, token, pos):
        self.token = token
        self.pos = pos
# p ='./external_dict/weapon.txt'

# jieba.load_userdict(p)
# for word, tag in pseg.cut(sentence):
#     print word, tag

class Tagger:
    def __init__(self, dict_paths):
        # TODO 加载外部词典
        for p in dict_paths:
            jieba.load_userdict(p)

    @staticmethod
    def get_word_objects(sentence):
        # type: (str) -> list
        """
        把自然语言转为Word对象
        :param sentence:
        :return:
        """
        return [Word(word.encode('utf-8'), tag) for word, tag in pseg.cut(sentence)]



# tw = Tagger(['./external_dict/weapon.txt'])
# word_object=tw.get_word_objects(sentence)
#
# for i in word_object:
#     print i.token, i.pos