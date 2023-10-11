import os 
n = input("Input string: ")
with open ('digit.txt','w') as d:
  with open('letter.txt','w') as l:
    with open('special.txt','w') as s:
      n = ''.join(list(n.split(' ')))
      for i in n:
        if i.isdigit():
          d.write(i)
        elif i.isalpha():
          l.write(i)
        else:
          s.write(i)
      
  