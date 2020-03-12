#字典转json格式
import json
k = {
    "a": 1,
    "b": 12.33,
    "c": True,
    "d": False,
    "f": None,
    "g": (1,2,3,4),
    "k": [1,2,3,4],
    "avc": {
        "ad": "1111",
        "cd": "2323"
    }
}

d_json = json.dumps(k)
print(d_json)
print(type(d_json))