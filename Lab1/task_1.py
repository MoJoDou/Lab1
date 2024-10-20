numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
missing_index = numbers.index(None) # находим индекс пропущенного элемента

# создаем срезы до и после пропущенного элемента
before_missing_element = numbers[:missing_index]
after_missing_element = numbers[missing_index+1:]
# суммируем их
sum_numbers = sum(before_missing_element)+sum(after_missing_element)
count = len(numbers)  # расcчитываем длину
# рассчитываем среднее арифметическое
missing_element = sum_numbers / (count)
# делаем замену пропущенного элемента на среднее арифметическое
numbers[missing_index] = missing_element
print("Измененный список:", numbers)

