text = "hello world this is python python programming "
split=text.split()



def unique_words():
    count=len(split)
    for i in range(len(split)):
        for j in range(i+1,len(split)):
            if split[i]==split[j]:
                count-=1
                print('Number of unique words:',count)

def longest_word():
    length=0
    for k in range(len(split)):
        if len(split[k]) > length:
            length=len(split[k])
    print('Length of the longest word:',length)


unique_words()
longest_word()


