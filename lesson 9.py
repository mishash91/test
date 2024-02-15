# Создайте декоратор, с помощью которого можно будет сварить кофе с одной любой добавкой и получить финальную стоимость напитка.

class dop_kofe:
    dop_summ: int = 0

    def __call__(self, fn):
        def wrapper(*args, **kwargs):
             return fn(*args, **kwargs) + self.dop_summ
        return wrapper


dop_kofe = dop_kofe()


def no_sugar():  # без сахара
    return -1


def chocolate():  # Шоколад
    return 2.0


def cinnamon():  # корица
    return 1.0


def cream():  # взбитые сливки
    return 2.0



@dop_kofe
def houseBlend():  # Молотый
    return 5.5

@dop_kofe
def DarkRoast():  # Темной обжарки
    return 6.0

@dop_kofe
def Decaf():  # Без кофеина
    return 7.0

@dop_kofe
def Espresso():  # Эспрессо
    return 3.5


dop_kofe.dop_summ = no_sugar()
print(houseBlend())

dop_kofe.dop_summ = cinnamon()
print(Espresso())

dop_kofe.dop_summ = 0
print(Espresso())


#########################################################
# Модернизируйте декоратор, с помощью которого можно будет сварить кофе с любыми добавками и получить финальную стоимость напитка.

def no_sugar():  # без сахара
    return -1


def chocolate():  # Шоколад
    return 2.0


def cinnamon():  # корица
    return 1.0


def cream():  # взбитые сливки
    return 2.0


def res_decor(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        if result is None:
            return 0
        else:
            return result
    return wrapper


@res_decor
def summarize_ingredients(*ingredients):
    result = sum(i() for i in ingredients)
    return result


class DopSumm:
    dop_summ: int = 0

    def __call__(self, fn):
        def wrapper(*args, **kwargs):
             return fn(*args, **kwargs) + self.dop_summ
        return wrapper


additional_ingredients = DopSumm()


@additional_ingredients
def houseBlend():  # Молотый
    return 5.5

@additional_ingredients
def DarkRoast():  # Темной обжарки
    return 6.0

@additional_ingredients
def Decaf():  # Без кофеина
    return 7.0

@additional_ingredients
def Espresso():  # Эспрессо
    return 3.5


additional_ingredients.dop_summ = summarize_ingredients(cinnamon)
print(Decaf())

additional_ingredients.dop_summ = summarize_ingredients()
print(Espresso())

additional_ingredients.dop_summ = summarize_ingredients(cream, chocolate, cinnamon)
print(houseBlend())

