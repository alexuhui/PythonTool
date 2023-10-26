import re

# 正则表达式测试

str = r"test c 33.txt"

p = r"(test)\s+c\s+(\d+)"
pattern = re.compile(p)

print(re.compile(pattern).match(str))

print(pattern.match(str))

print(re.sub(p, r"\1\2", str))