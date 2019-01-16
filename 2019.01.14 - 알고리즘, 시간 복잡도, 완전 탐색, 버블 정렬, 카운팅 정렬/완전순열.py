# data = [6, 6, 7, 7, 6, 7]
#
# for i in range(len(data)):   # 6이라고 써도 상관은 없다(해당 data 하에서는)
# 	for j in range(len(data)):
# 		if j != i:
# 			for k in range(len(data)):
# 				if k != i and k != j:
#                     for l in range(len(data)):
#                         if l != i and l != j and l !=k:
#                             for m in range(len(data)):
#                                 if m != i and m != j and m != k and m != l:
#                                     for n in range(len(data)):   # 모든 경우의 수 나열
#                                         if n != i and n != j and n != k and n != l and n != m:
#                                             chk = 0
#                                             if data[i] == data[j] and data[j] == data[k]:  # data에 있는 값 출력
#                                                 chk += 1
#                                             if data[l] == data[m] and data[m] == data[n]:
#                                                 chk += 1
#                                             if data[i] + 1 == data[j] and data[j] + 1 == data[k]:
#                                                 chk += 1
#                                             if data[l] + 1 == data[m] and data[m] + 1 == data[n]:
#                                                 chk += 1
#                                             if chk == 2:   # 앞줄 따로 뒷줄따로
#                                                 print("Baby jin")
#                                             else:
#                                                 print("Not Baby Jin")



def baby_jin(data):
    for i1 in range(6):   # 6이라고 써도 상관은 없다(해당 data 하에서는)
        for i2 in range(6):
            if i2 != i1:
                for i3 in range(6):
                    if i3 != i1 and i3 != i2:
                        for i4 in range(6):
                            if i4 != i1 and i4 != i2 and i4 != i3:
                                for i5 in range(6):
                                    if i5 != i1 and i5 != i2 and i5 != i3 and i5 != i4:
                                        for i6 in range(6):   # 모든 경우의 수 나열
                                            if i6 != i1 and i6 != i2 and i6 != i3 and i6 != i4 and i6 != i5:
                                                chk = 0
                                                print(data[i1], data[i2], data[i3], data[i4], data[i5], data[i6])
                                                if data[i1] == data[i2] and data[i1] == data[i3]:  # data에 있는 값 출력
                                                    chk += 1
                                                if data[i4] == data[i5] and data[i4] == data[i6]:
                                                    chk += 1
                                                if data[i1] + 1 == data[i2] and data[i2] + 1 == data[i3]:
                                                    chk += 1
                                                if data[i4] + 1 == data[i5] and data[i5] + 1 == data[i6]:
                                                    chk += 1
                                                if chk == 2:   # 앞줄 따로 뒷줄따로
                                                    return


data = [6, 6, 7, 7, 6, 7]

if baby_jin(data):
    print("Baby Jin")
else:
    print("Not Baby Jin")





