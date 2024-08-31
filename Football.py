def team():
    binary = input()
    binary_arr = binary.strip()
    arr_size = len(binary_arr)
    
    if arr_size <= 100:
        count = 0
        for i in binary_arr:
            if i == '1':
                count += 1
                if count >= 7:
                    print('YES')
                    return
            else:
                count = 0
        
        count = 0
        for i in binary_arr:
            if i == '0':
                count += 1
                if count >= 7:
                    print('YES')
                    return
            else:
                count = 0


    print('NO')

if __name__ == "__main__":
    team()
