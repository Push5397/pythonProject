# # def greet():
# #     print("Hello")
# #     print("Good")
# #     print("Morning")
# #
# # greet()
#
#
#
#
#
#
#
#
#
# # num = int(input("Enter a number : "))
# # a = 0
# # b=1
# # count =0
# # while count<num:
# #     print(a)
# #     n=a+b
# #     a=b
# #     b=n
# #     count=count+1
#
#
# # Palindrom
#
#
# # num = int(input())
# # n= num
# # rev =0
# # while num>0:
# #     rem = num%10
# #     rev = rev*10 + rem
# #     num = int(num/10)
# # print(rev)
# #
# # if rev==n:
# #     print("palindrome")
# # else:
# #     print("Not palindrome")
#
#
#
#
#String palindrom
# # text = input("Enter name ")
# # txt_rev = ""
# # for char in text:
# #     txt_rev = char+txt_rev
# # print(txt_rev)
# #
# # if(text==txt_rev):
# #     print("palindrome")
# # else:
# #     print("not palindrome")
#
#
# # nameList = ["A","B","C","D"]
# # nameSearch = input("Enter name: ")
# # flag = False
# # i = 0
# # while i <len(nameList) and flag == False:
# #     if nameSearch == nameList[i]:
# #         print(f"{nameSearch} exist in the array.")
# #         flag = True
# #         break
# #     else:
# #         i = i+1
# #         print(f"{nameSearch} does not exists in the array")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# nameList = ["A","B","C","D"]
# nameSearch = input("Enter name: ")
# flag = False
# i = 0
# while i <len(nameList):
#     if nameSearch == nameList[i]:
#         flag = True
#         break
#     else:
#         i = i +1
#
# if flag == True:
#     print(f"found at position {i+1}")
# else:
#     print("Not found")
#
#
#
# nameList = ["A","B","C","D"]
# nameSearch = input("Enter name: ")
#
# if nameSearch in nameList:
#     index = nameList.index(nameSearch)
#     print(f"Found at position {index+1}")
# else:
#     print("Not Found")


# def func1 (name, location):
#     print(f"Hello {name}")
#     print(f"what is it like in {location}")
#
# func1(location = "mumbai", name = "Push")


# def calculate_love_score(name1,name2):
#     name = (name1+name2).lower()
#     T = name.count("t")
#     R = name.count("r")
#     U = name.count("u")
#     E = name.count("e")
#     score1 = T+R+U+E
#
#     L = name.count("l")
#     O = name.count("o")
#     V = name.count("v")
#     E = name.count("e")
#     score2 = L+O+V+E
#     score = str(score1) + str(score2)
#     print(score)
#
# calculate_love_score("KANYE west","kim kardashian")

# Learning functions