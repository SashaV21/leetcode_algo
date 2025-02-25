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

## Longest Subarray of 1's After Deleting One Element (Отражение линии)

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



