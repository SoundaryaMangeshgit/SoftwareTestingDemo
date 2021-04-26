def check_pythagorean_triple(a: int,b: int, c: int ):
    if (a*a + b*b)== (c*c):
        return True
    if( b*b + c*c)== (a*a):
        return True
    if(c*c + a*a)== (b*b):
        return True
    else:
        return False