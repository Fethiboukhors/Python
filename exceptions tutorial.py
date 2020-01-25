def main():
    try:
        readfile=open("test.txt","r")
        for line in readfile:
            print(line)
        readfile.close()
    except IOError:
        print("file not found")
    else:
        print("what next")


if __name__ == '__main__':main()