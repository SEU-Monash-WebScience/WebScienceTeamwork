# encoding=utf-8


import question2neo4j

if __name__ == '__main__':
    q2n = question2neo4j.Question2neo4j(['./external_dict/dict.txt'])
    while True:
        question = raw_input()
        my_query = q2n.get_neo4j(question.decode('utf-8'))
        if my_query is not None:
            print my_query
            # result = fuseki.get_sparql_result(my_query)
            # value = fuseki.get_sparql_result_value(result)
            #
            # # TODO 判断结果是否是布尔值，是布尔值则提问类型是"ASK"，回答“是”或者“不知道”。
            # if isinstance(value, bool):
            #     if value is True:
            #         print 'Yes'
            #     else:
            #         print 'I don\'t know. :('
            # else:
            #     # TODO 查询结果为空，根据OWA，回答“不知道”
            #     if len(value) == 0:
            #         print 'I don\'t know. :('
            #     elif len(value) == 1:
            #         print value[0]
            #     else:
            #         output = ''
            #         for v in value:
            #             output += v + u'、'
            #         print output[0:-1]

        else:
            # TODO 自然语言问题无法匹配到已有的正则模板上，回答“无法理解”
            print 'I can\'t understand. :('

        print '#' * 100