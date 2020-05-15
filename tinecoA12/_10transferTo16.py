

def transferNumber(str1):
    list1 = []
    str2 = str1.split(' ')
    for i in str2:
        str3 = int(i,16)
        list1.append(str3)

    print(list1)

if __name__ == '__main__':
    list2 = ["03 03 04 06 09 0b 0d 0d"]
    list3 = ["36 36 3c 3c 3f 48 48 72"]
    for l in list2:
        transferNumber(l)