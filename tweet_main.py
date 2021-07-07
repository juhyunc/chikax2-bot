import random
import config
import tweet


def main():
    filename=open('text.txt','r')
    text=filename.readlines()
    filename.close()
    
    count=random.randint(0,len(text)-1)
    tweet.post(text[count])

if __name__ == "__main__":
    main()
