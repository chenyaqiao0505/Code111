from flask import Flask#倒包
# from test1 import data
from flask import jsonify

app = Flask(__name__)#实例化一个Flask类型
app.debug=True


@app.route('/')
def hello():
    aa = {
        "message": "查询成功",
        "data": [{
            "id": 1,
            "name": "杂交稻"
        }, {
            "id": 2,
            "name": "小麦"
        }, {
            "id": 3,
            "name": "玉米"
        }, {
            "id": 4,
            "name": "大豆"
        }, {
            "id": 5,
            "name": "棉花"
        }],
        "code": 10000
    }
    return jsonify(aa)


if __name__ == '__main__':
    app.run()