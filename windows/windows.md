## 一、命令

### 1.1 查看当前用户
`whoami`

### 1.2 查看当前所有登录用户
`query user`

### 1.3 查看系统所有用户
`net user`

### 1.4 打印系统变量
`echo %PATH%`

## 二、Net command

### 2.1 Net use
作用：连接计算机或断开计算机与共享资源的连接，或显示计算机的连接信息。 

`net use /` 显示命令帮助

- 不带参数 ， 显示计算机的连接信息。

- 建立计算机与共享资源的连接
`net use \\IP password /user:username` @用来表示域用户

`net use \\10.10.3.1 password /user:userName@domain`

- 建立连接后复制文件

xcopy 帮助命令`xcopy /?`

`xcopy /e /y /r /f ./folderName \\10.10.3.1\web\folderName\`

## 三、windows 端口占用

### 3.1 查看端口
`netstat -ano`  
`-a` 显示所有连接和侦听端口  
`-n` 数字形式显示地址和端口  
`-o` 显示进程 ID 添加    
`-b` 可能的情况下显示执行程序

### 3.2 查看进程
`tasklist`  执行程序、pid

`tasklist|findstr 1206` 查找包含1206的行

### 3.3 结束进程  
`taskkill /f /t /im Tencentdl.exe`
强制结束，以管理员身份启动 `cmd`  

## 四、任务管理器
这么多年白用了

菜单`查看-》选择列` 添加 pid CPU时间 等。。。

 


