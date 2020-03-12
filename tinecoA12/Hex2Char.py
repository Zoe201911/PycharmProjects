"""
十六进制和字符串的互相转换

"""
import binascii


def hex2char(data):
    output = binascii.a2b_hex(data)
    print(output)


def char2hex(data):
    data = data.encode('utf-8')
    data = b'data'
    output = binascii.hexlify(data)
    print(output)


def main():
    # hex2char('604650466163746f7279526573657400007130303039006a7b7d000a')
    char2hex('PFactoryReset\x00\x00q0009\x00j{}\x00\n')
if __name__ == '__main__':
    main()