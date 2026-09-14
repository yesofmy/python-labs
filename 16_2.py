'''Продемонструвати використання декоратора для функції. Функцію створюєте відповідно до завдання самі, але щоб підходила для обгортки заданим декоратором.
Розробіть декоратор, який вимірює кількість використаної оперативної пам'яті під час виконання функції.'''

import psutil
import time

def memory_usage_decorator(func):
    def wrapper(*args, **kwargs):
        process = psutil.Process()
        start_mem = process.memory_info().rss / 1024 / 1024
        print(f"Memory before execution: {start_mem:.2f} MB")
        
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        end_mem = process.memory_info().rss / 1024 / 1024
        print(f"Memory after execution: {end_mem:.2f} MB")
        
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        print(f"Memory used: {end_mem - start_mem:.2f} MB")
        
        return result
    return wrapper

@memory_usage_decorator
def create_large_list(n):
    """Функція для створення великого списку"""
    large_list = [i for i in range(n)]
    return large_list

result = create_large_list(10)