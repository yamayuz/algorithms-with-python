from algorithms.maximum_profit import *
from algorithms.dot_product import *
from algorithms.milestones import *


if __name__ == "__main__":
#     x = [[1, 5, 3],
#          [8, 5, 6]]

#     y = [[1, 2],
#          [9, 4],
#          [5, 1]]
    
#     print(dot_product(x, y))
#     print('-' * 10)
#     print(dot_product_imp(x, y))
            
     sales = [10, 15, 20, 37, 10]
     milestones = [30, 70, 90]

     for idx_sal, elm_sal in enumerate(sales):
          print(idx_sal, elm_sal)

     print(calc_achieve(sales, milestones))
     print(calc_achieve_imp(sales, milestones))