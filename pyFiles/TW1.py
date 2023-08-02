from collections import defaultdict
graph=defaultdict(list)
def addEdge(u,v):
  graph[u].append(v)
def dfs(start,goal,depth):
  print(start,end="->")
  if start==goal:
    return True
  if depth<=0:
    return False
  for i in graph[start]:
    if dfs(i,goal,depth):
      return True
  return False
def dfid(start,goal,maxdepth):
  for i in range(maxdepth):
    print("DFS at level:",i+1)
    print("Path:")
    isgoal=dfs(start,goal,i)
  if isgoal==True:
    print("Found")
  else:
    print("Not found")
graph=defaultdict(list)
addEdge('A','B')
addEdge('A','C')
addEdge('B','D')
addEdge('B','E')
addEdge('C','F')
addEdge('C','G')
addEdge('G','Z')
addEdge('K','Z')
g=input("Enter the goal node:")
dfid('A',g,4)