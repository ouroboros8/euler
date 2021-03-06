'''
Problem:

    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
'''

from euler import factorise

def solve():
    '''
    Solve the problem.
    '''
    return max(factorise(600851475143))

if __name__ == '__main__':
    print(solve())
