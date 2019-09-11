# -*- coding: utf-8 -*-
# @Time    : 2019/4/29 22:53
# @Author  : Weiyang
# @File    : main.py

import re
from py2neo import Graph

regx = re.compile('<->') # 用于切分字段
graph = Graph('http://localhost:7474',username='neo4j',password='1990121')
with open('./data/disease_cause_entity_label.txt','r',encoding='utf-8') as fi:
    count = 0
    for line in fi:
        result = regx.split(line.strip())
        # 过滤出 无效的数据
        if result[0] == result[3] or result[3] == result[4]:
            continue
        # 给节点 和 关系 添加唯一约束
        if count == 0:
            # 节点
            statement = 'create constraint on (p:疾病) assert p.name is unique'
            graph.evaluate(statement)
            statement = 'create constraint on (p:具体病因) assert p.name is unique'
            graph.evaluate(statement)
            statement = 'create constraint on (p:病因类别) assert p.name is unique'
            graph.evaluate(statement)

            # 关系
            statement = 'create constraint on (r:病因) assert r.name is unique'
            graph.evaluate(statement)
            statement = 'create constraint on (r:属于) assert r.name is unique'
            graph.evaluate(statement)
            count += 1
            continue

        # 查找节点是否存在
        statement = 'match(p:疾病) where p.name="%s" return p' % result[0]  # match 后必须有return语句
        temp = graph.evaluate(statement)
        if temp == None:
            # 如果不存在该节点，则创建节点
            statement = 'create (p:疾病{name:"%s"}) return p' % (result[0])
            graph.evaluate(statement)

        statement = 'match(p:具体病因) where p.name="%s" return p' % result[3]
        temp = graph.evaluate(statement)
        if temp == None:
            # 如果不存在该节点，则创建节点
            statement = 'create (p:具体病因{name:"%s"}) return p' % (result[3])
            graph.evaluate(statement)

        statement = 'match(p:病因类别) where p.name="%s" return p' % result[4]
        temp = graph.evaluate(statement)
        if temp == None:
            # 如果不存在该节点，则创建节点
            statement = 'create (p:病因类别{name:"%s"}) return p' % (result[4])
            graph.evaluate(statement)

        # 查找关系是否存在
        statement = 'match(p:疾病)-[r:病因]->(q:具体病因) where p.name="%s" and q.name="%s" return r' % (result[0], result[3])
        temp = graph.evaluate(statement)
        print(temp, result[0], result[4])
        if temp == None:
            # 如果不存在该节点，则创建节点
            statement = 'match (p:疾病),(g:具体病因) where p.name= "%s" and g.name="%s" create (p)-[r:病因]->(g) ' % \
                (result[0], result[3])
            graph.evaluate(statement)

        statement = 'match(p:具体病因)-[r:属于]->(q:病因类别) where p.name="%s" and q.name="%s" return r' % (result[3], result[4])
        temp = graph.evaluate(statement)
        print(temp, result[3], result[4])
        if temp == None:
            # 如果不存在该节点，则创建节点
            statement = 'match (p:具体病因),(g:病因类别) where p.name= "%s" and g.name="%s" create (p)-[r:属于]->(g) ' % \
                (result[3], result[4])
            graph.evaluate(statement)
        count += 1