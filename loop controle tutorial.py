def main():
    word="python"
    for letter in word:
        if(letter=='t'):
            continue
        elif(letter=='o'):
            break
        elif(letter=='y'):
            pass
        print(letter)



if __name__ == '__main__':main()