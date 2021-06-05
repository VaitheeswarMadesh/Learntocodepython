f=open("a.txt", 'a')   #appends the data
f.write("\nhye-hello")
f.close()

f=open("a.txt", "w") #erases and write the data to file
#if the file is existing it wil open and write the data to file
#else if will create a new file
f.write("Gone!")
f.close()