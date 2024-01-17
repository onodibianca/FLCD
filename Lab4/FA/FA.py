class FA:
    def __init__(self):
        self.Q={}
        self.E={}
        self.q0={}
        self.F={}
        self.T={}

    def read_file(self,name):
        with open(name) as f:
            first_four_lines_selected=""
            for i in range(4):
                line=f.readline().strip()
                found=False
                line.replace(" ","")
                for i in line:
                    if found==True:
                        first_four_lines_selected=first_four_lines_selected+i
                    if i=='{':
                        found=True
            list={}
            list=first_four_lines_selected.strip().split('}')
            self.Q = list[0].split(",")
            self.E = list[1].split(",")
            self.q0 = list[2].split(",")
            self.F = list[3].split(",")
            line=f.readline().strip()


    def __str__(self) -> str:
        return str(f"Q:{self.Q}\nE:{self.E}\nq0:{self.q0}\nF:{self.F}") 
        #print(self.T)

            #for line in f:
            #    if line != '}' and  len(line)>0:

fa=FA()

fa.read_file("FA.in")
print(fa)
    