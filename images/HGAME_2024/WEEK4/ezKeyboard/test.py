normalKeys = {"04": "a", "05": "b", "06": "c", "07": "d", "08": "e", "09":
"f", "0a": "g", "0b": "h", "0c": "i",
"0d": "j", "0e": "k", "0f": "l", "10": "m", "11": "n", "12":
"o", "13": "p", "14": "q", "15": "r",
"16": "s", "17": "t", "18": "u", "19": "v", "1a": "w", "1b":
"x", "1c": "y", "1d": "z", "1e": "1",
"1f": "2", "20": "3", "21": "4", "22": "5", "23": "6", "24":
"7", "25": "8", "26": "9", "27": "0",
"28": "<RET>", "29": "<ESC>", "2a": "<DEL>", "2b": "\t", "2c": "<SPACE>", "2d": "-", "2e": "=", "2f": "[",
"30": "]", "31": "\\", "32": "<NON>", "33": ";", "34": "'",
"35": "<GA>", "36": ",", "37": ".", "38": "/",
"39": "<CAP>", "3a": "<F1>", "3b": "<F2>", "3c": "<F3>", "3d": "<F4>", "3e": "<F5>", "3f": "<F6>",
"40": "<F7>", "41": "<F8>", "42": "<F9>", "43": "<F10>", "44": "<F11>", "45": "<F12>"}
shiftKeys = {"04": "A", "05": "B", "06": "C", "07": "D", "08": "E", "09": "F",
"0a": "G", "0b": "H", "0c": "I",
"0d": "J", "0e": "K", "0f": "L", "10": "M", "11": "N", "12": "O",
"13": "P", "14": "Q", "15": "R",
"16": "S", "17": "T", "18": "U", "19": "V", "1a": "W", "1b": "X",
"1c": "Y", "1d": "Z", "1e": "!",
"1f": "@", "20": "#", "21": "$", "22": "%", "23": "^", "24": "&",
"25": "*", "26": "(", "27": ")",
"28": "<RET>", "29": "<ESC>", "2a": "<DEL>", "2b": "\t", "2c": "<SPACE>", "2d": "_", "2e": "+", "2f": "{",
"30": "}", "31": "|", "32": "<NON>", "33": "\"", "34": ":", "35":
"~", "36": "<", "37": ">", "38": "?",
"39": "<CAP>", "3a": "<F1>", "3b": "<F2>", "3c": "<F3>", "3d": "<F4>", "3e": "<F5>", "3f": "<F6>",
"40": "<F7>", "41": "<F8>", "42": "<F9>", "43": "<F10>", "44": "<F11>", "45": "<F12>"}
output = []
last = []
new = []
keys = open('hgame2.txt')
press = ''
for line in keys:
    try:
        if line[2]!='0' or (line[3]!='0' and line[3]!='2'):
            continue
        offset = 6
        new = []
        while line[offset:offset+2] != '00':
            press = line[offset:offset+2]
            if press in normalKeys.keys():
                if line[3]=='0':
                    key = normalKeys[press]
                else:
                    key = shiftKeys[press]
            else:
                key = '[unknown]'
            if press not in last:
                output.append(key)
            new.append(press)
            offset += 2
    except:
        print(line)
    finally:
        last = new

keys.close()
flag=0

for i in range(len(output)):
    try:
        if output[i]=="<CAP>":
            flag = 1-flag
        if flag!=0:
            output[i]=output[i].upper()
    except:
        pass
output = [x for x in output if x != '<CAP>']

new_output = []

for i in range(len(output)):
    if output[i] == "<DEL>":
        new_output = new_output[:-1]
    else:
        new_output.append(output[i])

print ("".join(new_output))