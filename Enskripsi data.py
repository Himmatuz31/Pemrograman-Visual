import string


abjad = string.printable

def enkrip (pesan) :
    global abjad

    kunci = input('Masukkan key : ')
    cipher = ''
    for i in pesan :
        if i in abjad:
            k = abjad.find(i)
            k = (k + key)%100
            cipher = cipher+abjad[k]
        else:
            cipher = cipher + 1
            
    return cipher

def dekrip(cipher):
    global abjad
    kunci = input ('Masukkan key : ')
    pesan =''
    for i in cipher:
        if i in abjad:
            k = abjad.find(i)
            k = (k - key)%100
            pesan = pesan+abjad[k]
        else:
            pesan = pesan + 1
    return pesan

print ('Himmatuz Zahiroh')

print ('------------------------')
pilihan =  int(input ('1. Enkripsi\n2. Dekripsi\nPilih------------- : '))
                        
if pilihan == 1:
    pesan = input('Masukkan pesan : ')
    print(enkrip(pesan))

elif pilihan ==2:
    cipher= input('Masukkan pesan : ')
    print(dekrip(cipher))
else:
    print('Masukkan pilihan 1 atau 2 !!')
    
