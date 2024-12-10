import time

from data_analysis.service.realtime_data_loader import RealtimeMonitoringService

service = RealtimeMonitoringService(1, [], 1000, 'configs/logging.conf')
service.start()

print("Введите сообщение (для выхода введите 'exit' или 'quit'):")

while True:
    cities= {'vancouver': [49.2497, -123.1193], 'chicago': [41.85, 87.65], 'argentina': [3.1412, 101.687]}
    # Читаем сообщение от пользователя
    message = input()
    # Проверяем, не ввел ли пользователь команду для выхода
    if message.lower() in ['exit', 'quit']:
        print("Спасибо за использование программы. До свидания!")
        service.stop()
        break
    if message.lower() in cities:
        print(f"Получено сообщение: {cities[message.lower()]}")
        service.set_coords(cities[message.lower()])
    # Выводим сообщение на экран
    print(f"Получено сообщение: {message}")