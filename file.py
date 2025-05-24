#   READING FILES
# f = open('myfile.txt', 'r' )
# print(f)
# text=f.read()
# print(text)
# print(f.read())
# f.close()


# WRITING FILES
# f = open('myfile.txt', 'w' )
# write = f.write
# write('Hello World')
# write(' hey everyone how are you \n ')
# write( ' i am fine \n')
# write('i hope everyone is fine ')
# f.close()




f=open('myfile.txt', 'r' )
# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         print(line,type(line))
#         break
#     print(line)



# with open('myfile.txt', 'r') as f:
#     print(type(f))
#     f.seek(10)
#     # move to the 10th bytes in the file
# f.tell() # returns the current position of the file pointer
#     data=f.read(5) #read 5 bytes
# print(data)

# f.truncate(0) # delete the content of the file
# f.truncate(5) # delete the content of the file from 5 bytes
