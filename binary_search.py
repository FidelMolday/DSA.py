def search(list,a):
    i = 0
    u = len(list)-1
    while i < u :
        mid = (i+u)//2
        
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                i = mid
            else:
                u = mid
                
    list = [4,7,8,12,45,99]
    n = 7
    
    if search(list,n):
        print("Found at", 'pos' +1)
    else:
        print("Not found")
