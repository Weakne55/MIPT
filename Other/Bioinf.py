class FormatException(Exception):
    def __init__(self, format):
        self.format = format

    def __str__(self):
        return f'Недопустимый формат ввода: {self.format} \n Формат может быть FASTA или string'


from collections import defaultdict


class Node:
    """
    Это класс вершин. В вершине мы храним её предка, исходящие из неё рёбра (в виде словаря) и суффиксные ссылки.
    Также (для листьев) будут храниться порядковые номера этих листьев.
    """
    text = ""  # для дальнейшей прорисовки полученного дерева 

    def __init__(self, edges=None, suff_link=None, parent=None, num=0):
        self.edges = edges if edges is not None else defaultdict(type(None))
        self.suff_link = suff_link
        self.parent = parent
        self.num = num

    def __str__(self):
        if self.parent:
            idxs = [e.idxs for e in self.parent.edges.values() if e.target_node == self][0]
            return f"{self.parent}{self.text[idxs[0]: idxs[1]]}_"
        else:
            return "_"


class Edge:
    """Это класс рёбер. В нём храним 2 индекса -- начало и конец части текста, лежащей на ребре.
       Также храним узел, в который направлено ребро.
    """

    def __init__(self, idxs=None, target_node=None):
        self.idxs = idxs
        self.target_node = target_node


