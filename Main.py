import os,ast
import Ressources.cracker2 as c
def main():
    try:
        text=open("data.txt","r")
        print(text)
    except:
        l=os.listdir()
        for el in l:
            if el[0:4]=="data" and el[len(el)-4:len(el)]==".txt":
                text=open(el,"r")
    dataPack=ast.literal_eval(text.readline())
    ram=int(text.readline())
    core=int(text.readline())
    ok=ast.literal_eval(text.readline())
    c.main([94,103,97,100,88,82,76,85,79,91],8000,12,False)




main()