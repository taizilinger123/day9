import paramiko

transport = paramiko.Transport(('192.168.1.3', 22))
transport.connect(username='root', password='123456')

sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
#sftp.put('笔记', '/tmp/test_from_win')
# 将remove_path 下载到本地 local_path
sftp.get('/tmp/yum.log', 'fromlinux.txt')

transport.close()