import pandas as pd,numpy as np


array_list=list(map(int,input().split()))


# print(array_list)


def shifting_the_zeros_towards_right(array):
	answer=[  nonzeros   for nonzeros in array if nonzeros!=0]  +   [     zeros   for zeros in array if zeros ==0]
	return answer














print(shifting_the_zeros_towards_right(array_list))