# repeated_letter
def main():
    pass
    inp=input()
    list_1=list(inp)
    temp=[]
    for i in list_1:
        k=list_1.count(i)
        temp.append(k)
    index=(temp.index(max(temp)))
    print(list_1[index])
if __name__ == '__main__':
    main()
