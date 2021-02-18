from fractions import Fraction

T = int(input())

def henry(numer, denom):
    if numer == 1:
        return denom
        
    else:
        X = denom//numer + 1

        ''' 시간 초과 코드
        numer = numer * X - denom 
        denom = denom * X
        return henry(numer, denom)
        '''

        '''통과 코드'''
        step = Fraction(numer,denom) - Fraction(1,X)
        return henry(step.numerator, step.denominator)
        ''''''

for _ in range(T):
    A, B = map(int, input().split())
    print(henry(A,B))