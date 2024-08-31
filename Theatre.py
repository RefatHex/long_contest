from math import ceil

def theatre():
    n, m, a = map(int, input().split())
    
    tiles_n = ceil(n / a)
    tiles_m = ceil(m / a)
    
    tiles = tiles_n * tiles_m
    
    print(tiles)

if __name__ == "__main__":
    theatre()
