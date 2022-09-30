str1 = 'abc'
str2 = str1
print(str1 is str2)       # True - это две ссылки на один и тот же объект!
str1 += 'de'              # Теперь переменная str1 ссылается на другой объект!
print(str1 is str2)       # False - теперь это два разных объекта!
print(str1, str2)