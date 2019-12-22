# -*- coding: utf-8 -*-

import word_tag
import question_demo


class Question2neo4j:
    def __init__(self, dict_paths):
        self.tw = word_tag.Tagger(dict_paths)
        self.rules = question_demo.rules

    def get_neo4j(self, question):
        word_object=self.tw.get_word_objects(question)
        # for i in word_object:
        #     print i.token, i.pos
        queries_dict = dict()

        for rule in self.rules:
            query, num = rule.apply(word_object)
            if query is not None:
                queries_dict[num] = query



        if len(queries_dict) == 0:
            return None
        elif len(queries_dict) == 1:
            return queries_dict.values()[0]
        else:
            # 匹配多个语句，以匹配关键词最多的句子作为返回结果
            sorted_dict = sorted(queries_dict.iteritems(), key=lambda item: item[0], reverse=True)
            return sorted_dict[0][1]