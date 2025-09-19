# create_excel_template.py
import os
import pandas as pd

# 配置路径
NEW_IMAGES_DIR = "new_images"
OUTPUT_CSV = "products_input.csv"
OUTPUT_XLSX = "products_input.xlsx"

# 支持的图片格式（含大小写）
IMAGE_EXTS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff', '.svg', 
              '.JPG', '.JPEG', '.PNG', '.GIF', '.BMP', '.WEBP', '.TIFF', '.SVG'}

def main():
    if not os.path.exists(NEW_IMAGES_DIR):
        print(f"❌ 错误：未找到文件夹 {NEW_IMAGES_DIR}")
        return

    # 获取所有图片文件
    files = [f for f in os.listdir(NEW_IMAGES_DIR) 
             if os.path.splitext(f)[1] in IMAGE_EXTS]
    
    if not files:
        print(f"⚠️  {NEW_IMAGES_DIR} 中没有找到图片文件")
        return

    # 创建 DataFrame
    df = pd.DataFrame({
        'filename': sorted(files),
        'name': ['' for _ in files],
        'alt': ['' for _ in files],
        'description': ['' for _ in files]
    })

    # 保存为 CSV（UTF-8 with BOM，兼容 Excel）
    df.to_csv(OUTPUT_CSV, index=False, encoding='utf-8-sig')
    print(f"✅ 已生成 CSV 模板：{OUTPUT_CSV}")

    # 保存为 Excel
    try:
        df.to_excel(OUTPUT_XLSX, index=False, engine='openpyxl')
        print(f"✅ 已生成 Excel 模板：{OUTPUT_XLSX}")
    except ImportError:
        print("⚠️  未安装 openpyxl，请运行：pip install openpyxl")
        print(f"✅ 请先填写 {OUTPUT_CSV}，然后我会帮你读取")
    except Exception as e:
        print(f"❌ 生成 Excel 失败：{e}")

    # 显示文件列表
    print(f"📊 共 {len(files)} 个文件：")
    for f in files:
        print(f"   - {f}")

if __name__ == "__main__":
    main()