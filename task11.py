def word_count(value):
    string=value
    i=0
    counter=0
    while string[i]!= '.':
        if string[i]==' ':
            counter+=1
        i+=1
    return counter+1
print(word_count('hi hi hi.'))

# Второй вариант
# def word_count(word):
#     string=word
#     substring= ' '
#     count=string.count(substring)
#     print('the word count is:'+str(count+1))
#     return 0
# word_count("the wether is cool")