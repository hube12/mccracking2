import os,ast,sys
sys.path.append("Ressources")
import cracker2 as c
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
    c.main(dataPack,ram,core,ok)



if __name__ == '__main__':
    main()