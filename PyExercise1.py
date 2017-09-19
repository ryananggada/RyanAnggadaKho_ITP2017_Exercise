right_num=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        right_num.append(i)
print(right_num)
