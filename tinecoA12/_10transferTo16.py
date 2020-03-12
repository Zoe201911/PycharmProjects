

def transferNumber(str1):
    list1 = []
    str2 = str1.split(' ')
    for i in str2:
        str3 = int(i,16)
        list1.append(str3)

    print(list1)

if __name__ == '__main__':
    list2 = ["06 07 09 0c 0c 0f 11 11","36 36 3c 3c 3f 48 48 48"]
    list3 = ["36 36 3c 3c 3f 48 48 72"]
    for l in list2:
        transferNumber(l)