# JSON:轻量级数据交换格式，易于人阅读和机器解析--->带有格式的字符串，主要用于数据交换
# Json对象：Python字典
# Json数组：Python列表内含多个字典
#使用场景：
#   1.数据交换：不同系统之间交换数据，如：前后端数据交换
#   2.数据存储：将数据存储为Json格式，如：配置文件
# Python内置Json库：
# json.dumps(): 将Python对象转换为Json字符串
# json.loads(): 将Json字符串转换为Python对象

import json

data = {
    "name": "张三",
    "age": 18,
    "sex":"男"
}
print(data)

s = json.dumps(data, indent=4, ensure_ascii=False)
print(s)

#反向转换：
json_str = '{"name":"周杰伦","age":38,"sex":"男"}'
print(json_str,type(json_str))
data = json.loads(json_str)
print(data,type(data))
