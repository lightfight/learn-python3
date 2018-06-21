
# foreach遍历字典

print("------for f in sorted(set(basket))------")

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

print('排序')
basket.sort()
print(basket)

print('另外一种排序')
basket.append('egg')
print(basket)
for f in sorted(set(basket)):
    print(f)

print('一般的平方')
squares = []
for x in range(10):
    squares.append(x**2)
print(squares)

print('lambda平方')
squares = [x**2 for x in range(10)]
print(squares)


def my_function():
    """
        Do nothing, but document it.

        No, really, it doesn't do anything.
    """


print(my_function.__doc__)
print(range.__doc__)





