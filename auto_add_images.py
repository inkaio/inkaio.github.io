# auto_add_images.py
import os
import shutil
from PIL import Image
import yaml

# 配置路径
NEW_IMAGES_DIR = "new_images"      # 拖图进来
IMAGES_DIR = "images"             # 正式图片存放
DATA_FILE = "_data/products_zh.yml"  # 数据文件（注意是下划线）
EXCEL_FILE = "products_input.xlsx"   # Excel 输入文件（可选）
PREVIEW_FILE = "preview_products.html"  # 预览页面
START_INDEX = 1

def load_from_excel():
    """从 Excel 读取产品信息（如果有）"""
    try:
        import pandas as pd
        if os.path.exists(EXCEL_FILE):
            df = pd.read_excel(EXCEL_FILE, engine='openpyxl')
            return df.set_index('filename').to_dict('index')
        else:
            print(f"⚠️ 未找到 {EXCEL_FILE}，将使用默认名称")
    except ImportError:
        print("⚠️ 未安装 pandas，请运行：pip install pandas")
    except Exception as e:
        print(f"❌ 读取 Excel 失败：{e}")
    return None

def resize_image(img, max_size=1200):
    """压缩图片，保持比例"""
    img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
    return img

def generate_preview():
    """生成 HTML 预览页面"""
    if not os.path.exists(DATA_FILE):
        print("❌ 没有找到产品数据，无法生成预览")
        return

    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        products = yaml.safe_load(f) or []

    html = """<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <title>产品预览</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {{ font-family: Arial, sans-serif; max-width: 1000px; margin: 40px auto; padding: 20px; }}
        .product {{ margin: 30px 0; border-bottom: 1px solid #eee; padding-bottom: 20px; }}
        .product img {{ max-width: 100%; height: auto; border-radius: 8px; }}
        .product h3 {{ color: #333; }}
        .product p {{ color: #666; line-height: 1.6; }}
    </style>
</head>
<body>
    <h1>📦 产品预览</h1>
    <p><small>共 {} 个产品</small></p>
""".format(len(products))

    for p in products:
        html += f"""
    <div class="product">
        <h3>{p['name']}</h3>
        <img src="{p['image']}" alt="{p['alt']}">
        <p><strong>描述：</strong>{p['description']}</p>
    </div>
"""

    html += """
    <footer>
        <p><small>预览页面 | 双击即可查看</small></p>
    </footer>
</body>
</html>
"""

    with open(PREVIEW_FILE, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"🎉 预览页面已生成：file://{os.path.abspath(PREVIEW_FILE)}")

def main():
    os.makedirs(NEW_IMAGES_DIR, exist_ok=True)
    os.makedirs(IMAGES_DIR, exist_ok=True)

    image_exts = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']
    files = [f for f in os.listdir(NEW_IMAGES_DIR) if os.path.splitext(f.lower())[1] in image_exts]

    if not files:
        print("⚠️  new_images 文件夹里没有图片，请拖入图片后再运行。")
        return

    print(f"✅ 发现 {len(files)} 张图片")

    # 读取 Excel 数据（可选）
    excel_data = load_from_excel()

    # 读取已有产品数据
    existing_products = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            if content.strip():
                existing_products = yaml.safe_load(content) or []

    new_products = []

    for i, filename in enumerate(sorted(files)):
        src = os.path.join(NEW_IMAGES_DIR, filename)
        index = START_INDEX + len(existing_products) + i
        new_name = f"p-{index:02d}.jpg"
        dst = os.path.join(IMAGES_DIR, new_name)

        # 压缩并保存图片
        img = Image.open(src)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        img = resize_image(img, 1200)
        img.save(dst, "JPEG", quality=85, optimize=True)

        # 从 Excel 读取信息，否则用默认值
        if excel_data and filename in excel_data:
            name = excel_data[filename].get('name', f"产品{index}")
            alt = excel_data[filename].get('alt', f"产品图片 {index}")
            desc = excel_data[filename].get('description', f"这是第 {index} 个产品")
        else:
            name = f"产品{index}"
            alt = f"产品图片 {index}"
            desc = f"这是第 {index} 个产品"

        new_products.append({
            "name": name,
            "image": f"/images/{new_name}",
            "alt": alt,
            "description": desc
        })

        print(f"✅ 已处理: {filename} → {new_name} | 名称: {name}")

    # 合并数据
    all_products = new_products+existing_products 
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        yaml.dump(all_products, f, allow_unicode=True, default_flow_style=False, indent=2)

    # 清理 new_images
    for f in files:
        os.remove(os.path.join(NEW_IMAGES_DIR, f))

    print(f"🎉 成功！共添加 {len(new_products)} 个新产品")
    print(f"📝 数据已保存到 {DATA_FILE}")

    # 生成预览
    generate_preview()

if __name__ == "__main__":
    main()