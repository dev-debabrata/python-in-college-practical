# 8. Find the frequency of each character in 
# "this is a python programming language"
# a)With and b)without dictionary

# a) With
text = "this is a python programming language"
freq = {}

for char in text:
    if char != ' ':
        freq[char] = freq.get(char, 0) + 1
print(freq)



# b) Without
text = "this is a python programming language"
checked = []

for char in text:
    if char != ' ' and char not in checked:
        count = 0
        for c in text:
            if c == char:
                count += 1
        print(char, ":", count)
        checked.append(char)
