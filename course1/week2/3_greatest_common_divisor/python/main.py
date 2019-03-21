# python3

##
#
# Python implementation to find the greatest common divisor between two numbers
#
# (c) Copyright 2019 Clayton J. Wong ( http://www.claytonjwong.com )
#
##

def gcd( a, b ):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

if __name__ == '__main__':
    a, b = map( int, input().split() )
    ans = gcd( a, b )
    print( ans )
