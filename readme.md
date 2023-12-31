# 🔍 Практична робота №6: Про Файли та Олімпіади

## 🎯 **Мета Роботи:**

У рамках цієї практичної роботи основна увага приділяється практичному застосуванню Python для обробки текстових даних.

## 📋 **Загальний Опис:**

Ця практична робота зосереджена на обробці текстових даних за допомогою Python, використовуючи реальні датасети. У
рамках роботи ви працюватимете з файлами, вивчите нові структури даних, такі як словники та множини, та навчитесь
оптимізувати обробку великих обсягів даних.

> [!IMPORTANT]
> У репозиторії проекту вже є файл з даними, `data_source.tsv`, який буде використовуватися для
> виконання завдань. Цей файл містить інформацію про олімпійських атлетів та їхні результати за останні 120 років.
> Формат
> файлу TSV (Tab-Separated Values) є схожим на CSV, але використовує табуляцію як роздільник, що робить його зручним для
> обробки в Python.
>
> Використання цього файлу дозволяє зосередитися на алгоритмічній частині завдання, мінімізуючи необхідність
> самостійного пошуку та підготовки даних.

> [!WARNING]
> Під час роботи над практичним завданням, використовуйте спеціально призначену для цього гілку у репозиторії - `main`.
> Це важливо для забезпечення організованого процесу роботи та ефективного відстеження змін.
> 
> Код практичної роботи розміщуйте в теці [src](./src).

## 🛠️ **Завдання:**

### **Завдання 1: Реалізація команди `-medals`**

Розробіть функціонал для вашої програми, що дозволяє обробляти команду `-medals`. Ця команда використовується для
отримання детальної інформації про медалі, здобуті конкретною країною в певний рік на Олімпійських іграх.

#### **Аргументи Командного Рядка**:

- Шлях до файлу з даними
- `-medals`
- Країну
- Рік, за який потрібно зібрати статистику
- (Опційно) `-output`
- (Опційно) Шлях до файлу для виведення результатів

#### **Приклад Використання**:

- `olympics.py data.csv -medals USA 1996`
- `olympics.py data.csv -medals AUT 1976 -output result.txt`
  <br/>

> [!NOTE]
> Програма повинна обробляти наданий файл, виводячи інформацію про десять перших медалістів з обраної країни для
> заданого року, а також загальну кількість медалей за кожним типом.

### **Завдання 2: Реалізація Команди `-total`**

Розробіть функціонал для вашої програми, що дозволяє обробляти команду `-total`. Ця команда призначена для отримання
загального огляду медалей, здобутих усіма країнами на певній Олімпіаді.

#### **Аргументи Командного Рядка**:

- Шлях до файлу з даними.
- Команду `-total`.
- Рік, за який необхідно зібрати статистику.

#### **Приклад Використання**:

- `olympics.py data.csv -total 1992`
  <br/>

> [!NOTE]
> Після виконання команди `-total`, програма повинна виводити інформацію про всі країни, які здобули медалі на олімпіаді
> вказаного року. Ця інформація має включати загальну кількість золотих, срібних та бронзових медалей для кожної країни.

### **Завдання 3: Реалізація Команди `-overall`**

Розширте функціонал вашої програми, додавши підтримку команди `-overall`. Ця команда призначена для аналізу загальних
результатів кількох країн у різних олімпіадах. Специфікація команди наступна:

#### **Аргументи Командного Рядка**:

- Шлях до файлу з даними.
- Команда `-overall`.
- Список країн, для яких потрібно провести аналіз.

#### **Приклад Використання**:

- `olympics.py data.csv -overall Ukraine Canada Japan`
  <br/>

> [!NOTE]
> Після виконання команди `-overall`, програма повинна виводити рік, в якому кожна з вказаних країн здобула найбільшу
> кількість медалей, та вказувати цю кількість медалей.

### **Завдання 4: Реалізація Команди `-interactive`**

Додайте до вашої програми підтримку нової команди `-interactive`. Ця команда дозволяє користувачу взаємодіяти з
програмою в інтерактивному режимі.

#### **Аргументи Командного Рядка**:

- Шлях до файлу з даними.
- Команда `-interactive`.

#### **Приклад Використання**:

- `olympics.py data.csv -interactive`
  <br/>

> [!NOTE]
> Після активації команди `-interactive`, програма переходить в інтерактивний режим. У цьому режимі користувач може
> вводити назви країн, а програма надає детальну статистику за кожною з введених країн. Це включає інформацію про першу
> участь країни у Олімпійських іграх, її найуспішнішу олімпіаду за кількістю медалей, найменш успішну, а також середню
> кількість медалей кожного типу на кожній олімпіаді.

