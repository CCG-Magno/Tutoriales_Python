
class Node:

    def __init__(self, data=None, adj=[]):
        self.data = data
        self.adj = adj
        return
    
    def data(self):
        return self.data
    
    def adjacent(self):

        for node in self.adj:
            yield node

    def __str__(self):
        return self.data
    
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

def create_graph(di=graph):
    f, d = Node('F') , Node('D')
    e = Node('E', adj=[f])
    c = Node('D', adj=[f])

    b = Node('B', adj=[d,e])
    a = Node('A', adj=[b,c])
    nodes= [f,d, e , c,b,a ]
    
    return nodes

def depth_first_search(visited=set(), graph={}, start_node=Node()):

    stack=[]

    stack.append(start_node)

    while len(stack) > 0:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)
            for n in node.adjacent():
                stack.append(n)

    return

def breadth_first_search(visited=set(), graph={}, start_node=Node()):

    que=[]

    que.append(start_node)

    while len(que) > 0:
        node = que.pop(0)
        if node not in visited:
            visited.add(node)
            print(node)
            for n in node.adjacent():
                que.append(n)

    return

if __name__ == '__main__':
    graph =create_graph()
    print('DFS:')
    depth_first_search(start_node=graph[len(graph)-1])
    print()
    print('BFS:')
    breadth_first_search(start_node=graph[len(graph)-1])
    print()