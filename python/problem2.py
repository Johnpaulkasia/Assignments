def task(no_br,str, open_br, close_br, pos):
    last=[]
    if( no_br >= 1 and no_br <= 8):

        if (open_br < no_br):
            str[pos] = '('
            task(no_br, str, open_br+1, close_br, pos+1)
    
        if (open_br > close_br):
            str[pos] = ')'
            task(no_br, str, open_br, close_br+1, pos+1)
        
        if (close_br == no_br):

            b = ''.join(str)
            last.append(b)
            print(last)
        
        
        
    else:
        print("Limit Exceeded!") 


open_br = close_br = pos = 0
no_br = 3
str = [' '] * 2 * no_br
task(no_br,str, open_br, close_br, pos)
