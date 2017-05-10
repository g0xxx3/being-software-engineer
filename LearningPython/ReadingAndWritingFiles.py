# https://learnpythonthehardway.org/book/ex16.html

file_name = 'inputfile'
print("We're going to erase %r." % file_name)
print("If you don't want that, hit CTRL-C (^C).")
print( "If you do want that, hit RETURN.")
input('?')

print("Opening file")
file = open(file_name, 'w')

print("Truncating the file. Goodbye!!!")
file.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print( "I'm going to write these to the file.")

file.write(line1)
file.write("\n")
file.write(line2)
file.write("\n")
file.write(line3)
file.write("\n")

print("And finally, we close it.")
file.close()