## **Додаткове Завдання: Реалізація модуля `argparse`**

Для отримання додаткового балу, інтегруйте в вашу програму модуль `argparse`. Це дозволить поліпшити роботу з
аргументами командного рядка.

---

> [!WARNING]
> При використанні цього проекту, будьте уважні до можливості вводу некоректних даних. Це може включати, але не
> обмежується:
>
>   - **Неправильні Назви Країн**: Переконайтеся, що назва країни введена правильно та відповідає даним, що очікуються у
      вашій програмі.
>   - **Некоректні Роки Олімпіад**: Переконайтеся, що введений рік є роком, коли олімпіада дійсно проводилась.

---

## 💡 **Як Виконувати Практичну Роботу**

### Освіження Знань про String Slicing

Перегляньте матеріали про <a href="https://www.freecodecamp.org/news/python-substring-how-to-slice-a-string/">string
slicing</a>, якщо ви не впевнені у своїх знаннях. Це може значно спростити роботу з текстовими даними.

### Читання з Файлу

Ознайомтеся з базовим методом читання з файлу:

```Python
with open(path, 'r') as file:
    lines = file.readlines()
```

> [!NOTE]
> Врахуйте, що цей метод може бути неефективним для великих файлів. Наприклад, наш датасет містить близько 300 тисяч
> рядків і 41 Мб загалом. Читання всіх даних одразу може бути нераціональним.

### Ефективніша Робота з Великими Файлами

Використовуйте метод `file.readline()`, щоб читати файл построково:

```Python
next_line = file.readline()
while next_line:
    # do stuff with line
    next_line = file.readline()
```

### Використання Словників (Dictionaries)

Словники в Python зберігають пари "ключ-значення" і дуже корисні для організації даних.
Приклад словника:

```Python
phone_book = {
    "Ann": "095-150-23-34",
    "Bob": "063-456-12-43",
    "Charlie": "050-123-12-56"
}
```

Використовуйте словники для збереження та обробки даних, наприклад, для накопичення медалей по країнам. Детальніше про
словники можна прочитати [тут](https://www.w3schools.com/python/python_dictionaries.asp)
та [тут](https://www.programiz.com/python-programming/dictionary).

Ці рекомендації допоможуть вам ефективно працювати з текстовими даними та використовувати Python для аналізу та обробки
даних.

## 📝 Контрольні Питання

### **Режими Роботи з Файлами (r, w, a, x, b, t)**:

- 📖 **r**: Читання файлу.
- ✍️ **w**: Запис у файл, стирає попередній вміст.
- 🔄 **a**: Дописування в кінець файлу.
- 🆕 **x**: Створення нового файлу.
- 🖥️ **b**: Бінарний режим.
- 📜 **t**: Текстовий режим.

### **Конструкція `with ... as ...`**:

- 🛠️ Автоматично закриває файл після використання.

### **Різниця між Списком, Таплом, та Множиною**:

- 📋 **Список**: Змінний, індексований.
- 📦 **Тапл (Tuple)**: Незмінний, індексований.
- 🎲 **Множина (Set)**: Неіндексована, унікальні елементи.

### **Аргументи Командного Рядка**:

- ⌨️ Параметри, передані програмі через командний рядок.

### **List Comprehension**:

- 🚀 Короткий спосіб створення списків на основі інших списків або ітерованих об'єктів.

  ```Python
  # Створення списку квадратів чисел від 1 до 5
  squares = [x ** 2 for x in range(1, 6)]

  print(squares)  # Виведе: [1, 4, 9, 16, 25]
  ```

> [!WARNING]
> Наведений список питань є лише прикладом. Можуть бути й інші питання, пов'язані з темою практичної роботи.

## 🌟 Оцінювання Практичної Роботи

Максимальна кількість балів, яку можна отримати за практичну роботу, становить 6, з можливістю отримати додатковий бал:

1. **Завдання 1-4**:
    - 🎯 По одному балу за кожне з чотирьох завдань.

2. **Відповіді на Контрольні Питання**:
    - 📚 1 бал за відповіді на питання під час здачі.

3. **Виконання Практичного Завдання**:
    - 🛠️ 1 бал за демонстрацію виконання практичного завдання під час здачі.

4. **Додатковий Бал за Використання `argparse`**:
    - 🌟 1 додатковий бал за використання модуля `argparse` в роботі.
