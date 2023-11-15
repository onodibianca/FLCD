import re

def check_if_identifier(element):
    return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]|_)*$',element) is not None

def check_if_constant(element):
    return re.match(r'^(0|[+|-]?[1-9][0-9]*)$|^\'.*\'',element) is not None

class Scanner:
    def __init__(self) :
        self.separators=[]
        self.operators=[]
        self.reserved_words=[]
        self.digits_alphabet=[]
        self.letters_alphabet=[]

    def read_tokens(self):
        with open('tokens.in', 'r') as f:
            for i in range(14):
                self.operators.append(f.readline().strip())
            for i in range(10):
                separator = f.readline().strip()
                if separator == 'space':
                    self.separators.append(" ")
                else:
                    self.separators.append(separator)
            for i in range(11):
                self.reserved_words.append(f.readline().strip())
            for i in range(53):
                self.letters_alphabet.append(f.readline().strip())
            for i in range(10):
                self.digits_alphabet.append(f.readline().strip())
            print(self.operators,"\n")
            print(self.separators, "\n")
            print(self.reserved_words,"\n")
            print(self.digits_alphabet,"\n")
            print(self.letters_alphabet,"\n")

    def is_in_operator(self, elem):
        for i in self.operators:
            if elem in i :
                return True
        return False
    
    def is_operator(self,elem):
        if elem in self.operators:
            return True
        else:
            return False
        
    ''''def get_required_op(self,elem):
        before=0
        after=0
        l=[]
        for i in range(len(self.operators)):
            if elem in self.operators[i]:
                found=0
                for j in self.operators[i]:
                    if j == elem and found==0:
                        found=1
                    else:
                        if found==0 and j!= elem:
                            before=before+1
                        else:
                            if found==1:
                                after=after+1
                l.append((before,after,i))
        return l'''


    def check_operators(self,op_list):
        list=[]
        error=[]
        separators=[]
        index=0
        for i in op_list:
            if self.is_in_operator(i) == False:
                error.append(i)
        while index < len(op_list):
            if index+1<len(i) and i[index]=='<' and i[index+1]=='<':
                separators.append('<<')
                index=index+2
            else:
                if index+1<len(i) and i[index]=='>' and i[index+1]=='>':
                    separators.append('>>')
                    index=index+2
                else:
                    if self.is_operator(op_list[index]) == True:
                        list.append(op_list[index])
                    else:
                        if op_list[index]== '!':
                            if op_list[index+1]!='=':
                                error.append(op_list[index])
                            else:
                                list.append(('!','='))
                                index=index+1
                    index=index+1
        return (list,error,separators)
    
    def read_file(self,name):
        program=[]
        with open(name,"r") as f:
            for line in f:
                program.append(line)
        return program
    
    def check_all_digits(self,string):
        letter_found=0
        for i in string:
            if i in self.letters_alphabet:
                letter_found=1
        return letter_found
    
    
    def get_elements(self,program):
        elements=[]
        line=-1
        for i in program:
            line=line+1
            j=0
            while j<len(i):
                if i[j] in self.letters_alphabet:
                    word=''
                    while j<len(i) and (i[j] in self.letters_alphabet or i[j] in self.digits_alphabet):
                        word=word+str(i[j])
                        j=j+1
                    elements.append((word,line))
                else:
                    if i[j] in self.digits_alphabet:
                        number=''
                        while j<len(i) and (i[j] in self.letters_alphabet or i[j] in self.digits_alphabet):
                            number=number+i[j]
                            j=j+1
                        elements.append((number,line))
                    else:
                        if i[j] in self.separators:
                            separator=''
                            while j<len(i) and i[j] in self.separators:
                                separator=separator+i[j]
                                j=j+1
                            elements.append((separator,line))
                        else:
                            if i[j] in self.separators:
                                separator=''
                                while j<len(i) and i[j] in self.separators:
                                    separator=separator+i[j]
                                    j=j+1
                                elements.append((separator,line))
                            else:
                                elements.append((i[j],line))
                                j=j+1
        return elements

    
    def get_by_category(self,full_program):
        pif_list=[]
        lex_error_list=[]
        separators_list=[]
        operators_list=[]
        identifiers_list=[]
        constants_list=[]
        reserved_word_list=[]
        quote_flag=False
        quote_nr=0
        string_const=''
        for j in range(len(self.get_elements(full_program))):
            i=self.get_elements(full_program)[j][0]
            line=self.get_elements(full_program)[j][1]
            #checks if separator
            if i[0] in self.separators and quote_flag==False:
                if i in self.separators:
                    separators_list.append(i)
                    pif_list.append((i,-1))
                else:
                    index=0
                    while index < len(i):
                        if i[index] in self.separators:
                            separators_list.append(i[index])
                            pif_list.append((i[index],-1))
                        else:
                            if i[index] =='<':
                                if index+1<len(i) and i[index+1]=='<':
                                    separators_list.append('<<')
                                    pif_list.append(('<<',-1))
                                    index=index+1
                                else:
                                    operators_list.append(i[index])
                                    pif_list.append((i[index],-1))
                            else:
                                if i[index]  =='>':
                                    if i[index+1] == '>':
                                        separators_list.append('>>')
                                        pif_list.append(('>>',-1))
                                        index=index+1
                                    else:
                                        operators_list.append(i[index])
                                        pif_list.append((i[index],-1))
                        index=index+1
            else:
                #checks if identifier/reserved word
                if i[0] in self.letters_alphabet and quote_flag==False:
                    if check_if_identifier(i):
                        if i in self.reserved_words:
                            reserved_word_list.append(i)
                            pif_list.append((i,-1))
                        else:
                            identifiers_list.append(i)
                            pif_list.append((i,-3))
                    else:
                        lex_error_list.append(i)
                        pif_list.append((i,-4,line))
                else:
                    #checks if constant nr or identifier/resv word 
                    if i[0] in self.digits_alphabet and quote_flag==False:
                        if self.check_all_digits(i)==0:
                            if check_if_constant(i):
                                constants_list.append(i)
                                pif_list.append((i,-2))
                            else:
                                lex_error_list.append(i)
                                pif_list.append((i,-4,line))
                        else:
                            if check_if_identifier(i):
                                if i in self.reserved_words:
                                    reserved_word_list.append(i)
                                    pif_list.append((i,-1))
                                else:
                                    identifiers_list.append(i)
                                    pif_list.append((i,-3))
                            else:
                                lex_error_list.append(i)
                                pif_list.append((i,-4,line))
                    else:
                        #checks if operator
                        if self.is_in_operator(i[0])==True and quote_flag==False:
                            if self.is_operator(i)==True:
                                operators_list.append(i)
                                pif_list.append((i,-1))
                            else:
                                if self.check_operators(i)[0]!=[]:
                                    operators_list.append(self.check_operators(i)[0])
                                    for j in self.check_operators(i)[0]:
                                        pif_list.append((self.check_operators(i)[0][j],-1))
                                if self.check_operators(i)[1]!=[]:
                                    lex_error_list.append(self.check_operators(i)[1])
                                    pif_list.append((self.check_operators(i)[1],-4,line))
                                if self.check_operators(i)[2]!=[]:
                                    separators_list.append(self.check_operators(i)[2])
                                    for j in self.check_operators(i)[2]:
                                        pif_list.append((self.check_operators(i)[2][j],-1))
                        else:
                            if i=='\'':
                                quote_nr=quote_nr+1
                                string_const=string_const+i
                                if quote_nr%2==1:
                                    quote_flag=True
                                if quote_nr%2==0:
                                    quote_flag=False
                                    pif_list.append((string_const,-2))
                                    string_const=''
                            else:
                                if quote_flag==True:
                                    string_const=string_const+i
                                else:
                                    if i!="\n":
                                        lex_error_list.append(i)
                                        pif_list.append((i,-4,line))
        return (pif_list)
sc=Scanner()
           
print()
    
    













            

