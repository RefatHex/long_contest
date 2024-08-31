def hello():
    target = "hello"
    s = input()
    j = 0  
    
    for char in s:
        if char == target[j]:
            j += 1
        if j == len(target):  
            print("YES")
            return
    
    print("NO")

if __name__ == "__main__":
    hello()
