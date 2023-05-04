import argparse


freelist=[]
decrypted=''
#works only with lower case alphabets and no special characters
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
parser = argparse.ArgumentParser(description="c1pher : A cipher decrypt made by 0xDevvvvv\n(currently supports only shift cipher)")
parser.add_argument('-k','--key',help='key : Number of times the character should be shifted',type=int,required=False,default=0)
parser.add_argument('-t','--text',help='text : The text to be decoded using shift cipher ',type=str,required=True , default='No text to be decoded!!!')
args= parser.parse_args()
#argument for different character set 
#Currently Developing
#parser.add_argument('-c','--characters',help='characters  : The set of characters to be used for decoding',default=alphabets)



shift=args.key
message=args.text

def  decrypt(message,alphabets,shift,freelist):
     for i in message:
        if i==' ':
            freelist.append("+")
            continue
        search=alphabets.index(i.lower()) # searching in character set
        if (search+shift)<26 and (search+shift)>=0:
            freelist.append(alphabets[search+shift])
        elif (shift+search)>25:  #i shifted key value is more than 26 
            newindex=(search+shift+1)%26-1
            freelist.append(alphabets[newindex])
        elif (search+shift)<0:   #if shifted key value is less than 26
            newindex=25+(search+shift)
            freelist.append(alphabets[newindex])
     return(freelist)
def final_output(decrypted,freelist): # output in a variable
     for i in freelist:
            if i=='+':
                decrypted+=' '
                continue
            decrypted+=i
     return(decrypted) 

if shift!=0:
    print("key : "+str(shift))
    decrypt(message,alphabets,abs(shift),freelist)  #shifting towards right
    print("Shifting" +" towards right ---> "+str(final_output(decrypted,freelist)))
    
    freelist=[]  #list keeps accumulating values unless cleared
    decrypt(message,alphabets,-abs(shift),freelist)  #shifting towards left
    print("Shifting" +" towards left ---> "+str(final_output(decrypted,freelist)))
    
if shift==0:
    print("Shifting towards right..")
    while shift<26:  #finding all possible shift combinations towards right
        freelist=[]
        decrypt(message,alphabets,shift,freelist)
        print("Key : " +str(shift)+" --> "+str(final_output(decrypted,freelist)))
        shift+=1


