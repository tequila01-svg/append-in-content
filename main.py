file=open('sample.txt', 'r')
print(file.read())
file.close()

#append
file_append=open('sample.txt','a')
file_append.write("\n it is my first hobby")
file_append.close()