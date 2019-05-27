def ExtractFileName(s):
    a=s.split('/')
    return a[-1]
if __name__=='__main__':
    inputstring=input()
    #inputstring
    print(ExtractFileName(inputstring))
