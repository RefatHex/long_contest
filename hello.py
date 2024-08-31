def hello():
    hello="hello"
    s=input()
    last_index=0
    for i in range(len(hello)):
        if hello[i] in s:
            s_index=s.index(hello[i])
            if s_index>last_index:
                print("NO")
                return
            last_index=s.index(hello[i])
    
    print("YES")
    
if __name__ == "__main__":
    hello()
            
        