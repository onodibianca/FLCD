class Grammer:
    def __init__(self):
        self.N = [] #nonTerminals
        self.E = [] #terminals
        self.P = [] #production
        self.S = '' #initial state

    def readGrammer(self):
        with open('g1.txt') as f:
            self.N=f.readline().strip("\n").split(" ")
            self.T=f.readline().split(" ")
            self.S=f.readline()
            while f:
                line=[]
                products=[]
                nonTerm=''
                line=f.readline()
                if line=="":
                    break
                else:
                    nonTerm=line[0]
                    sides=line.split(">")
                    if len(sides[0])>2:
                        nonTerm='-1'
                    products=sides[1].strip("\n").split("|")
                    self.P.append((nonTerm,products))
            self.T.pop()
        print(f"N={self.N}\nT={self.T}\nS={self.S}P={self.P}\n")
        

    def getNonterminals(self):
        print(self.N)

    def getTerminals(self):
        print(self.T)

    def getProduction(self):
        print(self.P)

    def getPrByNo(self,nonTerm):
        for i in self.P:
            if i[0]==nonTerm:
                print(i[1])

    def checkCFG(self):
        flag=True
        for i in self.P:
            if i[0]=='-1':
                flag=False
            else:
                if i[0] not in self.N:
                    flag=False
                else:
                    for j in i[1]:
                        for k in j:
                            if k not in self.T and k not in self.N and k!="Epsilon":
                                flag=False
        if flag==False:
            print('Incorrect syntax')
        else:
            print("Everything went well")



            


gr=Grammer()
gr.readGrammer()
gr.getNonterminals()
gr.getTerminals()
gr.getProduction()
print("\n")
gr.getPrByNo("S")
print("\n")
gr.checkCFG()
print("\n")