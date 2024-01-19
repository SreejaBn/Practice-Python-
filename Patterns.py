# * * * *
# * * * *
# * * * *
# * * * *

n = 4
for i in range(n):
    for j in range (n):
        print('* ', end="")
    print()

print()


# *
# * *
# * * *
# * * * *
    
for i in range (n):
    for j in range (i+1):
        print ('* ', end='')
    print()
print()


# * * * * 
# * * * 
# * * 
# *

for i in range (n):
    for j in range (n-i):
        print('* ', end='')
    print()
print()


# * * * *
#   * * *
#     * *
#       *

for i in range (n):
    for j in range(i):
        print ("  ", end="")
    for k in range (n-i):
        print ("* ", end='')
    print()
print()


#       *
#     * *
#   * * *
# * * * *

for i in range (n):
    for j in range (n-i):
        print ('  ', end='')
    for k in range (i+1):
        print ("* ", end='')
    print()
print()


#       * * * *
#     * * * *
#   * * * * 
# * * * *
    
for i in range (n):
    for j in range (n-i):
        print ("  ", end='')
    for k in range (n):
        print ("* ", end='')
    print()
print()


#    *  
#   * *  
#  * * *
# * * * *

for i in range (n):
    for j in range (n-i):
        print(" ", end='')
    for k in range (i+1):
        print ("* ", end= "")
    print ()
print()


# * * * *
#  * * *
#   * *
#    *

for i in range (n):
    for j in range (i):
        print (' ', end='')
    for z in range (n-i):
        print('* ', end='')
    print()
print()
    

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5
 
n = 5
for i in range (1,n+1):
    for j in range (1, i+1):
        print (j, end ='')
    print ()
print ()
