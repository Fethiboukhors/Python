def main():
    age=input("enter your age")
    if(int(age)>=8 and int(age)<=10):
        print("Children")
    elif(int(age)>=11 and int(age)<=15):
        print("Kids")
    else:
        print("you are welcome")

if __name__ == '__main__':main()
