s = input("Enter your string:")
palindromes = set()
def expand(s, low, high, palindromes):
  
    while low >= 0 and high < len(s) and s[low] == s[high]:  
        palindromes.add(s[low: high + 1])  
        low -= 1
        high += 1


if( (len(s) >= 1 and len(s) <= 16) and s.islower()):
    
    
    
    #se = set(s)
    op = list(s)
    if(len(s) == 1 or len(s) == 2):   
        print(op)
    
    if(len(s) == 3 and s[0] == s[2]):
        op.append(s)
        print(op)
        
    else:
        for i in range(len(s)):
            expand(s, i, i, palindromes)
            expand(s, i, i + 1, palindromes)
        print(palindromes, end='')

else:
    print("Invalid Input! Please lowercase letters only or less then 16")
