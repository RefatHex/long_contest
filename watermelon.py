def yes_or_no():
    w = int(input()) 
    if 3<=w<=100 and (w-2) % 2 == 0: 
        print('YES') 
    else: 
        print('NO')
if __name__ == "__main__":
    yes_or_no()