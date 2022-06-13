# словник для зберігання даних користувачів
phone_book = {}

# декоратор для обробки помилок


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        # якщо команли немає
        except IndexError:
            return 'Error. Try another command.'
        # якщо контакту немає в книзі
        except KeyError:
            return f"Contact {args[0]} does not exist."
    return wrapper
    pass

# привітання


def hello(*args):
    return 'How can I help you?'

# прощання


def exit(*args):
    return "Good bye."

# додавання нового користувача


@input_error
def add(*args):
    name = args[0]
    phone = args[1]
    phone_book[name] = phone
    return f"Contact {name} added succesfully."
    pass

# зміна номера телефону користувача що присутній в книзі


@input_error
def change(*args):
    # ім'я користувача
    name = args[0]
    # номер телефону користувача
    phone = args[1]
    # якщо користувач присутній у книзі - вносимо зміну
    if phone_book[name]:
        phone_book[name] = phone
        return f"Contact {name} changed succesfully."

    pass

# виведення номера телефону


@input_error
def phone(*args):
    # ім'я користувача
    name = args[0]
    # якщо користувач присутній у книзі - виводимо номер
    if phone_book[name]:
        return f"Phone {name}:{phone_book[name]}"
    pass

# виведення книги


def show_all(*args):
    return '\n'.join([f'{key}:{value}' for key, value in phone_book.items()])
    pass


# словник можливих команд користувача
COMMANDS = {
    hello: ['Hello', 'hello', 'hi'],
    exit: ['.', 'exit', 'stop', 'bye', 'close', 'бувай'],
    add: ['add',  '+', 'додай'],
    change: ['change', 'змінити', 'зміни'],
    phone: ['phone', 'номер', 'телефон'],
    show_all: ['show all', 'show']
}

# обробка введеної користувачем команди


def parse_command(user_input: str):
    for key, value in COMMANDS.items():
        for item in value:
            if user_input.lower().startswith(item.lower()):
                return key, user_input[len(item):].strip().split(" ")

    pass

# нескінченний цикл для приймання і обробки команд від користувача


def main():
    while True:
        user_input = input("Type your command here, please: ")
        rezult, data = parse_command(user_input)
        print(rezult(*data))
        # зупинка циклу, якщо введена команда відповідає функції exit
        if rezult is exit:

            break
    pass


if __name__ == '__main__':
    main()
