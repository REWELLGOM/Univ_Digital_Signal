__version__=1.0
def calmax(*arg):
    return max(arg)
def calmin(*arg):
    return min(arg)
if __name__=='__main__':   
    print('calculator Test')
    print(calmax(1,2,3,4))
    print(calmin(2,3,4,5))