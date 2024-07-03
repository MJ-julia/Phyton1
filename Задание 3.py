import requests

response = requests.get('https://fakestoreapi.com/products/categories')
categories = response.json()

print('Доступные категории:')
for category in categories:
    print('- ' + category)

user_category = input('Введите категорию товаров, которую вы хотите просмотреть: ')

response = requests.get(f'https://fakestoreapi.com/products/category/{user_category}')
products = response.json()

print(f'Товары категории "{user_category}":')
for product in products:
    print(f'''
        Название: {product['title']}
        Цена: ${product['price']}
        Описание: {product['description']}
        Рейтинг: {product['rating']['rate']} ({product['rating']['count']} оценок)
    ''')