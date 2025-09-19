# excel_monitor.py
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pandas as pd

class ExcelHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        self.process(event)

    def on_modified(self, event):
        if event.is_directory:
            return
        self.process(event)

    def process(self, event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        
        # ✅ 过滤掉 Excel 临时文件：~$ 开头的文件
        if filename.startswith('~$'):
            return  # 什么也不做，直接忽略

        if filename.lower().endswith(('.xlsx', '.xls')):
            print(f"\n📁 检测到新文件: {filename}")
            try:
                df = pd.read_excel(filepath, nrows=5)
                print("📊 内容预览:")
                print(df.head().to_string(index=False))
            except Exception as e:
                print(f"❌ 读取失败: {e}")

def main():
    folder_to_watch = input("请输入要监控的文件夹路径（直接回车默认为当前目录）: ").strip()
    if not folder_to_watch:
        folder_to_watch = os.getcwd()
    
    if not os.path.exists(folder_to_watch):
        print("❌ 路径不存在！")
        return

    print(f"✅ 开始监控文件夹: {folder_to_watch}")
    print("💡 提示：将Excel文件放入此文件夹或修改现有文件会触发检测。\n")

    event_handler = ExcelHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_to_watch, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n🛑 监控已停止。")
    observer.join()

if __name__ == "__main__":
    main()