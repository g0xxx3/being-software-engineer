# https://learnpythonthehardway.org/book/ex6.html

# Strings may contain the format characters
n = 10
x = "There are %d types of people" %n

binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print(x)
print(y)

print("I said : %r" %x)
print("I also said %r" %y)

