import zipfile
import json
from datetime import datetime

def get_all_file_modification_time(zip_path):
    result = {}
    with zipfile.ZipFile(zip_path, 'r') as myzip:
        for file in myzip.namelist():
            info = myzip.getinfo(file)
            mod_time = datetime(*info.date_time)
            result[file] = str(mod_time)
    return result

# 使用函数并保存结果为json
result = get_all_file_modification_time('output.zip')
with open('output.json', 'w') as f:
    json.dump(result, f)