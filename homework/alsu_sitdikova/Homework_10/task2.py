"""
Задание на декораторы 2
Создайте универсальный декоратор, который будет управлять тем, сколько раз запускается декорируемая функция

Код, использующий этот декоратор может выглядеть, например, так:

@repeat_me
def example(text):
    print(text)

example('print me', count=2)
В результате работы будет такое:

print me

print me

Если есть время и желание погуглить и повозиться, то можно попробовать создать декоратор, который сможет обработать такой код:

@repeat_me(count=2)
def example(text):
    print(text)

example('print me')
"""


def repeat_me(count):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)
            return func
        return wrapper
    return decorator


@repeat_me(count=6)
def example(text):
    print(text)


example('print me')
