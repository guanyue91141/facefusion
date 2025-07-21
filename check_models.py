import os
import re
import zlib

# 1. 递归查找所有引用的模型文件名（.onnx/.hash）
model_dir = os.path.join('facefusion', '.assets', 'models')
code_dir = 'facefusion'
model_files = set()

pattern = re.compile(r"['\"]\.\./\.assets/models/([\w\-\.]+\.(onnx|hash))['\"]")

for root, dirs, files in os.walk(code_dir):
    for file in files:
        if file.endswith('.py'):
            with open(os.path.join(root, file), encoding='utf-8') as f:
                for line in f:
                    for m in pattern.finditer(line):
                        model_files.add(m.group(1))

# 2. 检查本地模型目录下实际存在的文件
actual_files = set(os.listdir(model_dir)) if os.path.exists(model_dir) else set()

# 3. 输出缺失的模型文件，并写入txt
missing = sorted(model_files - actual_files)
if missing:
    print('缺失的模型文件:')
    for f in missing:
        print(f)
    with open('missing_models.txt', 'w', encoding='utf-8') as out:
        for f in missing:
            out.write(f + '\n')
else:
    print('所有模型文件都已齐全！')
    if os.path.exists('missing_models.txt'):
        os.remove('missing_models.txt')

# 4. 校验每个已存在的 onnx 文件的 CRC32
print('\n模型 CRC32 校验结果:')
for f in sorted(actual_files):
    if f.endswith('.onnx'):
        onnx_path = os.path.join(model_dir, f)
        hash_path = os.path.join(model_dir, f.replace('.onnx', '.hash'))
        if os.path.exists(hash_path):
            with open(onnx_path, 'rb') as onnx_file:
                crc32 = format(zlib.crc32(onnx_file.read()), '08x')
            with open(hash_path, 'r', encoding='utf-8') as hash_file:
                hash_value = hash_file.read().strip()
            if crc32 == hash_value:
                print(f'{f}: 校验通过')
            else:
                print(f'{f}: 校验失败！应为 {hash_value}，实际为 {crc32}')
        else:
            print(f'{f}: 缺少对应的 .hash 文件')
