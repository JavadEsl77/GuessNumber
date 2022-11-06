import random


# def gamer(a, b):
#     hads = random.randint(a, b)
#     print(hads)
#     javab = input('آیا درسته ؟')
#     while javab != 'd':
#         if javab == 'k':
#             b = hads
#         elif javab == 'b':
#             a = hads
#
#         hads = random.randint(a, b)
#         print(hads)
#         javab = input('آیا درسته ؟')

def gamer(a, b, j) -> str:
    randList = []
    count = 0
    hads = random.randint(a, b)
    randList.append(hads)
    print(hads)

    if hads > j:
        javab = 'k'
    elif hads < j:
        javab = 'b'
    else:
        javab = 'd'

    while javab != 'd':
        if javab == 'k':
            b = hads
            count += 1
        elif javab == 'b':
            a = hads
            count += 1

        hads = random.randint(a, b)
        if hads not in randList:
            print(hads)
            if hads > j:
                javab = 'k'
            elif hads < j:
                javab = 'b'
            else:
                javab = 'd'

    return count + 1


a = int(input("a: "))
b = int(input("B: "))
j = int(input("j: "))
print("count : ", gamer(a, b, j))
