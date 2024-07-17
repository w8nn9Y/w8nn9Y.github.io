import json

# 读取json文件
with open('output.json', 'r') as f:
    data = json.load(f)
string_of_01 =''
# 遍历json数据
for file, time in data.items():
    # 检查文件名是否在指定范围内
    if 'out/' in file and 'png' in file:
        file_number = int(file.split('/')[1].split('.')[0])
        if file_number >= 1 and file_number <= 118:
            # 检查时间的最后一位是否为0
            if time[-1] == '0':
                print(f"{file_number} - 0")
                string_of_01 += '0'
            else:
                print(f"{file_number} - 1")
                string_of_01 += '1'

print(string_of_01)

# 二进制转ascii字符串

def binary_to_string(binary):
    result = ''
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        result += chr(int(byte,2))  #从二进制转为十进制
    # 忽略不可见字符
    result = ''.join([i if ord(i) > 31 and ord(i) < 127 else '' for i in result])
    return result

key_of_zip = binary_to_string(string_of_01)
print(key_of_zip)