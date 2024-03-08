# Finding the Greater Number

if __name__=='__main__':
    A=int(input("Insert value of A: "))
    B=int(input("Insert value of B: "))

    if (A==B):
        print(f"Both numbers are equal.")
    else:  
        if (A<B):
            Greater=B
        else:
            Greater=A
        print(f"{Greater} is the greatest of both: A:{A} and B:{B}") 