# Жадібні алгоритми та динамічне програмування

## Завдання:

Маємо набір монет ```[50, 25, 10, 5, 2, 1]```.

Вам необхідно написати дві функції для касової системи, яка видає решту покупцеві:

1. **Функція жадібного алгоритму** ```find_coins_greedy```. Ця функція повинна приймати суму, яку потрібно видати покупцеві, і повертати словник із кількістю монет кожного номіналу, що використовуються для формування цієї суми.
   Наприклад, для суми 113 це буде словник ```{50: 2, 10: 1, 2: 1, 1: 1}```. Алгоритм повинен бути жадібним, тобто спочатку вибирати найбільш доступні номінали монет.

2. **Функція динамічного програмування** ```find_min_coins```. Ця функція також повинна приймати суму для видачі решти, але використовувати метод динамічного програмування, щоб знайти мінімальну кількість монет, необхідних для формування цієї суми. Функція повинна повертати словник із номіналами монет та їх кількістю для досягнення заданої суми найефективнішим способом. Наприклад, для суми 113 це буде словник ```{1: 1, 2: 1, 10: 1, 50: 2}```

Порівняйте ефективність жадібного алгоритму та алгоритму динамічного програмування, базуючись на часі їх виконання або O великому та звертаючи увагу на їхню продуктивність при великих сумах.
Висвітліть, як вони справляються з великими сумами та чому один алгоритм може бути більш ефективним за інший у певних ситуаціях.

## Результати виконання:

```
Greedy Algorithm result: {50: 2, 10: 1, 2: 1, 1: 1}
Dynamic Programming result: {1: 1, 2: 1, 10: 1, 50: 2}

Amount: 200, Greedy Time: 0.000000s, DP Time: 0.000000s
Amount: 580, Greedy Time: 0.000000s, DP Time: 0.000000s
Amount: 1043, Greedy Time: 0.000000s, DP Time: 0.001002s
Amount: 5020, Greedy Time: 0.000000s, DP Time: 0.002001s
Amount: 11321, Greedy Time: 0.000000s, DP Time: 0.005005s
Amount: 50678, Greedy Time: 0.000000s, DP Time: 0.022020s
Amount: 105680, Greedy Time: 0.000000s, DP Time: 0.045845s
```

## Висновки:

Результати показують, що обидва алгоритми працюють дуже швидко для невеликих та помірних сум. Однак важливо враховувати, що жадібний алгоритм, як правило, має часову складність $O(n)$, що є константою в даному випадку.
Тим часом, алгоритм динамічного програмування має квадратичну залежність від суми у своїй часовій складності $O(n^2 \cdot sum)$, що може призводити до значного зростання часу виконання при збільшенні сум.

Час виконання алгоритму динамічного програмування зростає при збільшенні сум, і це природно, оскільки алгоритму потрібно більше часу для обробки більших вхідних даних.

Обидва алгоритми мають свої сильні та слабкі сторони. Жадібний алгоритм простий та швидкий, але не завжди гарантує оптимальний результат. Алгоритм динамічного програмування зазвичай дає оптимальні результати, але може бути більш витратним у відношенні до часу та пам'яті, особливо при великих вхідних даних.