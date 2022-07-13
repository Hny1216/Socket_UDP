# UDP客户机程序
# 服务器IP:192.168.0.106
# 客户机IP:192.168.0.103
import time
import numpy as np
from socket import *
clientSocket = socket(AF_INET, SOCK_DGRAM)   # 创建客户机套接字
clientSocket.settimeout(1)  # 设置的最大等待时间
serverName = "192.168.0.106"       # 服务器主机
message = ["lxy","hny","python","test","deeplearning","net","face","love","hahaha","lalala"]    # 10个Ping报文
success = []      # 存放接收成功的Ping报文对应的时延
print("正在 Ping",serverName,"具有 51 字节的数据:")
for i in range(10):
    clientSocket.sendto(message[i].encode(), (serverName,6121))   # 发送Ping报文
    start = time.perf_counter()    # 计时开始
    try:
        modifiedMessage,serverAddress = clientSocket.recvfrom(2048)   # 等待接收响应Pong报文
        end = time.perf_counter()  # 计时结束
        print("来自 ", serverName, " 的回复：报文='", modifiedMessage.decode(),"', 字节=",len(message[i]), ", 时延RTT=", end - start, "s。", sep="")
        success.append(end-start)   # 将成功接收响应报文对应的时延保存
    except :
        print("[Error]:请求超时")
clientSocket.close()    # 关闭客户机套接字

## 打印 Ping 的统计信息
print("\n",serverName,"的 Ping 统计信息：\n    数据包：已发送=10 ,已接受=%d ,丢失=%d (%d%% 丢失)"%(len(success),10-len(success),100*(1-len(success)/10)))
if len(success)>0:
    print("往返行程的估计时间(以秒为单位):\n    最短=%6fs，最长=%6fs，平均=%7fs"%(min(success),max(success),np.mean(success)),sep="")

"""
遇到的问题和解决方案：
Q1:   报错：socket.gaierror: [Error 11001] getaddrinfo failed
原因分析：主机名出错，一开始使用了主机名，改用IP后正确
Q2:   报错：socket.timeout: timed out
原因分析：报错的原因是settimeout()函数是会直接报错而终止程序的运行的，
所以应该加上了try...except将异常抛出而不报错，不影响程序的正常运行
"""