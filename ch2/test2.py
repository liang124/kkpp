
paragraph = '''
Most discussions of GraphQL focus on data fetching, but any complete data platform needs a way to modify server-side data as well.
In REST, any request might end up causing some side-effects on the server, but by convention it's suggested that one doesn't use GET requests to modify data. GraphQL is similar - technically any query could be implemented to cause a data write. However, it's useful to establish a convention that any operations that cause writes should be sent explicitly via a mutation.
Just like in queries, if the mutation field returns an object type, you can ask for nested fields. This can be useful for fetching the new state of an object after an update.
'''

p1 = "Most discussions of GraphQL focus on data fetching, but any complete data platform needs a way to modify server-side data as well." \
"In REST, any request might end up causing some side-effects on the server, but by convention it's suggested that one doesn't use GET requests to modify data. GraphQL is similar - technically any query could be implemented to cause a data write. However, it's useful to establish a convention that any operations that cause writes should be sent explicitly via a mutation." \
"Just like in queries, if the mutation field returns an object type, you can ask for nested fields. This can be useful for fetching the new state of an object after an update."


# Q1: 印出這個段落的長度


# Q2: 把文章裡 'GraphQL' 這個單字變全大寫, 其餘單字變全小寫
# 解法：先全部轉小寫，在把GraphQL 這個單字轉大寫
p2 = p1.lower()
p3 = p2.replace('graphql','GRAPHQL')
print(p3)

# Q3: 印出這個段落有多少個英文單字(不含標點符號與空白)
#1.用split 去掉空白 2.用len算字數
p1List = p1.split()
print("文章單字(word)數：" + str(len(p1List)))

# Q4: x = 2, y = 6, 把兩個變數的值交換, 讓他變成 x = 6, y = 2, 只能使用加減乘除, 不能使用第三個變數, 不能使用常數
#解1 
x = 2
y = 6
x,y = y,x
#print("X="+ str(x),"Y="+ str(y))
print("X = %d , Y = %d " %(x,y))

