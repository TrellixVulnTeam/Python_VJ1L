
message = "hello"
print(message)

msg = "hEhh'hel'g3wgg"
print(msg)

# 按照标题栏
print(msg.title())
# 大写
print(msg.upper())
# 小写
print(msg.lower())

# 合并字符串
print(message + " " + msg)

# 制表符添加空白
msg1 = "I like\t Python"
print(msg1)

# 换行符
msg2 = "I love\nPython"
print(msg2)

# 删除空白
msg3 = "  I love Python    "
print(msg3.strip())
print(msg3.lstrip())
print(msg3.rstrip())

# 运算
msg4 = 2 + 2 * 5
print(msg4)

# 乘方
msg5 = 4 ** 3
print(msg5)

msg5 = 3 / 2
print(msg5)

print(0.1 + 0.2)

# str 将非字符转为字符
msg5 = "happy " + str(msg4) + " birthday"
print(msg5)

