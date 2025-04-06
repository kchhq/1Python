i, k ,ggline = 0, 0, ""

for i in range(2, 10, 1) :
    ggline += (" #  %d단  #" %i)

print(ggline)

for i in range(1,10) :
    ggline =""

    for k in range(2,10) :
        ggline += str("%2dX %2d= %2d" % (k, i, k*i))

    print(ggline)