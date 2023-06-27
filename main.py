import types

# тестовый список

test_list = [['Ira', 'Petya', 'Larisa', 'Boris', 'Rosa'],
            [12, 'forest', 'man'],
            [{"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
             {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
             {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}],
            [{"title":"Web-разработчик с нуля", "duration":19,
			"mentors":["Николай Лопин", "Алексей Кулагин", "Эдгар Нуруллин", "Александр Дудинский"]}],
            [(1, 2, 3),(10,15,20)]]

# итератор, который принимает список списков и возвращает их плоское представление
class FlatIterator:

    def __init__(self, new_list):
        self.new_list = [object for item in new_list for object in item]

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.new_list):
            raise StopIteration
        return self.new_list[self.cursor]


if __name__ == '__main__':

    for element in FlatIterator(test_list):
        print(element)

    flat_list = [item for item in FlatIterator(test_list)]
    print(flat_list)

# проверка теста 1
def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()

# генератор, который принимает список списков и возвращает их плоское представление.

def flat_generator(new_list):
    for item in new_list:
        for elem in item:
            yield elem

if __name__ == '__main__':
    for item_1 in flat_generator(test_list):
        print(item_1)

# проверка теста 2
def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()