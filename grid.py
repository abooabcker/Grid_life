class grid_life():
    life_grid=[]
    result=[]
                              
        
    def __init__(self,ip):
        global life_grid
        global result
        result=[]
        life_grid= ip
        self.s=self.sizee()
        for i in range(self.s):
            result.append([0]*(self.s))
        
    def sizee(self):
        return(len(life_grid[0]))
        
    def is_alive(self,x,y):
        if life_grid[x][y]==1:
            return True
        else:
            return False

    def num_neighbours(self,xx,yy):
        count=0
        for i in range(xx-1,xx+2):
            j=yy-1
            for j in range(yy-1,yy+2):
                if i>=0 and j>=0 and i<(self.s) and j<(self.s):
                    if life_grid[i][j]==1:
                        count += 1
        return count
        
    def apply_rules(self):
        for m in range(self.s):
            for n in range (self.s):
                num=self.num_neighbours(m,n)
                if self.is_alive(m,n)==True:
                    num-=1
                    if num in (2,3):
                        result[m][n]=1
                else:
                    if num==3:
                        result[m][n]=1
        
        return(result)

    def printer(self,r):
        print "\n"
        for i in r:
            for j in i:
                    if  j==1:
                        print'#',
                    else:
                        print '.',
            print "\n"
        
