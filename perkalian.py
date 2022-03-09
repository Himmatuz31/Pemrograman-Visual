print ("Himmatuz Zahiroh")
print ("MI 2020B_20051397070")

def tabel(a):
    for i in range (0,a+1):
        if i <10:
            print  (i), '',
        else:
            print (i),
        for j in range(1, a+1):
            c = j*i
            if j < 10:
                if c < 10:
                    print ('| %s' %(c) ),
                elif c >= 10 and c < 110:
                    print ('| %s' %(c) ),
               
            else:
                if c < 10:
                    print ('| %s |' %(c) )
                elif c >= 10 and c < 110:
                    print ('| %s |' %(c) )
                
a = 10
tabel(a)
