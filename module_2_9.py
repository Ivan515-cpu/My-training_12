def send_email(message, recipient, *, sender="university.help@gmail.com"):
    valid_domains = [".com", ".ru", ".net"] # Список допустимых доменов

    if "@" not in sender or "@" not in recipient or not any(
            recipient.endswith(domain) for domain in valid_domains) or not any(
            sender.endswith(domain) for domain in valid_domains):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return  # Проверка корректности e-mail адресов

    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return  # Проверка на отправку самому себе

    if sender == "university.help@gmail.com": # Проверка на отправителя по умолчанию
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")
        # Сообщение для нестандартного отправителя

# Примеры вызовов функции
send_email('Семён, добрый вечер! Проверка связи', 'malov333@gmail.com')
send_email('Поздравляем, Вы лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Маклаков, пожалуйста, исправьте все ошибки', 'urban.maklakhcov@mail.ru', sender='urban.teacher@mail.uk')
send_email('Не забыть, в субботу в 13.00 заочники', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
