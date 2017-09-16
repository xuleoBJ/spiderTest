#coding=utf-8
import json

# Reading data back
with open('some.json', 'r') as fp:
    fp = fp.decode("gbk").encode("utf-8")
    data = json.loads(fp, encoding="utf-8")
