
from urllib import request, parse
# 负责处理json格式的模块
import json


baseurl = 'http://fanyi.baidu.com/sug'


# 存放用来模拟form的数据一定是dict格式
data = {
    # girl是翻译输入的英文内容，应该是由用户输入，此处使用硬编码
    'kw': 'girl'
}

# 需要使用parse模块对data进行编码
data = parse.urlencode(data).encode("utf-8")

print(type(data))
#  我们需要构造一个请求头，请求头部应该至少包含传入的数据的长度
# request要求传入的请求头是一个dict格式

headers = {
    # 因为使用post，至少应该包含content-length 字段
    'Content-Length':len(data)
}


# 有了headers，data，url，就可以尝试发出请求了
rsp = request.urlopen(baseurl, data=data)

json_data = rsp.read().decode('utf-8')
print(type(json_data))
print(json_data)


# 把json字符串转化成字典
json_data = json.loads(json_data)
print(type(json_data))
print(json_data)


for item in json_data['data']:
    print(item['k'], "--", item['v'])