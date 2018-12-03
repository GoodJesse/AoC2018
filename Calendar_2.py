fobj = open('boxes.txt', 'r')
box_list = [x.strip('\n ') for x in fobj]
two = 0
three = 0


for box in box_list:
    twochanged = False
    threechanged = False
    for letter in box:
        number = list(box).count(letter)
        if twochanged == False:
            if number == 2:
                two += 1
                twochanged = True
        if threechanged == False:
            if number == 3:
                three += 1
                threechanged = True

print two*three
print len(box)
for box1 in box_list:
    for box2 in box_list:
        difference = 0
        for i in range(len(box1)):
            if box1[i] != box2[i]:
                difference += 1
                index = i
            if difference == 2:
                break
        if difference == 1:
            print box1, box2, index
