'''
Implementation of Ford-Fulkerson algorithm for finding the maximum flow in graph.
It is assumed that the capacities are integers. This implementation uses BFS
to find augmenting paths which makes it the Edmonds-Karp algorithm.

References:

1. Videos:
https://www.youtube.com/watch?v=_G6_-ljgmXE
https://www.youtube.com/watch?v=GiN3jRdgxU4
https://www.youtube.com/watch?v=v1VgJmkEJW0
https://www.youtube.com/watch?v=6jq52v6Gkts

2. Implementation:
http://people.inf.elte.hu/hytruongson/Ford-Fulkerson/Ford-Fulkerson.html
http://stackoverflow.com/questions/16652902/having-trouble-understanding-and-implementing-the-ford-fulkerson-algorithm
https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
http://www.cs.ucc.ie/~gprovan/CS4407/Ford-Fulkerson-lecture1.pdf

3. Example graphs
http://www.cs.cornell.edu/~wdtseng/icpc/notes/graph_part5.pdf
https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
http://www.cs.princeton.edu/courses/archive/spr04/cos226/lectures/maxflow.4up.pdf
http://www.cse.psu.edu/~sxr48/cse565/lecture-notes/07demo-maxflow.pdf
https://web.stanford.edu/class/cs97si/08-network-flow-problems.pdf
http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2012/lecture-notes/MIT6_046JS12_lec13.pdf
'''


from collections import deque

def ford_fulkerson(n, s, t, c):
    '''
    n: number of nodes
    s: start node
    t: target node
    c: capacity matrix
    '''
    INF = 1 << 50
    max_flow = 0
    
    # flow matrix f(u,v) for computing the residual capacity
    # cf = c(u,v) - f(u,v) for the edge (u,v)
    f = [[0 for k in range(n)] for i in range(n)]
    
    # while there is a path from s to t in the residual graph
    while True:
        # Use BFS to find s-t path in residual graph
        prev = [ -1 for _ in range(n) ]  
        prev[s] = -2                             
        q = deque()
        q.append(s)
        
        while q and prev[t] == -1:
            u = q.popleft()
            for v in range(n):
                cf = c[u][v] - f[u][v]
                if cf > 0 and prev[v] == -1:
                    q.append(v)
                    prev[v] = u
                    
        if prev[t] == -1:   # if t has not been reached
            break
            
        # augment s-t path in residual graph that has been found by BFS
        v = t
        delta = INF
        while True:
            u = prev[v]
            cf = c[u][v] - f[u][v]
            delta = min(delta, cf)
            v = u
            if v == s:
                break
                
        v = t
        while True:
            u = prev[v]
            f[u][v] += delta
            f[v][u] -= delta
            v = u
            if v == s:
                break
            
        max_flow += delta
        
    return max_flow
    
    
#--------------------------------------------------------

'''
Example standard input from
http://people.inf.elte.hu/hytruongson/Ford-Fulkerson/Ford-Fulkerson.html

6 9 1 6
1 2 2
1 4 6
2 3 1
2 4 7
2 5 1
3 5 8
3 6 1
4 5 4
5 6 5

- Input: Standard
The first line includes four numbers V, E, s, t.
V is the number of vertices (1 < V < 1,000). Vertices are numbered from 1.
E is the number of edges (1 < E < 5,000). 

E lines of the form 
u v c
u and v are nodes, and c is the capacity for the edge (u, v).

- Output: Standard
Only one line containing the maximum flow from s to t.
'''


def task():
    from sys import stdin, stdout
    num_nodes, num_edges, s, t = [int(c) for c in stdin.readline().split()]
    capacity_matrix = [[0 for k in range(num_nodes)] for i in range(num_nodes)]
        
    for i in range(num_edges):
        u, v, c = [int(c) for c in stdin.readline().split()]
        capacity_matrix[u-1][v-1] = c
        
    res = ford_fulkerson(num_nodes, s-1, t-1, capacity_matrix)
    stdout.write("Maximum flow: " + str(res) + '\n')
    

if __name__ == '__main__':
    task()
