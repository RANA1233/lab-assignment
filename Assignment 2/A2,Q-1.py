# Question:1
string='Python is a case sensitive language'
# a)
print("(a) Size of string is: ", len(string))
# b)
string1=string[::-1]
print("(b) The reversed string is: ", string1)
#c
S=slice(10, 26)
print("(c) String after slicing: ", string[S])
#d
a=string.replace('a case sensitive', 'object oriented')
print("(d) Replacing substring: ", a)

#[e] (finding index of substring)
i=string.index('a')
print("(e) The index of 'a' is: ", i)

#[f] (removing spaces from the string)
r=string.replace(' ','')
print("(f) Removing white spaces: ", r, end="\n")
