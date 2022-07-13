# UDP服务器程序
# 服务器IP:192.168.0.106
# 客户机IP:192.168.0.103
import random
from socket import *
serverSocket = socket(AF_INET, SOCK_DGRAM)    # 创建服务器套接字
serverSocket.bind(('', 6121))                 # 绑定服务器套接字和端口号
print("服务器已启动......")
while True:
    rand = random.randint(0, 10)    # 生成随机数
    message, address = serverSocket.recvfrom(2048)    # 接收客户机的请求报文
    print("报文 '",message.decode(), "' 接收成功", sep="")
    if rand < 4:     # 以一定的概率模拟超时
        print()
        continue
    serverSocket.sendto(message.decode().upper().encode(), address)     # 发送响应报文
    print("报文 '", message.decode().upper(), "' 发送成功\n", sep="")      # 打印响应报文发送成功
