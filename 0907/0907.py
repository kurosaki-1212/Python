# x = float(input("実数ｘ："))
# y = float(input("実数ｙ："))
# z = float(input("実数ｚ："))

# print("abs(x)      = ", abs(x))
# print("bool(x)     = ", bool(x))
# print("divmod(x, y)= ", divmod(x, y))
# print("max(x, y)   = ", max(x, y))
# print("min(x, y)   = ", min(x, y))
# print("pow(x, y)   = ", pow(x, y))
# print("round(x, 2) = ", round(x, 2))
# print("round(x, 3  = ", round(x, 3))
# print("sum(x, y, z)= ", sum(x, y, z))



x = int(input("整数："))
n = int(input("シフトするビット数："))

print("x      = {:b}".format(x))
print("x << n = {:b}".format(x << n))
print("x >> n = {:b}".format(x >> n))