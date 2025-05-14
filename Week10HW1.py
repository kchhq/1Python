inFp=None
inStr=""
i = 1

inFp=open("/Users/kchhq/Desktop/Mysmallcode/1Python/함수모음집.txt","r",encoding='UTF8')


while True:
    inStr=inFp.readline()
    if inStr=="":
        break
    print(f"{i}:  {inStr}", end="")
    i += 1

inFp.close()