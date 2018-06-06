#for i in range(0,255):
#    print(i)
#    print(chr(i))


#bs = 0
#z = "abcdefghijklmnopqrstuvwxyz"
#j = 0
#l = 0
#for c in z:
#    m = ord(c.lower())
#    n = ord(c.lower()) - ord('a')
#    j = (1 << n)
#    l = (1 |= n)
#    if not 0 <= n < 26:
#        continue
#    if bs & (1 << n):
#        print("False")
#    bs |= (1 << n)
#    
#    print("c: %s \n m: %d n: %d bs: %d j: %d l: %d" % (c, m, n, bs, j, l))
#    print("bin(n): ", bin(n))
#    print("bin(1<<n)): ", bin(1<<n))
#    print("bin(bs)): ", bin(bs))
#    print("bin(bs & (1 <<n))): ", bin(bs & (1 << n)))

for i in range(0,16):
    print(i+i)