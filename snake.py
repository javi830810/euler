sequence = [1,2,3,4,5]
direction = -1
index = 0

times = 0

while True:
    if times == 3:
        break
    print sequence[index]

    if index == 0 or index == len(sequence)-1:
        print sequence[index]
        direction = -1 * direction
        times += 1

    index += 1*direction
