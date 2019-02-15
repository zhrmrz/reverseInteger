class Sol:
    def __init__(self,a):
        self.a=a
    def divide(self):
        reverse=0
        if(self.a<0):
            x=-1
            self.a*=-1
        else:
            x=1
        while(self.a>0):
            reminder=self.a%10
            reverse=reverse*10+reminder
            self.a=self.a//10
        if reverse>2**31-1:
            return 0
        return (x*reverse)
if __name__ == '__main__':
    a=int(input("Enter a number"))
    p1=Sol(a)
    print(p1.divide())
