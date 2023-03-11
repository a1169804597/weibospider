from celery import Celery


app = Celery('test', include=["test.tasks"])

app.config_from_object("test.config")


if __name__ == '__main__':
    app.start()
    # 1.启动worker任务
    # celery -A test.celeryApp worker -l info -P gevent
    # 2.同时启动worker任务和beat任务
    # celery -B -A test.celeryApp worker -l info -P gevent
