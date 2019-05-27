def ExtractFileName(s):
    a=s.split('/')
    return a[-1]

inputstring=input()
#inputstring
print(ExtractFileName(inputstring))
