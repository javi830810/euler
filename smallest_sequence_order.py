sequence = [1,2,3,4,7,6,5,9,7,10,11,12]

start = -1
end = len(sequence)

for x in xrange(0,len(sequence)):
    valid = True
    for y in xrange(x+1,len(sequence)):
        if sequence[y] < sequence[x]:
            valid = False
            break
    if valid:
        start = x
    else:
        break


for x in xrange(len(sequence)-1,-1,-1):
    valid = True
    for y in xrange(x,-1,-1):
        if sequence[y] > sequence[x]:
            valid = False
            break
    if valid:
        end = x
    else:
        break


print start
print end
