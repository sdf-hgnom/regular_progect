def get_lower_betwin_two_upper(t: str) -> str:
    """Ф-ция вернет list из ,букв нижнего реестра ограниченных буквами верхнего реестра"""
    result = []
    for index, x in enumerate(t):

        if index == 0: continue
        if t[index - 1].isupper() and x.islower() and t[index + 1].isupper():
            result.append(x)
    return "".join(result)


if __name__ == '__main__':
    line = 'AiAdAARTtS'
    res = get_lower_betwin_two_upper(line)
    print(res)
