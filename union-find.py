from random import randint
import matplotlib.pyplot as plt
import networkx as nx


class BaseUF():
    """
    base class for implementation of union-find classes
    """

    @staticmethod
    def input_to_list(lines):
        """converts input lines to a list of lists containing integers

            for example :
                lines:
                    "2 3 4
                    5 9
                    5 0
                    9 4"
                output:
                    [[2,3,4], [5,9], [5,0], [9,4]]
            """
        return list(map(lambda line: list(map(int, line.split())), lines.split('\n')))

    @staticmethod
    def test(_class, input_text=None, debug=True):
        """
        run and test the class with given method and input
        """

        # if no input has given, input_text fills out randomly
        if input_text == None:
            input_text = '\n'.join(
                ['10 8 8'] +
                [f'{randint(0, 9)} {randint(0, 9)}' for i in range(8)] +
                [f'{randint(0, 9)} {randint(0, 9)}' for i in range(8)]
            )

        lines = BaseUF.input_to_list(input_text)
        nodes_n, unions_n, queries_n = lines[0]
        union_queries = lines[1:unions_n+1]
        connected_queries = lines[unions_n+1:unions_n+queries_n+1]
        result = ''

        G = nx.Graph()
        G.add_nodes_from(range(nodes_n))

        uf = _class(nodes_n)
        for p, q in union_queries:
            uf.union(p, q)
            G.add_edge(p, q, weight=1)
            if debug:
                print(uf.ids, f'- {p} and {q} connected')

        for p, q in connected_queries:
            result += f'{uf.connected(p,q)}\n'
            if debug:
                print(f'Are {p} and {q} connected ? ', 'YES' if uf.connected(
                    p, q) else 'NO ', ' - ', 'right' if nx.has_path(G, p, q) == uf.connected(p, q) else 'wrong', 'answer',
                    '(checked by networkx module)')

        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, node_size=700)
        nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=6)
        nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
        plt.axis('off')
        plt.show()

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


class QuickUnionImprovedUF(BaseUF):

    ids = []
    weights = []

    def __init__(self, N):
        self.ids = [i for i in range(N)]
        self.weights = [1 for i in range(N)]

    def root(self, p):
        t = p
        while t != self.ids[t]:
            t = self.ids[t]
        return t

    def union(self, p, q):
        # swaping p and q if the weight of root of q is more than p
        if self.weights[self.root(p)] > self.weights[self.root(q)]:
            p, q = q, p
        self.ids[self.root(q)] = self.root(p)
        self.weights[self.root(p)] += self.weights[self.root(q)]

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def test(input_text=None, debug=True):
        BaseUF.test(QuickUnionImprovedUF, input_text=input_text, debug=debug)


if __name__ == '__main__':
    # QuickFindUF.test(debug=True)
    # QuickUnionUF.test(debug=True)
    QuickUnionImprovedUF.test(debug=True)
