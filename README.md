# Задачи по программированию

## Line Reflection (Отражение линии)

**Сложность:** Medium

**Условие задачи:** 

Given n points on a 2D plane, find if there is such a line parallel to the y-axis that reflects the given points symmetrically.
In other words, answer whether or not if there exists a line that after reflecting all points over the given line, the original points' set is the same as the reflected ones.

Даны n точек на двумерной плоскости. Найдите, существует ли такая прямая, параллельная оси Y, которая симметрично отражает заданные точки.
Другими словами, ответьте, существует ли такая прямая, что после отражения всех точек относительно этой прямой исходный набор точек будет таким же, как и отражённый.

**Описание алгоритма:**

1.  Находим минимум и максимум по x
2.  Создаем set() координат точек, для быстрого поиска
3.  Проходим по всем парам точек, добавляем в set()
4.  Находим сумму максимальной точки и минимальной. Это будет удвоенная координата оси симметрии по X
5.  Далее проверяем для каждой точки, найдется ли в множестве точка отраженная ей, если все точки можно отразить - возвращаем True. `all((s - x, y) in point_set for x, y in points)`

**Реализация:**
[Решение на Python](https://github.com/SashaV21/leetcode_algo/blob/main/Line%20Reflection.py)

## Longest Subarray of 1's After Deleting One Element (Наибольшая подстрока из единиц после удаления одного элемента)

**Сложность:** Medium
**Подсказка:** Два указателя

**Условие задачи:** 

Given a binary array nums, you should delete one element from it. Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Учитывая двоичный массив nums, вы должны удалить из него один элемент. Верните размер самого длинного непустого подмассива, содержащего только 1's в результирующем массиве. Верните 0, если такого подмассива нет.

**Описание алгоритма:**

1.  Проходим правым указателям по значениям, если встретили `0`, то увеличиваем счетчик `zeroes`.
2.  Пока количество нулей будет больше 1, мы сдвигаем левый указатель и если `nums[l] == 0`, то уменьшаем счетчик
3.  Каждый раз обновляем `ans`. Длина нужной нам последовательности - `r - l + 1 - zeroes`
4.  Возвращаем результат

**Реализация:**
[Решение на Python](https://github.com/SashaV21/leetcode_algo/blob/main/Longest%20Subarry%20of%201's%20After%20deleting%20one%20element.py)


## Summary Ranges (Сводные диапазоны)

**Сложность:** Easy

**Условие задачи:** 

You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:
"a->b" if a != b
"a" if a == b

Вам предоставляется отсортированный уникальный целочисленный массив nums.
Диапазон [a,b] — это множество всех целых чисел от a до b (включительно).
Возвращает наименьший отсортированный список диапазонов, которые точно охватывают все числа в массиве. То есть каждый элемент nums покрывается ровно одним из диапазонов, и не существует целого числа, x такого, x которое находится в одном из диапазонов, но не в nums.
Каждый диапазон [a,b] в списке должен быть выведен в виде:
"a->b" если a != b
"a" если a == b
**Описание алгоритма:**

1.  Проходим правым указателям по значениям, если встретили `0`, то увеличиваем счетчик `zeroes`.
2.  Пока количество нулей будет больше 1, мы сдвигаем левый указатель и если `nums[l] == 0`, то уменьшаем счетчик
3.  Каждый раз обновляем `ans`. Длина нужной нам последовательности - `r - l + 1 - zeroes`
4.  Возвращаем результат

**Реализация:**
[Решение на Python](https://github.com/SashaV21/leetcode_algo/blob/main/Longest%20Subarry%20of%201's%20After%20deleting%20one%20element.py)




