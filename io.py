myfile = open('test.txt')
print(myfile.read())
print(myfile.read())
myfile.read()
print(myfile.read())
myfile.seek(0)
print(myfile.read())
myfile.seek(0)
print(myfile.readlines())
myfile.close()
with open('test.txt') as my_new_file:
	contents = my_new_file.read()
print(contents)

with open('test.txt', mode= 'r') as myfile:
	contents = myfile.read()
print(contents)	

with open('my_new_file.txt',mode='r') as f:
	print(f.read())       				# Read mode


with open('my_new_file.txt', mode = 'a') as f:
	f.write('FOUR ON FOURTH')

with open('my_new_file.txt',mode='r') as f:
	print(f.read())  	


