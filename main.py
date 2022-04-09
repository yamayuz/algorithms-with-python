from algorithms.maximum_profit import *


if __name__ == "__main__":
    input = [6, 5, 3, 1, 3, 4, 3]
    # input = [3, 4, 3, 2]
    
    print(f'O(n**2): {maximum_profit_n2(input)}')
    print(f'O(n)   : {maximum_profit_n(input)}')
    

