c.NotebookApp.allow_remote_access = True
#允许远程访问

c.NotebookApp.ip='*'
#似乎'*'或者'0.0.0.0'效果一样

# c.NotebookApp.password = u'sha1:a9079......'
#这里是刚才的哈希密码（可用右键粘贴）

c.NotebookApp.open_browser = False
#不打开浏览器

c.NotebookApp.port =8888
#随便指定一个端口   