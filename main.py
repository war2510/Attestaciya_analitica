import pandas as pd
import random

# Создаем исходный DataFrame
lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Преобразуем в one hot кодирование вручную
data["robot"] = (data["whoAmI"] == "robot").astype(int)
data["human"] = (data["whoAmI"] == "human").astype(int)

# Показываем первые десять строк полученного DataFrame
print(data.head(10))