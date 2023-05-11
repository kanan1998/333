from django import template


register = template.Library()

stop_words = [
    'плохое_слово1',
    'плохое_слово2',
    'плохое_слово3',
]

@register.filter(name='censor')
# первый аргумент здесь это то значение, к которому надо применить фильтр, второй аргумент — это аргумент фильтра,
# т. е. в шаблоне будет примерно следующее - value|multiply:arg
def censor(value):
    # фильтр заменяет слова из стоп-листа на '...'
    for sw in stop_words:
        value = value.lower().replace(sw.lower(), '...')
    return value

    # проверка типов аргументов
    # if isinstance(value, str)
    #     return ...
    # else:
    #     #  в случае, если кто-то неправильно воспользовался нашим тегом, выводим ошибку
    #     raise ValueError(f'Ошибка! Тип {type(value)} не подходит!')


@register.filter(name='preview')
# первый аргумент здесь это то значение, к которому надо применить фильтр, второй аргумент — это аргумент фильтра,
# т. е. в шаблоне будет примерно следующее - value|multiply:arg
def preview(value):
    if len(value) > 20:
        return value[:21] + '...'
    else:
        return value

#@register.simple_tag()
#def current_time(format_string='%b %d %Y'):
#   return datetime.utcnow().strftime(format_string)


if __name__ == '__main__':
    print(censor("""Слово1 слово2 плохое_слово1 Плохое_слово2
плохое_слово3 плохое_слово4 слово3"""))