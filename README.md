# **Завдання 1: Застосування алгоритму максимального потоку для логістики товарів**  

## **Опис моделі логістичної мережі**  
Для розрахунку максимального потоку ми побудували граф, що моделює логістичну мережу транспортування товарів від терміналів до складів, а потім до магазинів. Граф складається з:

- **Вершин (20 точок):**
  - **2 термінали (T1, T2)** – джерела товарів
  - **4 склади (S1, S2, S3, S4)** – проміжні точки розподілу
  - **14 магазинів (M1-M14)** – кінцеві точки постачання
  - **Додаткові вершини**: штучне **джерело (super_source)** та **сток (super_sink)** для зручності розрахунків

- **Ребра з пропускною здатністю:**
  - Від терміналів до складів
  - Від складів до магазинів
  - Від магазинів до стоку (super_sink), що означає завершення ланцюга постачання

## **Реалізація алгоритму Едмондса-Карпа**
Для обчислення максимального потоку використано **алгоритм Едмондса-Карпа**, який є варіацією алгоритму Форда-Фалкерсона з використанням BFS для знаходження найкоротшого аугментуючого шляху.

Кроки алгоритму:
1. Ініціалізація потоку в усіх ребрах як 0.
2. Виконання BFS для пошуку збільшувального шляху від `super_source` до `super_sink`.
3. Визначення мінімальної пропускної здатності уздовж знайденого шляху.
4. Оновлення потоку у відповідних ребрах.
5. Повторення кроків 2-4, поки BFS знаходить шлях.

## **Результати обчислень**
### **Максимальний потік: 115 одиниць**

**Розподіл потоків між вершинами:**
```
super_source -> T1: 60
super_source -> T2: 55
T1 -> S1: 25
T1 -> S2: 20
T1 -> S3: 15
T2 -> S3: 15
T2 -> S4: 30
T2 -> S2: 10
S1 -> M1: 15
S1 -> M2: 10
S2 -> M4: 15
S2 -> M5: 10
S2 -> M6: 5
S3 -> M7: 20
S3 -> M8: 10
S4 -> M10: 20
S4 -> M11: 10
M1 -> super_sink: 15
M2 -> super_sink: 10
M4 -> super_sink: 15
M5 -> super_sink: 10
M6 -> super_sink: 5
M7 -> super_sink: 20
M8 -> super_sink: 10
M10 -> super_sink: 20
M11 -> super_sink: 10
```

## **Аналіз результатів**
1. **Які термінали забезпечують найбільший потік товарів до магазинів?**
   - `T1` передав **60 одиниць** товарів
   - `T2` передав **55 одиниць** товарів
   - **Висновок**: Обидва термінали мають приблизно однакове навантаження, але `T1` трохи ефективніший.

2. **Які маршрути мають найменшу пропускну здатність?**
   - `S2 -> M6` (5 одиниць)
   - `S3 -> M8` (10 одиниць)
   - `S2 -> M5` (10 одиниць)
   - **Вплив**: Через обмежену пропускну здатність цих маршрутів деякі магазини отримують недостатньо товарів.

3. **Які магазини отримали найменше товарів?**
   - `M6` отримав **5 одиниць**
   - `M8` отримав **10 одиниць**
   - **Можливе покращення**: Якщо збільшити потік між `S2` та `M6`, то магазин `M6` отримає більше товарів.

4. **Чи є вузькі місця в мережі?**
   - Так, основні обмеження на маршрутах `S2 -> M6`, `S3 -> M8` та `S2 -> M5`.
   - **Як покращити?**
     - Збільшити пропускну здатність цих шляхів.
     - Додати додаткові маршрути між складами та магазинами.

## **Висновки**
- Алгоритм Едмондса-Карпа показав, що **максимальний можливий потік — 115 одиниць**.
- Основні вузькі місця знаходяться на маршрутах з `S2` та `S3` до магазинів.
- Для покращення логістичної мережі варто збільшити пропускну здатність слабких маршрутів.

---

# **Завдання 2: Порівняння ефективності OOBTree і Dict для діапазонних запитів**

## **Порівняльний аналіз OOBTree та dict**
Ми протестували дві структури для зберігання товарів:
- **OOBTree (з BTrees.OOBTree)** – збалансоване дерево B-типу, ефективне для діапазонних запитів.
- **Dict (звичайний Python-словник)** – не має вбудованої підтримки діапазонних запитів, тому використано лінійний пошук.

**Метод тестування:**
- Виконано **100 запитів** на пошук товарів у певному діапазоні цін.
- Виміряно загальний час виконання для кожної структури.

### **Результати тестування:**
```
Total range_query time for OOBTree: 0.000031 seconds
Total range_query time for Dict: 0.000029 seconds
```

### **Висновки**
1. **OOBTree не показав значної переваги** у порівнянні з `dict`.
2. **Можливі причини такого результату:**
   - Малий обсяг тестових даних.
   - OOBTree показує перевагу на **дуже великих обсягах даних (100 000+ записів)**.

## **Загальний висновок**
- У невеликих обсягах даних `dict` і `OOBTree` працюють однаково швидко.
- OOBTree буде ефективнішим для **великого** обсягу товарних записів.
- Логістична мережа має вузькі місця, які можна усунути для покращення постачання товарів.

