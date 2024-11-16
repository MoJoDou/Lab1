# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, separator=","):
    first_group = set(participants_first_group.split(separator))
    second_group = set(participants_second_group.split(separator))
    common_participants = sorted(first_group & second_group)
    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common = find_common_participants(participants_first_group, participants_second_group, separator="|")
print(common)