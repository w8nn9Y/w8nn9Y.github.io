def xor_with_0x27(input_file, output_file):
    with open(input_file, 'rb') as f:
        data = f.read()
    xor_data = bytearray([b ^ 0x27 for b in data])
    with open(output_file, 'wb') as f:
        f.write(xor_data)

# 使用函数
xor_with_0x27('maybezip', 'output.zip')