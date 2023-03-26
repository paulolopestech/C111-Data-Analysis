loja1 = {
    'Apple iPhone 13',
    'Samsung Galaxy S21',
    'Google Pixel 6',
    'OnePlus 9 Pro',
    'Sony Xperia 1 III',
    'Xiaomi Mi 11',
    'Oppo Find X3 Pro',
    'Asus ROG Phone 5',
}

loja2 = {
    'Huawei P50 Pro',
    'Sony Xperia 1 III',
    'LG Wing 5G',
    'Motorola Edge Plus',
    'Asus ROG Phone 5',
    'Nokia 8.3 5G'
}

print('Todos os modelos disponíveis: ', loja1.union(loja2))

print('Modelos disponíveis em ambas as lojas: ', loja1.intersection(loja2))