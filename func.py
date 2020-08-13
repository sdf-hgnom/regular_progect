import re

REGULAR_ULU = r'[A-Z]+([(a-z)+])[A-Z]'



def get_lower_betwin_two_upper(t: str) -> str:
    """Ф-ция вернет list из ,букв нижнего реестра ограниченных буквами верхнего реестра"""
    result = []
    for index, x in enumerate(t):

        if index == 0: continue
        if t[index - 1].isupper() and x.islower() and t[index + 1].isupper():
            result.append(x)
    return "".join(result)


def get_lower_betwin_two_upper_re(t: str) -> str:
    res = re.findall(REGULAR_ULU, t)
    return ''.join(res)


if __name__ == '__main__':
    line = 'tvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxgc'
    t_line = 'AAiAdS'
    res = get_lower_betwin_two_upper(t_line)
    print(res)
    res1 = get_lower_betwin_two_upper_re(t_line)
    print(res1)


