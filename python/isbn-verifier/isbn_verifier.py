def verify(isbn):
    # strip non-numerics
    # max_length: 10
    #  last digit can be 'X' to represent 10 'XX' not allowed
    # http://exercism.io/exercises/python/isbn-verifier/readme
    
    t = isbn
    t = [s for s in t if s.isdigit() or (s.lower() == 'x')]
    t = [s for s in t if s.isdigit() or t[9].lower() == 'x']
    
    if t != '' and len(t) == 10:
        if t[9].lower() == 'x':
            t.pop()
            t.insert(9,10)
            t = list(map(int, t))
        elif all(isinstance(item, int) for item in t):
            return False
            
        if not all(isinstance(item,int) for item in t):
            t = list(map(int,t))
            
        result = ((t[0]*10+t[1]*9+t[2]*8+t[3]*7+t[4]*6+t[5]*5+t[6]*4+t[7]*3+t[8]*2+t[9]*1) % 11)
        
        if result == 0:
            return True
        else:
            return False
    else:
        return False
            
    pass