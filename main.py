from algorithms.dot_product import dot_product_imp
from algorithms.maximum_profit import *
from algorithms.dot_product import *


if __name__ == "__main__":
    x = [[1, 5, 3],
         [8, 5, 6]]

    y = [[1, 2],
         [9, 4],
         [5, 1]]
    
    print(dot_product(x, y))
    print('-' * 10)
    print(dot_product_imp(x, y))
            

