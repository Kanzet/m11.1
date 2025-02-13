import pandas as pd

data = {
    'Имя': ['Алексей', 'Мария', 'Дмитрий', 'Анна'],
    'Возраст': [25, 30, 22, 28],
    'Город': ['Москва', 'Санкт-Петербург', 'Казань', 'Екатеринбург']
}

df = pd.DataFrame(data)

print("Исходный DataFrame:")
print(df)

df['Зарплата'] = [50000, 60000, 45000, 55000]

фильтрованный_df = df[df['Возраст'] > 25]

print("\nОтфильтрованный DataFrame (возраст > 25):")
print(фильтрованный_df)

средняя_зарплата = df['Зарплата'].mean()
print("\nСредняя зарплата:", средняя_зарплата)
