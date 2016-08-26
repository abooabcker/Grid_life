from time import sleep
class grid_life():
                              
        
    def __init__(self,ip):
        #global life_grid
        #global result
        self.result=[]
        self.life_grid= ip
        self.s=self.sizee()
        for i in range(self.s):
            self.result.append([0]*(self.s))
        
    def sizee(self):
        return(len(self.life_grid[0]))
        
    def is_alive(self,x,y):
        if self.life_grid[x][y]==1:
            return True
        else:
            return False

    def num_neighbours(self,xx,yy):
        count=0
        for i in range(xx-1,xx+2):
            j=yy-1
            for j in range(yy-1,yy+2):
                if i>=0 and j>=0 and i<(self.s) and j<(self.s):
                    if self.life_grid[i][j]==1:
                        count += 1
        return count
        
    def apply_rules(self):
        for m in range(self.s):
            for n in range (self.s):
                num=self.num_neighbours(m,n)
                if self.is_alive(m,n)==True:
                    num-=1
                    if num in (2,3):
                        self.result[m][n]=1
                else:
                    if num==3:
                        self.result[m][n]=1
        
        return(self.result)

    def printer(self,r):
        print "\n"
        for i in r:
            for j in i:
                    if  j==1:
                        print'#',
                    else:
                        print '.',
            print "\n"
        
class runner():
    def __init__(self,r1):
        r2=[]
        while r1 != r2:
            B=grid_life(r1)
            r1=(B.apply_rules())
            sleep(1)
            B.printer(r1)
            B=grid_life(r1)
            r2=(B.apply_rules())
            sleep(1)
            B.printer(r2)
        print ("O V E R")