class SuffixTree:
    # node =  < suffix_link, parent, edges >
    # edges = { first_char => edge }
    # edge =  < idxs, target_node >
    # idxs = (first, last) # corresponds to label = text[first: last]

    """
    Класс воспринимает два строковых формата:
    1) string -- строка в Pyhon. Соответствует аргумнту ввода format='string'.
    2) FASTA -- FASTA - файл. Соответствует аргументу ввода format='FASTA'

    Внимание! Вам не нужно вводить спецсимвол в конце строки, алгоритм делает это автоматически!
    """
    num = 1  # Переменная для подсчёта листьев. Нужна для поиска подстроки.

    def __init__(self, text, format='FASTA', read: int = 0):
        # обрабатываем текст в соответствии с форматом. Если введён неизвестный формат -- поднимаем исключение
        # read -- число, соответствующее номеру рида, который нужно прочитать как текст в данном FASTA файле

        if format == 'FASTA':
            text = self.from_FASTA(text)[read][1]
            self.text = text + '$'
        elif format == 'string':
            self.text = text + '$'
        else:
            raise FormatException(format)
        Node.text = self.text
        # создаём дефолтные ребро и узел, с помощью которых будем возвращаться к корню
        self.default_edge = Edge(idxs=(0, 1))
        self.default = Node(edges=defaultdict(lambda: self.default_edge))

        # создаём корневой узел, прописываем путь к нему от дефолтного
        self.root = Node(suff_link=self.default)
        self.default_edge.target_node = self.root
        self.end = len(self.text)

        # запускаем построение суффиксного дерева от корня
        self._build_tree(self.root, 0, self.end)

    def __str__(self):
        return f"SuffixTree(text='{self.text}')"

    def from_FASTA(self, file):  # передаем в функцию FASTA файл
        with open(file, 'r') as f:
            lines = f.readlines()
            A = []
            for i in range(len(lines)):
                start_symbol = lines[0][0]  # здесь выявляется начальный символ
                if lines[i][0] == start_symbol:
                    A.append([lines[i].strip()])
                    A[-1].append('')
                else:
                    A[-1][1] = A[-1][1] + lines[i].strip()
        return A  # возвращает массив с названиями и последовательностями

    def pp(self, node=None, indent=0):
        """Функция прорисовывает архитектуру полученного дерева"""
        node = node or self.root
        space = "    " * indent
        print(space + f"ID    : {node}")
        print(space + f"Num   : {node.num}")
        print(space + f"link  : {node.suff_link}")
        print(space + f"edges : ")

        for c, edge in node.edges.items():
            print(space + f"  -{c} {edge.idxs}={self.text[edge.idxs[0]: edge.idxs[1]]}:")
            self.pp(edge.target_node, indent + 1)

    def _build_tree(self, node: Node, n: int, end: int, skip: int = 0):
        """
        Здесь реализован алгоритм Укконена построения суффиксного дерева за время O(n)
        """
        while n < end:  # проходимся по одной букве от начала до конца
            c = self.text[n]
            edge = node.edges[c]

            if edge is not None:  # Если есть ребро, начинающееся с этой буквы, идём по нему
                first, last = edge.idxs
                i, n0 = first, n
                if skip > 0:  # Если было определено, сколько символов можно скипнуть, скипаем
                    can_skip = min(skip, last - first)
                    i += can_skip
                    n += can_skip
                    skip -= can_skip

                # Дальше сравниваем посимвольно i-й b n-й элементы текста
                while (
                        i < last and n < end and
                        (self.text[i] == self.text[n] or edge is self.default_edge)
                ):
                    i += 1
                    n += 1

                # Если дошли до конца ветки, переходим на следующую вершину
                if i == last:
                    node = edge.target_node

                # Если нет -- пора расщеплять ветку
                else:
                    middle_node = Node(parent=node)
                    middle_node.edges[self.text[i]] = edge
                    node.edges[c] = Edge(idxs=(first, i), target_node=middle_node)
                    edge.idxs = (i, last)
                    edge.target_node.parent = middle_node
                    middle_node.suff_link = self._build_tree(node.suff_link, n0, n, i - first)
                    node = middle_node

            else:  # если от текущей вершины нет ребра, начинающейся с текущей буквы, создаём новый лист
                new_leaf = Node(parent=node, num=self.num)
                self.num += 1
                node.edges[c] = Edge(idxs=(n, self.end), target_node=new_leaf)
                node = node.suff_link  # переходим по суффиксной ссылке текущего узла

        return node

    def get_leaves(self, node, entries):
        """Рекурсивная функция чтобы дойти до листьев и записать их номера.
           Номера листьев соответствуют вхождениям суффиксов в текст.
        """
        if len(node.edges) == 0:
            entries.append(node.num)
        for edge in node.edges.values():
            node = edge.target_node
            self.get_leaves(node, entries)

    def search(self, string, format='FASTA'):
        """Поиск подстроки в нашем тексте"""

        if format == 'FASTA':
            string = self.from_FASTA(string)[0][1]
        elif format == 'string':
            string = string
        else:
            raise FormatException(format)
        assert len(string) > 0
        text = self.text
        i = 0
        l = len(string)
        k = string[i]
        node = self.root
        edge = node.edges[k]
        while edge:
            start, end = edge.idxs
            to_compare = text[start:end]
            if l - i > end - start:
                if string[i: i + end - start] != to_compare:
                    j = 0
                    while string[i:i + j] == to_compare[:j]:
                        j += 1
                    print(f'No matches. \n Only {string[:i + j - 1]} matched')
                    return False
                i += end - start
                node = edge.target_node
                edge = node.edges[string[i]]
            else:
                if string[i:] not in to_compare:
                    j = 0
                    while string[i:i + j] == to_compare[:j]:
                        j += 1
                    print(f'No matches. \n Only {string[:i + j - 1]} matched')
                    return False
                entries = []
                node = edge.target_node
                self.get_leaves(node, entries)
                return sorted(entries)

        print(f'No matches. \n Only {string[:i]} matched')
        return False


# text = "ATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGC"
# Node.text = text
tree = SuffixTree('GCF_000865085_1_ViralMultiSegProj15622_genomic (1).fna', format='FASTA', read=5)
tree.search('sequence.fasta')
# tree.pp()
# print(1, tree.search('a'))
# print(2, tree.search('po'))
# print(3, tree.search('p'))
# print(4, tree.search('o'))
# entries = tree.search('ATGC', format='string')
# print(7, tree.search('ananikov'))
# print(8, tree.search('123414243235124221313'))
# print(9, tree.search('bananananab'))
# print(10, tree.search('loalwdo'))
