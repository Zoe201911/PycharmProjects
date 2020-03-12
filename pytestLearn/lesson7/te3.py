#json转字典
#json格式的数据实际是一个字符串，需要用引号，字典是键值对的格式
import json
j = '''
{
    "a": 1,
    "b": 12.33,
    "c": true, 
    "d": false, 
    "f": null, 
    "g": [1, 2, 3, 4], 
    "k": [1, 2, 3, 4], 
    "avc": 
        {
            "ad": "1111", "cd": "2323"
        }
}'''

j_dict = json.loads(j)

print(j_dict)
print(type(j_dict))

print(j_dict["f"])
print(j_dict.get('d','eee'))
