<div align="center">
  <h1>Jsonly</h1>
</div>

![banner](https://github.com/VoidAsMad/jsonly/assets/103942316/e6bf681e-3eee-4150-99dc-dd9afacd00b2)

<div align="center">
  <h2>누구나 데이터베이스 활용을</h2>
</div>

[<img src="https://img.shields.io/badge/license-MIT-yellow.svg">](https://github.com/VoidAsMad/Jsonly/blob/main/LICENSE)<br>
[<img src="https://img.shields.io/badge/python-≥3.10-blue.svg">](https://www.python.org/)
[<img src="https://img.shields.io/pypi/v/jsonly.svg">](https://pypi.python.org/pypi/jsonly)

누구나 데이터베이스를 사용할 수 있어요!<br>

> **여러가지 데이터베이스를 쉽게 활용할 수 있어요!**<br>
> 지원 파일 : .json / .db<br>
> [자세한 사용법은 여기를 참조해주세요!](https://devksy.xyz/docs/jsonly)<br>

## Installation
```
$ pip install jsonly
```

## **Example**
### **DATA**

```json
# data.json (default)
{
  "기본": {
    "사과": "애플"
  },
  "하나": "일",
  "둘": "이"
}
```

### **GET**

데이터를 불러올 때 사용하는 메소드

```py
# get.py
from jsonly.client import UseJsonly

jsonly = UseJsonly(path="data.json")
print(jsonly.get(path="기본/사과"))
```

```
# result
>>> 애플
```

### **SET**

데이터를 덮어씌울 때 사용하는 메소드

```py
# set.py
from jsonly.client import UseJsonly

jsonly = UseJsonly(path="data.json")

data = {"기본중에" : "기본"}
print(jsonly.set(data=data))
```

```
# result
>>> True
```

```json
# data.json (modified from default)
{
    "기본중에": "기본"
}
```

### **UPDATE**

데이터를 루트 경로에 추가할 때 사용하는 메소드

```py
# update.py
from jsonly.client import UseJsonly

jsonly = UseJsonly(path="data.json")

data = {"새로운" : "데이터"}
print(jsonly.update(data=data))
```

```
# result
>>> True
```

```json
# data.json (modified from default)
{
    "기본": {
        "사과": "애플"
    },
    "하나": "일",
    "둘": "이",
    "새로운": "데이터"
}
```

### **INSERT**

데이터를 특정 경로에 추가할 때 사용하는 메소드

```py
# insert.py
from jsonly.client import UseJsonly

jsonly = UseJsonly(path="data.json")

data = {"데이터" : "삽입"}
print(jsonly.insert(data=data, path='기본'))
```

```
# result
>>> True
```

```json
# data.json (modified from default)
{
    "기본": {
        "데이터": "삽입"
    },
    "하나": "일",
    "둘": "이",
}
```
