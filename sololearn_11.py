# try:
#     num = 5 / 0
# except:
#     print("An error occurred")
#     raise

# print(1)
# assert 2 + 2 == 4
# print(2)
# assert 1 + 1 == 3
# print(3)

# print(0)
# assert "h" != "w"
# print (1)
# assert False
# print(2)
# assert True
# print(3)

# file = open("filename.txt", "r")
# print(file.read(16))
# print(file.read(4))
# print(file.read(4))
# print(file.read())
# file.close()

file = open("filename.txt", "r")
for i in range(21):
  print(file.read(4))
file.close()