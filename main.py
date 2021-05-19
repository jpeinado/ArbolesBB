
from TreeBinary import MyTree

def main():
    print("Ejecutando Examen de Mesa:")
    #pdb.set_trace()
    mytree = MyTree(500)
    mytree.addNode(mytree.getRoot(),200)
    mytree.addNode(mytree.getRoot(),600)
    print(mytree.printInorder(mytree.getRoot()))

if __name__ == "__main__":
    main()
''
