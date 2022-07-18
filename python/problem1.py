def unique(str, a, b):
    
    seen = [0]*(26)
 
    for k in range(a, b + 1):
        if (seen[ord(str[k]) -
                   ord('a')] == True):
            return False
             
        seen[ord(str[k]) -
                ord('a')] = True
 
    return True
 
def longestUniqueSubstr(str):
     
    n = len(str)
     
    res = 0
     
    for i in range(n):
        for j in range(i, n):
            if (unique(str, i, j)):
                res = max(res, j - i + 1)
                 
    return res
 
if __name__ == '__main__':
     
    str = "abcabcbb"
     
    len = longestUniqueSubstr(str)
    print("The longest substring without repeating characters is ", len)
 
