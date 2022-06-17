def subsets(string,currString,currIndex,n):
  if currString!='':
    print(currString)
  for i in range(currIndex,n):
    
    currStringCopy=currString+string[i]
    subsets(string,currStringCopy,i+1,n)
  

string=input()
n=len(string)
string=''.join(sorted(string))
subsets(string,'',0,n)