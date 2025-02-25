# Задачи по программированию

## Line Reflection

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

[Решение на Python]([https://github.com/your-username/my-repo/blob/main/solutions/solution.py](https://github.com/SashaV21/leetcode_algo/blob/main/Line%20Reflection.py))

