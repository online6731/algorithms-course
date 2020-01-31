class QuickFindUF():
    """
    union-find class which implements the eager algorithm (quick-find)
    for solving dynamic connectivity problem.
    """

    ids = []

    def __init__(self, N):
        """
        initialize the ids list by values from 0 to N-1
        """

        self.ids = [i for i in range(N)]


    def union(self, p, q):
        """
        connects the two given elements by changing the id of
        all connected elements of p to the id of q
        """

        self.ids = [i if i != self.ids[p] else self.ids[q] for i in self.ids]


    def connected(self, p, q):
        """
        checks if two given elements are connected by checking if they both have the same id
        """

        return self.ids[p] == self.ids[q]


    @staticmethod
    def test(input_text=None, debug=True):
        """
        runs and tests the class with given input_text
        """
        lines = input_text.split('\n')
        nodes_n, unions_n, queries_n = map(int, lines[0].split())
        union_queries = map(lambda line: list(map(int, line.split())), lines[1:unions_n+1])
        connected_queries = map(lambda line: list(map(int, line.split())), lines[unions_n+1:unions_n+queries_n+1])
        result = ''

        uf = QuickFindUF(nodes_n)

        for p,q in union_queries:
            uf.union(p,q)
            if debug: print(uf.ids, f'- {p} and {q} connected')

        for p,q in connected_queries:
            result += f'{uf.connected(p,q)}\n'
            if debug: print(f'{p} and {q}:', 'connected' if uf.connected(p,q) else 'not connected')

        return result


if __name__ == '__main__':
    from random import randint
    random_generated_input = '\n'.join(['10 5 5'] + [f'{randint(0, 9)} {randint(0, 9)}' for i in range(5)] +  [f'{randint(0, 9)} {randint(0, 9)}' for i in range(5)])
    QuickFindUF.test(input_text=random_generated_input, debug=True)