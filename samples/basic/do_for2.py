# 所有的名字，原始数据不可修改
names = (
    ('Apple', 'Google', 'Microsoft'),
    ('Java', 'Python', 'Ruby', 'PHP'),
    ('Adam', 'Bart', 'Lisa')
)

# 寻找的目标值
targets = ('Apple', 'Python', 'PHP', 'Lisa')

# 循环遍历
for x in names:
    for y in x:
        # 不换行输出
        print(y, ", ", end="")
    print()

print('---------------')

# 循环找到的值
locations = []
for t in targets:
    for x in names:
        for y in x:
            # 是否相同，使用逻辑符号is
            if y is t:
                locations.append(y)

print("finds = ", locations)
print('---------------')

# 在两个for循环中输出坐标
locations = []
for t in targets:
    # enumerate(iterable[, start]) -> iterator for index, value of iterable
    for x, l in enumerate(names):
        for y, m in enumerate(l):
            # 是否相同，使用逻辑符号is
            if m is t:
                # 字符串的拼接，使用+号效率会非常低下，使用这种格式化的字符串
                locations.append('%s(%s, %s)' % (m, x, y))
print("locations = ", locations)
print('---------------')
