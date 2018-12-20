# webhook-python
python3.6.7实现webhook脚本自动部署脚本

#### 采用架构

```
python3.6.7+flask1.0.2
```

#### 将配置信息放在.env文件

将配置信息放在.env文件， 更改为您的`git_path`和`webhook_token`

```
cp .env_template .env
```

#### 用法

```
python app.py &
# or
flask run -h 0.0.0.0 &
```
