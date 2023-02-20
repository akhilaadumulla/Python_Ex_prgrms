# txt = "hello"

# print(max(txt))

# def sum(x):

#     res = 0

#     for i in range(x):

#         res+=i

#     return res

    

# print(sum(4))
# def print_nums(x):

#   for i in range(x):

#     print(i)

#     return

# print_nums(10)

# def func(x):

#   res = 0

#   for i in range(x):

#      res += i

#   return res

# print(func(3))
text = input()
word = input()

def search(text, word):
	if word in text:
		print("word found")
	else:
		print("word not found")
	
search(word, text)
print(search(text, word))