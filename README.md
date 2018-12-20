# xwebhook

webhook(歪脖钩子)python版， 基于python3.6.7实现webhook脚本自动部署脚本。

#### 采用架构

```
python3.6.7+flask1.0.2
```

#### 将配置信息放在.env文件

从`.env_template`拷贝并重命名为`.env`， 将配置信息放在.env文件， 更改为您的`git_path`和`webhook_token`。

其中：

- `git_path`: 你要git pull的仓库在VPS上的路径
- `webhook_token`: 接头暗号(密码/安全令牌)， 明文

```
cp .env_template .env
```

#### 用法

```
$ pip3.6 install pipenv
$ cd xwebhook
$ pipenv install
$ pipenv shell
(xwebhook)$ python app.py &
# or
(xwebhook)$ flask run -h 0.0.0.0 &
```

#### 在仓库中添加webhook

for `gitee`:

- webhook url: http://host:[port]/webhook/gitee/
- password: 自定义安全令牌

for `gitlab`:

- webhook url: http://host:[port]/webhook/gitlab/
- token: 自定义安全令牌

