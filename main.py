# main.py
from flask import Flask, send_from_directory, abort
import os
import webbrowser
from threading import Timer
import pathlib

app = Flask(__name__)

# 获取当前工作目录
current_dir = pathlib.Path.cwd()

@app.route('/')
def serve_root():
    """处理根路径请求"""
    return serve_file('YJ.html')  # 改为YJ.html

@app.route('/<path:filename>')
def serve_file(filename):
    """提供当前目录下的文件服务"""
    # 确保请求的文件在当前工作目录内
    try:
        requested_path = current_dir / filename
        # 防止目录遍历攻击 - 允许子目录访问
        if not str(requested_path.resolve()).startswith(str(current_dir.resolve())):
            abort(403, description="访问被拒绝")

        # 检查文件是否存在
        if not requested_path.exists():
            abort(404, description="文件未找到")

        # 发送文件
        return send_from_directory(current_dir, filename)

    except Exception as e:
        abort(500, description=f"服务器错误: {str(e)}")

def open_browser():
    """在默认浏览器中打开应用"""
    webbrowser.open_new('http://localhost:8001/')

if __name__ == '__main__':
    # 启动前检查YJ.html是否存在
    index_path = current_dir / 'YJ.html'  # 改为YJ.html
    if not index_path.exists():
        print("警告: YJ.html 文件不存在!")
        print("请在同级目录创建 YJ.html 文件")

    # 延迟1秒后打开浏览器
    Timer(1, open_browser).start()

    # 启动Flask应用
    print("服务已启动：http://localhost:8001/")
    print("服务目录:", current_dir.resolve())
    app.run(host='0.0.0.0', port=8001, debug=True)