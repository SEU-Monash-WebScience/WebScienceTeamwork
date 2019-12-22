# -*- coding: utf-8 -*-
from refo import finditer, Predicate, Star, Any, Disjunction
import re


class W(Predicate):
    def __init__(self, token=".*", pos=".*"):
        self.token = re.compile(token + "$")
        self.pos = re.compile(pos + "$")
        super(W, self).__init__(self.match)

    def match(self, word):
        m1 = self.token.match(word.token)
        m2 = self.pos.match(word.pos)
        return m1 and m2



class Rule(object):
    def __init__(self,condition_num, condition=None, action=None):
        assert condition and action
        self.condition_num = condition_num
        self.condition = condition
        self.action = action



    def apply(self, sentence):
        matches = []
        for m in finditer(self.condition, sentence):
            i, j = m.span()
            matches.extend(sentence[i:j])
        if len(matches)==0:
            return None, None
        else:
            for i in matches:
                print i.token, i.pos
            return self.action(matches), self.condition_num


class QuestionSet:
    def __init__(self):
        pass

    def what_is_question(self, word_object):
        """
        name的property是多少

        cont: na + 的 + n

        :param word_object:
        :return:
        """
        return ["Q1"]

    def class_question(self, word_object):
        """
        name的class是什么

        cont: na + 的 + cls

        :param word_object:
        :return:
        """
        return ["Q2"]

    def na_na_pro_question(self,word_object):
        """
        name的name的property
        cont: na + 的 + na + 的 + n
        :param word_object:
        :return:
        """
        return ['Q3']

pos_name = "na"
pos_property = "ppt"
pos_number = "m"

# weapon_entity = (W(pos=pos_weapon))
name_entity = (W(pos=pos_name))
property_entity=(W(pos=pos_property))
number_entity = (W(pos=pos_number))






rules = [
    Rule(condition_num=2, condition=name_entity+W('的')+W(pos='n')+Star(Any(), greedy=False), action=QuestionSet().what_is_question),
    Rule(condition_num=2, condition=name_entity+W('的')+W(pos='cls')+Star(Any(), greedy=False), action=QuestionSet().class_question),
    Rule(condition_num=3, condition=name_entity+W('的')+name_entity+W('的')+W(pos='n')+Star(Any(), greedy=False), action=QuestionSet().na_na_pro_question)
]