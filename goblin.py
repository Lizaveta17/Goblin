def upgrade_data(n, data):
    mas = []
    for i in range(n):
        mas.append([])
    for j in data:
        mas[j[0]].append(j[1])
        mas[j[1]].append(j[0])
    return mas


class EulerWayCircle:
    def __init__(self, n, data):
        self.neighbors = upgrade_data(n, data)
        self.ways = []
        self.way = []
        self.stack = []
        self.visited = [False] * n
        self.break_on_ways()
        self.output()

    def break_on_ways(self):
        self.dfs(0)
        count = self.get_count_odd_v()
        connect = self.graph_is_connected()
        if count == 0 and connect:
            # print("euler")
            self.stack.append(0)
            self.find_euler_way(0)
            self.ways.append(self.way)
        elif count <= 2 and connect:
            # print("polu-euler")
            for v in range(len(self.neighbors)):
                if len(self.neighbors[v]).__mod__(2) == 1:
                    self.stack.append(v)
                    self.find_euler_way(v)
                    self.ways.append(self.way)
                    break
        else:
            # print("not euler")
            self.choose_start()
            while self.em_is_not_mark():
            # for i in range(len(self.visited)):
            #     if self.em_is_not_mark():
                self.choose_start()
                # else:
                #     break

    def get_count_odd_v(self):
        count = 0
        for v in self.neighbors:
            if len(v).__mod__(2) == 1:
                count += 1
        return count

    def em_is_not_mark(self):
        count = 0
        for l in self.neighbors:
            if l:
                count += 1
        return count != 0

    def find_euler_way(self, v):
        if not self.neighbors[v]:
            n = self.stack.pop()
            self.way.append(n)
            while self.stack:
            # for i in range(len(self.stack)):
            #     if self.stack:
                w = self.stack[-1]
                if not self.neighbors[w]:
                    self.way.append(self.stack.pop())
                    # else:
                    #     break
            return
        for u in self.neighbors[v]:
            self.neighbors[v].remove(u)
            self.neighbors[u].remove(v)
            self.stack.append(u)
            self.find_euler_way(u)

    def choose_start(self):
        for v in range(len(self.neighbors)):
            if len(self.neighbors[v]) == 1:
                return self.start(v)
        for v in range(len(self.neighbors)):
            if len(self.neighbors[v]).__mod__(2) == 1:
                return self.start(v)
        for v in range(len(self.neighbors)):
            if self.neighbors[v]:
                return self.start(v)

    def start(self, v):
        u = self.neighbors[v][0]
        self.neighbors[v].remove(u)
        self.neighbors[u].remove(v)
        self.way.append(v)
        self.way.append(u)
        return self.find_way(u)

    def find_way(self, v):
        if not self.neighbors[v]:
            way = self.way.copy()
            self.ways.append(way)
            self.way.clear()
            return
        for u in self.neighbors[v]:
            self.neighbors[v].remove(u)
            self.neighbors[u].remove(v)
            self.way.append(u)
            return self.find_way(u)

    def dfs(self, v):
        self.visited[v] = True
        if not self.neighbors[v]:
            return
        for w in self.neighbors[v]:
            if not self.visited[w]:
                self.dfs(w)

    def graph_is_connected(self):
        for v in range(len(self.visited)):
            if not self.visited[v] and len(self.neighbors[v]) > 0:
                return False
        return True

    def output(self):
        length = len(self.ways)
        print(length)
        s = ""
        for way in self.ways:
            for v in way:
                s += str(v + 1) + ' '
            print(s)
            s = ""


if __name__ == '__main__':
    vm, em = map(int, input().split())
    d = []
    # d = [(0, 2), (0, 4), (1, 2), (1, 4), (2, 4), (2, 3), (3, 4)]
    # d = [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (2, 3), (2, 5), (3, 5), (3, 4), (4, 5)]
    for k in range(em):
        a, b = map(int, input().split())
        d.append((a - 1, b - 1))
    ex = EulerWayCircle(vm, d)
