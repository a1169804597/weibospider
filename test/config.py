from kombu import Queue
from datetime import timedelta


BROKER_URL = 'redis://192.168.1.101/4' # 使用Redis作为消息代理

CELERY_RESULT_BACKEND = 'redis://192.168.1.101:6379/5' # 把任务结果存在了Redis

CELERY_TASK_SERIALIZER = 'msgpack' # 任务序列化和反序列化使用msgpack方案

CELERY_RESULT_SERIALIZER = 'json' # 读取任务结果一般性能要求不高，所以使用了可读性更好的JSON

CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24 # 任务过期时间

CELERY_ACCEPT_CONTENT = ['json', 'msgpack'] # 指定接受的内容类型


CELERY_QUEUES = (
    Queue('default', routing_key='task.#'),  # 路由键以“task.”开头的消息都进default队列

    Queue('web_tasks', routing_key='web.#'),  # 路由键以“web.”开头的消息都进web_tasks队列
)

CELERY_DEFAULT_EXCHANGE = 'tasks'  # 默认的交换机名字为tasks

CELERY_DEFAULT_EXCHANGE_TYPE = 'topic'  # 默认的交换类型是topic

CELERY_DEFAULT_ROUTING_KEY = 'task.default'  # 默认的路由键是task.default，这个路由键符合上面的default队列

CELERY_ROUTES = {

    'test.tasks.add': {  # tasks.add的消息会进入web_tasks队列
        'queue': 'web_tasks',
        'routing_key': 'web.add',

    }

}

# 使用beat进程自动生成任务
CELERYBEAT_SCHEDULE = {

    'add': {
        'task': 'test.tasks.print_datetime',
        'schedule': timedelta(seconds=10)

    }
}