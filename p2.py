s1 = ["Вася", "Петя", "Игорь", "Дима"]
s2 = [20, 300, 50, 100]
s3 = ["10.25%", "12.5%", "10.0%", "40.3%"]

import re

result = {s1[i]: s2[i] + s2[i]*float(re.sub("[^0-9. ]", "", s3[i]))/100 for i in range(0, len(s1))}
print(result)