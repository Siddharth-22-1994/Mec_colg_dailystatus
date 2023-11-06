
# -------------------------> Day:1 <--------------------------
# ways to define variables

# a = 8
# print(a)

# a = 8
# print(type(a))


# a = 8
# b =9
# print(a)
# print(b)

# j =67
# print(id(j)) # memory address of the variable

# a= 7, 8
# print(a)
# print(type(a))

# a = 7
# b = 7
# a=b=7
# print(a, b)

# a, b =3, 4
# print(b)
# print(a)

# a, b = 8
# print(a, b) # error

# a, b =c=7, 8
# print(a)
# print(b)
# print(c)

# a=b, c = 7,8
# print(a, b, c)

# a = 8, 9, 7, 9.8, "hello", [1,2,3]
# print(a)
   
# list()
# int()
# def calcaulator(c):
#     if c==1:
#         def sum(a, b):
#             print(a+b)
#         sum(2, 3)
        
#     if c==2:        
#         def sub(a, b):
#             print(a-b)
#         sub(4, 5)
        
#     if c==3:        
#         def mul(a, b):
#             print(a*b)
#         mul(6, 7)
# n = int(input("Enter the number: "))
# calcaulator(n)

# a = 7
# b = 10
# # print(a+b)
# print(a.__add__(b))

# class student2:
#     name= "sid"
#     age = 28
#     place = "cbe"
    
#     def display(self):
#         print(self.name, self.age, self.place)
# # print(student.name, student.age, student.place)
# # student.display()

# obj = student2()
# # print(obj.name, obj.age, obj.place)
# obj.display()


# class c1:
#     # def __init__(self, a, b):
#     # a = int(input())
#     # b = int(input())
    
#     a = 0
#     b = 0
#     def __init__(self, a1, b1):
#         self.a= a1
#         self.b=b1
#         return self.a, self.b
           
#     def add(self):
#         print(self.a+self.b)
            
#     def sub(self):
#         print(self.a-self.b)
        
# obj =c1(3, 4)
# obj.add()
# obj.sub()


# operator = "-"
# if operator=="+":
#     obj.add()
# elif operator=="-":
#     obj.sub()
    
    

# class profile:
#     def __init__(self, name, age):
#         print(name, age)
        
#     def display():
#         pass
        
# p = profile("sid", 28)


# ! Depth First Search
# ? def
# DFS --> Depth first search algorithm is a popular 
# graph traversal algorithm
# DFS begins by looking at the root 
# node based on random shoice

# Uses
# 1.) To find the path between 2 vertices
# 2.)Used to dtect the cycles of the graph
# 3.)To determine a graph is bipartite or not

# To form of representation 
# 1.) Adjacency list
# 2.) Matrix format

# Eg:1
# A-> B
# A-> C
# B-> C
# c-> D

# graph ={
#     "A":["B", "C"],
#     "B":["C"],
#     "C":["D"]
# }

# ! Eg:2
# A -> B
# A -> C
# B -> E
# E -> I
# C -> F
# C -> G
# F -> J
# A -> D
# D -> H

graph = {"A":["D", "C", "B"],
         "B":["E"],
         "C":["F", "G"],
         "D":["H"],
         "E":["I"],
         "F":['J']}

def dfs(graph, source):
    if source is None or source not in graph:
        return "Invalid input"
    path = []
    stack = [source]
    while (len(stack) !=0):
        s = stack.pop()
        if s not in path:
            path.append(s)
        if s not in graph:
            continue
        for neighbours in graph[s]:
            stack.append(neighbours)
    return " ".join(path)
print(dfs(graph, "A"))
    
    
# l1 = [1,2,3,4]
# num =3
# # membership operator ---> in , not in
# print(num not in l1)

# Identity operator # is used to find the values store in same
# memory location

# is, is not
# a = [1,2,3]
# b = [1,2,3]
# print(a is b)
# print(a==b)

# d1 = {"milk":100, "Tea":20, "shirt":250}
# for userdefined_variable in range(start, stop, step):
#     statement

# for i in d1:
#     d1[i]=d1[i]*0.012
# print(d1)


# d1["milk"] = 687
# print(d1)

# l1 = ["hello","There",3,4,5]
# for i in range(0, len(l1)):
#     print(l1[i])
    
# Convert iot to dollar
# 0.012


# int a = 78
# int *p;
# p = &a;
# printf("%p", p)
# --------------------------------> Day:1 end <----------------------------------