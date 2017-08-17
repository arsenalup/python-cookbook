# from collections import deque
#
#
# def search(lines, pattern, history):
#     previous_lines = deque(maxlen=history)
#     for i in lines:
#         if pattern in li:
#             yield li, previous_lines
#         previous_lines.append(li)

#查找最大最小的n个元素
# import heapq
# nums = [1,2,3,4,5,6,7]
# print(heapq.nlargest(3, nums))
# print(heapq.nsmallest(3, nums))

# portfolio = [ {'name': 'IBM', 'shares': 100, 'price': 91.1},
#               {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#               {'name': 'FB', 'shares': 200, 'price': 21.09},
#               {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#               {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#               {'name': 'ACME', 'shares': 75, 'price': 115.65}
#               ]
# cheap = heapq.nsmallest(3, portfolio, lambda s : s['price'])
# # print(cheap)
# expensive = heapq.nlargest(3, portfolio, lambda s : s['price'])
# heapq.heapify(nums)
# print(heapq.heappop(nums))
