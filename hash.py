import pickle
from difflib import SequenceMatcher

a1 = pickle.dumps('2', protocol=0)
a11 = pickle.dumps('1', protocol=0)
a2 = pickle.dumps({'vasya'}, protocol=0)

b1 = '2'
b3 = {'vasya'}


def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = word_file.read().split()

    return valid_words


def generator(slovar, num, end, step, magic_number, count_words):
    begin = (end // (count_words + 1)) * num  # разбиваю словарь на сегменты, количество сегментов count + 1. count - количество слов
    n = magic_number + begin - end if magic_number + begin >= end else magic_number + begin  # сдвигаю начало на magic_number
    old_word = ''
    while 1:
        n += step
        if n >= end:
            n = n - end

        if len(slovar[n]) < 4:
            continue

        new_word = slovar[n].title()

        if SequenceMatcher(None, old_word, new_word).ratio() > 0.7:  # если предыдущее слово похоже на новое на 70%,
            # то ищем другое
            continue

        old_word = new_word

        yield new_word


def init_generators(count_words, step, magic_number, eng_words, dict_length):
    lst = []
    for i in range(1, count_words + 1):
        lst.append(generator(eng_words, i, dict_length - 1, step, magic_number, count_words))

    return lst


def get_words(count_variables, generator_list, separate='_'):
    words = []
    for _ in range(count_variables):
        lst = [next(g) for g in generator_list]
        words.append(separate.join(lst))

    return words


def my_hash(obj, count_words=1, count_variables=1, separate=''):
    obj_id = id(obj)
    eng_words = load_words()
    dict_length = len(eng_words)
    magic_number = obj_id % dict_length
    step = dict_length // magic_number

    gens = init_generators(count_words, step, magic_number, eng_words, dict_length)
    return get_words(count_variables, gens, separate)


if __name__ == '__main__':
    print(my_hash(a1, 2, 2, '-'))
    print(my_hash(a1, 2, separate=''))
    print('___________')
    print(my_hash(b3))
    print(my_hash(b3))
    print(my_hash(b3))
    print('___________')
    print(my_hash(b1))