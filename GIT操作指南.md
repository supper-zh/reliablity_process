# Git操作指南

## 1. 基础配置

### 1.1 用户信息配置
```bash
# 设置用户名和邮箱
git config --global user.name "your_username"
git config --global user.email "your_email@example.com"
```

### 1.2 凭据存储配置
```bash
# 配置凭据存储，避免每次输入密码
git config --global credential.helper store
```

### 1.3 代理设置（如需要）
```bash
# 设置代理（如果在特殊网络环境下）
git config --global http.proxy http://proxy.server:port
git config --global https.proxy https://proxy.server:port

# 取消代理设置
git config --global --unset http.proxy
git config --global --unset https.proxy
```

## 2. 日常操作流程

### 2.1 初始化仓库
```bash
# 在项目目录中初始化Git仓库
git init

# 添加远程仓库地址
git remote add origin https://github.com/username/repository.git
```

### 2.2 添加和提交文件
```bash
# 添加所有文件到暂存区
git add .

# 提交更改
git commit -m "提交说明"
```

### 2.3 推送代码
```bash
# 首次推送并设置上游分支
git push -u origin master

# 后续推送
git push
```

## 3. 常见问题解决

### 3.1 网络连接问题
当遇到网络连接问题时，可以尝试以下方法：

1. 检查网络连接是否正常
2. 尝试取消代理设置：
   ```bash
   git config --global --unset http.proxy
   git config --global --unset https.proxy
   ```
3. 使用凭据存储避免重复认证：
   ```bash
   git config --global credential.helper store
   ```

### 3.2 SSH方式推送（推荐用于频繁操作）
1. 生成SSH密钥：
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```
2. 添加密钥到ssh-agent：
   ```bash
   ssh-agent bash
   ssh-add ~/.ssh/id_rsa
   ```
3. 将SSH密钥添加到GitHub账户
4. 修改远程仓库URL为SSH格式：
   ```bash
   git remote set-url origin git@github.com:username/repository.git
   ```

## 4. 实用命令

### 4.1 查看状态
```bash
# 查看仓库状态
git status

# 查看提交历史
git log --oneline
```

### 4.2 分支操作
```bash
# 查看所有分支
git branch -a

# 创建并切换到新分支
git checkout -b new_branch

# 切换分支
git checkout branch_name
```

### 4.3 撤销操作
```bash
# 撤销工作区修改
git checkout -- file_name

# 撤销暂存区修改
git reset HEAD file_name

# 撤销最后一次提交
git reset --soft HEAD~1
```