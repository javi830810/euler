for x in range(3,1000):
    for y in range(3,1000):
        for z in range(3,1000):
            if x**2 + y**2 == z**2 and x+y+z == 1000:
                print '%s + %s + %s = 1000' %(x,y,z)
