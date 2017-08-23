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

#1.5一个优先队列
# import heapq
#
# class PriorityQueue:
#     def __init__(self):
#         self._queue = []
#         self._index = 0
#
#     def push(self, item, priority):
#         heapq.heappush(self._queue, (-int(priority), self._index, item))
#         self._index +=1
#
#     def pop(self):
#         return  heapq.heappop(self._queue)[-1]
#
# class Item:
#      def __init__(self, name):
#          self.name = name
#      def __repr__(self):
#          return 'Item({!r})'.format(self.name)
#
# q = PriorityQueue()
# q.push(Item('foo'), 1)
# q.push(Item('bar'), 5)
# print(q.pop())

#1.6 字典中映射多个值
# from collections import defaultdict
#
# d = defaultdict(list)
# d['a'].append(1)
# d['a'].append(2)
# d['b'].append(1)
# for key in d:
#     print(key, d[key])
# print(d)
# d = defaultdict(set)
# d['a'].add(1)
# d['a'].add(2)
# d['b'].add(1)
# print(d)
# d = {}
# d.setdefault('a', []).append(1)
# d.setdefault('a', []).append(2)
# d.setdefault('b', []).append(4)
# print(d)

# 1.7 字典排序
# from collections import OrderedDict
#
# d = OrderedDict()
# d['foo'] = 1
# d['bar'] = 2
# d['add'] = 3
# for key in d:
#     print(key, d[key])

#1.8 字典运算
# prices = { 'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75 }
# min_price = min(zip(prices.values(), prices.keys()))
# max_price = max(zip(prices.values(), prices.keys()))
# prices_sort = sorted(zip(prices.values(), prices.keys()), reverse=True)
# print(max(prices_sort))
# print(min(prices_sort))
#zip是迭代器只能访问一次，可以对zip进行排序后，在进行操作

#1.9  查找两个字典的相同点
# a = { 'x' : 1, 'y' : 2, 'z' : 3 }
# b = { 'w' : 10, 'x' : 11, 'y' : 2 }
# print(a.keys() & b.keys())
# print(a.items() & b.items())
# c = {key:a[key] for key in a.keys() - {'z', 'b'}}
# print(c)

#1.10 删除元素并保持顺序
# def dedupe(items):
#     seen = set()
#     for item in items:
#         if item not in seen:
#             yield item
#             seen.add(item)
# #list append set add, set 有序，
# a= [1, 5, 3, 4, 6, 7, 7, 4, 5]
# print(list(dedupe(a)))

# def deque(items, key=None):
#     seen = set()
#     for item in items:
#         val = item if key is None else key(item)
#         if val not in seen:
#             yield item
#             seen.add(val)
# a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
# # print(list(deque(a, key=lambda d: (d['x'], d['y']))))
# # print(list(deque(a, key=lambda d:d['x'])))
# print(list(deque(a, key=lambda d:d['y'])))
