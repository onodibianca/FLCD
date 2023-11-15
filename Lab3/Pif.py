class PIF:
    def __init__(self):
        self.pif_list = []

    def add(self, token, position):
        self.pif_list.append((token,position))

    def __str__(self):
        pif_output=""
        for i in self.pif_list:
            pif_output=pif_output+ "("+ str(i[0]) + "," + str(i[1]) + ")\n" 
        return str(pif_output)
    

    

        