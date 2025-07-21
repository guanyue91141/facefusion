import os
import requests
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

MODEL_VERSION = 'models-3.0.0'
BASE_URL = f'https://github.com/facefusion/facefusion-assets/releases/download/{MODEL_VERSION}/'
TARGET_DIR = os.path.join('facefusion', '.assets', 'models')
THREADS = 6  # 可根据带宽和CPU调整

if not os.path.exists(TARGET_DIR):
    os.makedirs(TARGET_DIR)

with open('missing_models.txt', 'r', encoding='utf-8') as f:
    files = [line.strip() for line in f if line.strip()]

def download_file(file):
    url = BASE_URL + file
    out_path = os.path.join(TARGET_DIR, file)
    print(f'正在下载 {file} ...')
    try:
        resp = requests.get(url, stream=True, timeout=30)
        resp.raise_for_status()
        total = int(resp.headers.get('content-length', 0))
        with open(out_path, 'wb') as out, tqdm(
            total=total, unit='B', unit_scale=True, desc=file, ncols=80, ascii=True, leave=False
        ) as bar:
            for chunk in resp.iter_content(chunk_size=8192):
                if chunk:
                    out.write(chunk)
                    bar.update(len(chunk))
        print(f'成功下载: {file}')
    except Exception as e:
        print(f'下载失败: {file}，来源 {url}，原因: {e}')

with ThreadPoolExecutor(max_workers=THREADS) as executor:
    futures = [executor.submit(download_file, file) for file in files]
    for future in as_completed(futures):
        pass  # 结果已在download_file中输出

print('所有缺失模型文件下载尝试已完成。')
