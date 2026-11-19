# given 2 strings, check whether they are anagrams or not.

# eg listen and silent are anagrams.

def anagrams(str1,str2):
  str1.replace(" ","") # remove empty spaces
  str2.replace(" ","") # remove empty spaces
  if len(str1)!=len(str2):
    return False
  elif str1==str2:
    return True
  else:
    dict1={}
    dict2={}
    for i in str1:
      dict1[i]=1

    for j in str2:
      dict2[j]=1

    return dict1==dict2

str1="listten"
str2="silentt"
print(anagrams(str1,str2))
      