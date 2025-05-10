# Git & GitHub 实践学习笔记

## 📚 学习资料来源

* [廖雪峰 Git 教程](https://www.liaoxuefeng.com/wiki/896043488029600)
* GitHub 官方文档: [https://docs.github.com/](https://docs.github.com/)
* ChatGPT 指导
* B站相关教学视频

---

## 🧪 实践流程

1. 安装 Git，进行基本配置：

   ```bash
   git config --global user.name "用户名"
   git config --global user.email "邮箱"
   ```

2. 在本地创建项目文件夹，并初始化 Git：

   ```bash
   git init
   ```

3. 创建 Python 脚本 `main.py`，并分别完成下面 3 次修改和 commit：

   * 第一次提交：打印欢迎信息
   * 第二次提交：添加两个数的加法功能
   * 第三次提交：让用户输入两个数并显示结果

4. 把本地仓库连接到 GitHub 新建的公开仓库：

   ```bash
   git remote add origin https://github.com/用户名/仓库名.git
   ```

5. 三次分别提交后 push 到 GitHub：

   ```bash
   git push -u origin main
   ```

---

## 🛡️ 遇到的困难及解决方法

| 问题                                                  | 解决方法                            |
| --------------------------------------------------- | ------------------------------- |
| push 时提示权限错误                                        | 使用 GitHub PAT (个人访问令牌)，替代账号密码   |
| GitHub 只显示一次 commit                                 | 确保所有 commit 都在 main 分支，并分别 push |
| commit 混乱或重复                                        | 重新初始化仓库，删除多余分支或重新 clone         |
| `fatal: pathspec 'main.py' did not match any files` | 本目当前目录下无 main.py，需先 cd 进入项目文件夹  |

---

## 💡 学习心得

* Git 的版本控制很强大，很适合代码管理，但初学者需要练习掌握基本命令
* 每次 commit 都应写明确的描述，便于回顾和维护
* `git status` 和 `git log` 是非常有用的查看状态命令
* 经常 push 到 GitHub，可以防止本地数据丢失
* 遇到问题不要慌，分步骤排查并善用搜索、工具协助可以快速解决

---

本次实践完成后，我对 Git 的作用和 GitHub 同步过程有了更深圳的理解。下一步算法项目或实际使用中，我会继续使用这些技巧。
