#импортируем библиотеки нумпаи и пандас
import pandas as pd
import numpy as np        

#создаем таблицу умножения
lst = dict()
for i in range(1, 10):
    lst.update({i: [i*j for j in range(1, 10)]})
tabl_umn = pd.DataFrame(lst, index=np.arange(1, 10))

#создаем таблицу сложения
lst2 = dict()
for i in range(1, 10):
    lst2.update({i: [i+j for j in range(1, 10)]})
tabl_slozh = pd.DataFrame(lst2, index=np.arange(1, 10))

#выводим таблицы
print(f"Таблица умножения \n{tabl_umn}\n")
print(f"Таблица сложения \n{tabl_slozh}")
