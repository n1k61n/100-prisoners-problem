import random
n = 100
random.seed()
boxes = [i+1 for i in range(n)]
random.shuffle(boxes)
prisoners = [i+1 for i in range(n)]
random.shuffle(prisoners)



for p in prisoners:
    i = p
    count = 0
    flag = True
    while  p != boxes[i-1] and flag:
        if count > 50:
            flag = False
        i = boxes[i-1]
        count += 1
    if count > 50:
        break

if count > 50:
    print("prisoners lose!!")
else:
    print("prisoners win!!!")
