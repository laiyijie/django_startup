# django 脚手架

## 特性

1. 部署docker支持
2. log配置，区分 access_log
3. 请求数据转换中间件，数据会被转换到 request.data 中， 非常适合接受json数据
4. 基本用户系统，简单登录，密码是明文，请自行修改



## 使用方式

### 开发

    export CONSOLE_LOG_ONLY=1
    python3 manage.py migrate 
    python3 manage.py runserver 

### 部署
    
#### 默认部署

    ./script/start_docker.sh

内部采用uwsgi。base docker 来自于 [laiyijie/ubuntu_dev](https://cloud.docker.com/u/laiyijie/repository/docker/laiyijie/ubuntu_dev)
[github](https://github.com/laiyijie/ubuntu_server)

访问  http://127.0.0.1:8888

#### 手工打包

    docker build . -f Dockerfiles/Dockerfile --tag your_image_name
    
    
