class Stack:

    def __init__(self):
        """
        Создание стека
        """
        self.items = []


    def push(self, item):
        """
        Добавление нового элемента на вершину стека
        """
        self.items.append(item)


    def pop(self):
        """
        Удаление элемента из стека
        """
        return self.items.pop()


    def peek(self):
        """
        Возвращение верхнего элемента стека без удаления
        """
        return self.items[len(self.items) - 1]


    def isEmpty(self):
        """
        Проверка стека на пустоту
        """
        return self.items == []


    def size(self):
        """
        Возвращение кол-ва эл-ов в стеке
        """
        return len(self.items)

