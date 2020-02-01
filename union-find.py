class BaseUF():
    """
    base class for implementation of union-find classes
    """

    @staticmethod
    def test(_class, input_text=None, debug=True):
        """
        run and test the class with given method and input
        """

        from random import randint

        # if no input has given, input_text fills out randomly
        if input_text == None:
            input_text = '\n'.join(['10 5 5'] + [f'{randint(0, 9)} {randint(0, 9)}' for i in range(5)] +  [f'{randint(0, 9)} {randint(0, 9)}' for i in range(5)])

        lines = input_text.split('\n')
        nodes_n, unions_n, queries_n = map(int, lines[0].split())
        union_queries = map(lambda line: list(map(int, line.split())), lines[1:unions_n+1])
        connected_queries = map(lambda line: list(map(int, line.split())), lines[unions_n+1:unions_n+queries_n+1])
        result = ''

        uf = _class(nodes_n)
        for p,q in union_queries:
            uf.union(p,q)
            if debug: print(uf.ids, f'- {p} and {q} connected')

        for p,q in connected_queries:
            result += f'{uf.connected(p,q)}\n'
            if debug: print(f'{p} and {q}:', 'connected' if uf.connected(p,q) else 'not connected')

        return result


class QuickFindUF(BaseUF):
    """
    Implementation of eager algorithm or quick-find for dynamic connectivity problem.
    """

    ids = []

    def __init__(self, N):
        """
        initialize the ids list with [0 ... N-1]
        """

        self.ids = [i for i in range(N)]


    def union(self, p, q):
        """
        connect the two given elements

        change the id of all connected elements of p to ids[q]
        """

        self.ids = [i if i != self.ids[p] else self.ids[q] for i in self.ids]


    def connected(self, p, q):
        """
        return True if two given elements are connected, otherwise False

        checks if two given elements are connected by checking if they both have the same id
        """

        return self.ids[p] == self.ids[q]

    def test(input_text=None, debug=True):
        BaseUF.test(QuickFindUF, input_text=input_text, debug=debug)


class QuickUnionUF(BaseUF):
    """
    Implementation of lazy algorithm or quick-union for dynamic connectivity problem.
    """

    ids = []

    def __init__(self, N):
        """
        initialize the ids list with [0 ... N-1]
        """

        self.ids = [i for i in range(N)]


    def union(self, p, q):
        """
        connect the two given elements

        change the id of root of p to ids[q]
        """

        self.ids[self.root(p)] = self.ids[q]


    def connected(self, p, q):
        """
        return True if two given elements are connected, otherwise False

        check if the roots of p and q are the same
        """

        return self.root(p) == self.root(q)


    def root(self, p):
        """
        return the root of given element
        """

        root = self.ids[p]
        while root != self.ids[root]:
            root = self.ids[root]

        return root

    def test(input_text=None, debug=True):
        BaseUF.test(QuickFindUF, input_text=input_text, debug=debug)


if __name__ == '__main__':
    QuickFindUF.test(debug=True)
    QuickUnionUF.test(debug=True)