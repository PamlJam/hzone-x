from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer

consumer_object_list = []
# 用户列表
class ChatConsumer(WebsocketConsumer):
# 监听事件 自动触发
    def websocket_connect(self, message):
    # 请求连接
        self.accept()
        # 建立链接
        consumer_object_list.append(self)
        # 添加用户

    def websocket_receive(self, message):
    # 发起消息
        text = message.get('text')
        # 回复消息
        for consumer_object in consumer_object_list:
            consumer_object.send(text_data=text)
            # 群发消息
            
    def websocket_disconnect(self, message):
    # 断开连接
        consumer_object_list.remove(self)
        # 移除用户
        raise StopConsumer()
        # 抛出异常