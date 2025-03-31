# Ми маємо сейф, який можна розблокувати чотиризначним PIN-кодом (від 0000 до 9999). Під дисплеєм знаходяться
# деякі кнопки з числами від 1 до 9999 (наприклад: 13, 223, 782, 3902). Цей сейф працює по-іншому, ніж звичайний.
# Натискання кнопки з числом додає число з кнопки до числа на дисплеї. Якщо сума перевищує 9999, перша цифра
# відкидається. Ми знаємо PIN-код та числа, які відображаються на дисплеї. Знайдіть найкоротшу послідовність
# натискань кнопок, що дозволить нам розблокувати сейф. Якщо така послідовність не існує, поверніть None.

from queue import Queue

def safe(buttons, display, PIN):
    n = len(buttons)
    queue = Queue()
    visited = [False for _ in range(10000)]
    queue.put((display, []))
    visited[display] = True

    while not queue.empty():
        current_display, sequence = queue.get()

        if current_display == PIN:
            return sequence

        for button in buttons:
            new_display = (current_display + button) % 10000

            if not visited[new_display]:
                visited[new_display] = True
                new_sequence = sequence + [button]
                queue.put((new_display, new_sequence))

    return None


display = 1234
PIN = 7384
buttons = [13, 223, 782, 3902, 500]
print(safe(buttons, display, PIN))