from Scanner import *
from Pif import *
from SymbolTable import *



def main():
    sc=Scanner()
    sc.read_tokens()
    sti=HashTable(13)
    stc=HashTable(13)
    pif=PIF()
    value_const=0
    value_ident=0
    error_found=False
    errorf=open("LexicalErrors.out","w")

    for i in sc.get_by_category(sc.read_file("p1err.txt")):
        if i[1]==-1:
            pif.add(i[0],i[1])
        else:
            if i[1]==-2:
                if stc.check_if_already_exists(i[0])==-1:
                    stc.insert(i[0],value_const)
                    pif.add(i[0],value_const)
                    value_const=value_const+1
                else:
                    pif.add(i[0],stc.get_value(i[0]))
            else:
                if i[1]==-3:
                    if sti.check_if_already_exists(i[0])==-1:
                        sti.insert(i[0],value_ident)
                        pif.add(i[0],value_ident)
                        value_ident=value_ident+1
                    else:
                        pif.add(i[0],sti.get_value(i[0]))
                else:
                    if i[1]==-4:
                        error_found=True
                        errorf.write(f"you have a lixical error on line {i[2]}: {i[0]} \n")
    if error_found==False:
        print("Lexically_correct")
    else:
        print("Lexically incorrect")

    stif=open("Sti.out","w")
    stif.write("Hash Table was used to represent the Symbol Table\n")
    stif.write(str(sti))
    stcf=open("Stc.out","w")
    stcf.write("Hash Table was used to represent the Symbol Table\n")
    stcf.write(str(stc))
    piff=open("PIF.out","w")
    piff.write(str(pif))

main()
            

            

