def islower(c): #Checks ASCII value of the character is within the lowercase range
    return ord('a') <= ord(c) <= ord('z')

# Test the function
print(islower('a'))  # True
print(islower('Z'))  # False
print(islower('7'))  # False

