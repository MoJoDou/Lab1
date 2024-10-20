# TODO Найдите количество книг, которое можно разместить на дискете

size = 1.44  # информационный объем дискета в мб
page = 100  # количество страниц в книге
lines = 50  # число строк на странице
symbols = 25  # количество символов в строке
bytes_number = 4  # количество байтов

total_size_book = page * lines * symbols # рассчитываем общий размер книги
bytes_size_in_book = total_size_book * bytes_number  # узнав общий размер книги переводим в байтах

bytes_size_disk = size * 1024 * 1024 # здесь переводим объём дискета в байтах

numbers_books = bytes_size_disk // bytes_size_in_book # рассчитываем количество книг
print("Количество книг, помещающихся на дискету:", round(numbers_books))
