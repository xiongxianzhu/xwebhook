"""
利用码云的webhook功能实现用户push代码后， 在vps上git pull代码到指定目录下

码云webhook推送数据格式说明: https://gitee.com/help/articles/4186
"""
import os
from flask import Flask, request, Blueprint
# import simplejson
from xwebhook.utils import json_success, json_error


app = Flask(__name__)
webhook = Blueprint('webhook', __name__, url_prefix='/webhook')

GIT_PATH = os.getenv('git_path', '/home/www/html')
WEBHOOK_PASSWORD = os.getenv('webhook_password', 'yourwebhookpassword')
DEBUG = True if os.getenv('FLASK_ENV', 'development') == 'production' else False


@webhook.route('/gitee/', methods=['GET', 'POST'])
def webhook_gitee():
    """ gitee webhook """
    if not request.json:
        return json_error(msg='请求参数不能为空')

    password = request.json.get('password', None)
    if WEBHOOK_PASSWORD == password:
        os.chdir(GIT_PATH)
        os.system("git pull")
        return json_success('git pull完成')
    else:
        return json_error(msg='密码不正确')

app.register_blueprint(webhook)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=DEBUG, threaded=True)
    