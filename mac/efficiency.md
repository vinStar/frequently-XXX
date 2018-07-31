## 一、ssh

### 1.1 auto ssh without password

three step  
[refer to](http://note.youdao.com/noteshare?id=9ec81dd49cf70f513cf9cdc1359031ac)

```
安装 ssh-copy-id 命令行工具 brew install ssh-copy-id
生成本机密钥/公钥文件 ssh-keygen -t rsa
将本机公钥上传到远程服务器上 ssh-copy-id -i ~/.ssh/id_rsa.pub remote-host
```

iTerm2->Prefreences->profiles->click "+" add a profile

command `ssh user@192.168.1.1`

then you can click "Profiles"-> choose your "name" 
