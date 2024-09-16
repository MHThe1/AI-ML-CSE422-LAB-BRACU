import heapq

def astar(graph, heuristic, source, dest):
  fringe = []
  heapq.heapify(fringe)
  visited = []
  par_graph = {}
  distance = 0

  curr_n = source
  curr_cost = 0
  curr_d = 0
  heapq.heappush(fringe, (curr_cost, curr_n, None, curr_d))
  par_graph[curr_n] = None

  while fringe:
    curr = heapq.heappop(fringe)
    par_graph[curr[1]] = curr[2]
    if curr[1] == dest:
      distance = curr[3]
      path(par_graph, dest, source)
      return print(f"Total distance: {distance}")

    if curr[1] not in graph:
      return print("NO PATH FOUND")

    for next, dist in graph[curr[1]].items():
      if next not in visited:
        gn = dist + curr[3]
        hn = heuristic[next]
        cost = gn + hn
        heapq.heappush(fringe, (cost, next, curr[1], gn))

    visited.append(curr[1])

  return print("NO PATH FOUND")

def path(par_graph, goal, src):
  path_found = []
  path_found.append(goal)
  curr = par_graph[goal]
  while curr!=src:
    path_found.append(curr)
    curr = par_graph[curr]
  
  if curr==src:
    path_found.append(curr)

  for i in range(len(path_found)-1, -1, -1):
    if i!=0:
      print(f"{path_found[i]} -> ", end="")
    else:
      print(f"{path_found[i]}")


f = open('22101107_Md. Mehedi Hasan Tanvir_CSE422_05_Assignment01_Summer2024_InputFile.txt', 'r')

graph = {}
heuristic = {}

curr = f.readline().strip()
while curr!="":
  curr_list = curr.split(" ")
  for i in range(0, len(curr_list), +2):
    if i==0:
      heuristic[curr_list[0]] = int(curr_list[1])
      graph[curr_list[0]] = {}
    else:
      graph[curr_list[0]][curr_list[i]] = int(curr_list[i+1])

  curr = f.readline().strip()


f.close()

start_n = input(f"Start Node: ")
dest_n = input(f"Destination: ")
astar(graph, heuristic, start_n, dest_n)
