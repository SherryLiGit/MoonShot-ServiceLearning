from flask import Flask,request
from postblog import post_to_wordpress
import json

app = Flask(__name__)

@app.route('/')
def index():
    return {
        "msg": "success",
        "data": "welcome to use flask."
    }

@app.route("/postRequirement", methods=["POST"])
def post_requirement():
    #默认返回内容
    return_dict = {'return_code':'201','return_info':'处理成功','result':None}

    # 判断传入的json数据是否为空
    data = request.get_data()
    if len(data) == 0:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    
    # 对参数进行操作
    name = request.get_json()['ActivityName']
    content = request.get_json()['Introduction']
    print(name, content)

    post_to_wordpress(name, content)

    # 返回Post处理结果
    return json.dumps(return_dict,ensure_ascii=False)

app.run()

