<h1 align="center">Китос, привет ептвую мать 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>

### Перед запуском
```shell
docker-compose -f docker-compose.yml up -d
```

Перейдите по адресу: http://127.0.0.1:9001/buckets и создать ведро "tests", логин и пароль minioadmin

### Запустить app_Poller
```shell
export PYTHONPATH=$PWD
make run.poller
```

### Запустить app_Worcker
```shell
export PYTHONPATH=$PWD
make run.worker
```
Перейти по ссылке https://t.me/test_kts_bot к боту и отправить фото или документ, через некоторое время 
данные появятся в s3 хранилище
