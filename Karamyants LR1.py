# 1. Генерация списка с использованием цикла while
result = [] #Создаем пустой список
i = 0
while i < 16: 
    result.append(i) #Добавляем значения в список
    i += 1 #Увеличиваем переменную i на каждой итерации
print("Сгенерированный список:", result)

# 2. Создание множества с использованием цикла while и break
set_result = set() #Создаем пустое множество с помощью функции set
for num in result: 
    if num > 10:
        break #при достижении значения больше 10 используем оператор break чтобы прервать цикл
    set_result.add(num) #добавляем значения из списка во множество
print("Множество значений до 10:", set_result)

# 3. Удаление значений из списка с использованием цикла while
i = 0
while i < len(result): #используем len для нахождения длины списка
    if result[i] < 11:
        result.pop(i) #c помощью pop удаляем элемент
    else:
        i += 1 #увеличиваем значение на 1
print("Список после удаления значений меньше 11:", result)

# 4. Модификация списка и добавление элементов кортежа в обратном порядке
for i in range(len(result)): #используем len для нахождения длины списка
    if result[i] >= 50: #если элемент больше или равен 50
        result[i] = (result[i] + 39,) #заменяем его на кортеж увеличенный на 39
    else: #если условие не выполняется
        result[i] = (result[i] * 3,) #заменяем его на кортеж увеличенный в 3 раза
result.extend(tuple(result[::-1])) #c помощью extend добавляем кортеж в обратном порядке
print("Список с добавленными элементами кортежа:", result)

# 5. Функция для расчета площадей, фильтрации и вычисления результата
import math #импортируем модуль math чтобы использовать математические функции

def calculate_circle_area(length_list, width_list): #функция которая принимает два списка
    areas = [] #создаем пустой список куда будем записывать площади
    for length, width in zip(length_list, width_list): #перебираем значения списков с помощью цикла for
        radius = math.sqrt((length/2)**2 + (width/2)**2) #находим радиус круга из сторон прямоугольника
        area = math.pi * radius**2 #находим площадь круга
        areas.append(area) #добавляем значения площадей в список
    average_area = sum(areas) / len(areas) #считаем среднюю площадь кругов как сумму всех площадей, деленную на количество площадей
    filtered_areas = list(filter(lambda x: x <= 0.9 * average_area, areas)) #используем функцию filter для фильтрации значений в списке areas
    product = 1
    for num in filtered_areas:
        product *= num #перемножаем все значения в отфильтрованном списке
    result = product / len(length_list) #делим это произведение на длину входного списка
    return result #выходим из функции

length_list = [4, 6, 3, 5]
width_list = [3, 5, 2, 4]
answer = calculate_circle_area(length_list, width_list) #передаем в функцию списки
print(answer) #выводим результат


# 6. Функция для генерации списка, фильтрации и обработки
def generate_and_process(min_val, max_val, step): #создаем функцию которая принимает два значения и шаг
    numbers = list(range(min_val, max_val, step)) #создаем список чисел с заданным диапозоном и шагом
    divisible_by_7 = len(list(filter(lambda x: x % 7 == 0, numbers))) #находим количество чисел кратных 7 c помощью filter
    median = sorted(numbers)[len(numbers) // 2] #находим их медиану
    result = divisible_by_7 - median #вычисляем разность
    if result < 0: #если разность отрицательна
        return numbers[::-1] #возвращаем список, отраженный в обратном порядке
    else: #если уловие не выполнилось
        new_list = numbers.copy() #создаем копию
        new_list.insert(0, result) #с помощью insert помещаем число в начало списка
        return new_list #возвращаем скопированный список

final_result = generate_and_process(5, 35, 3) #передаем в ыункцию значения
print("Итоговый список:", final_result) #выводим результат

# 7. Функция поиска и замены
def find_and_replace(input_string, search_str, replace_str): #создаем функцию которая принимает исходную строку, часть строки для замены и то, на что нужно заменить
    return input_string.replace(search_str, replace_str) #пользуем метод replace для замены указанной части строки на указанное значение

original_string = "Роналду лучший футболист мира"
new_string = find_and_replace(original_string, "Роналду", "Месси")
print("Измененная строка:", new_string)
