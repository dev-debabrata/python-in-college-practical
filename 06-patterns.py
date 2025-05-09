# 6.  Print the patterns 
# a)
# *
# * *
# * * *
# * * * *
# * * * * *

# b)
# H 
# H E 
# H E L
# H E L L
# H E L L O

# Pattern a)
for i in range(1, 6):
    print("* " * i)

# Pattern b)
word = "HELLO"

for i in range(1, len(word) + 1):
    print(' '.join(word[:i]))
