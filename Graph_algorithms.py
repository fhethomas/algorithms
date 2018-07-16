def check_node(node,desired_quality,graph_quality=None):
    if graph_quality==None:
        return False
    return desired_quality == graph_quality[node]
def breadth_first(start,graph,desired_quality,graph_quality=None):
    queue=[start]
    found_result = False
    queue_int=0
    parent={start:[[]]}
    checked=set()
    while found_result==False:
        node=queue[queue_int]
        if node not in checked:
            if check_node(node,desired_quality,graph_quality) or desired_quality==node:
                found_result=True
                break
            else:
                queue+=graph[node]
                for sub_node in graph[node]:
                    if sub_node not in parent.keys():
                        parent[sub_node]=[[node]+x for x in parent[node]]
                    else:
                        parent[sub_node]+=[[node]+x for x in parent[node]]
                checked.add(node)
                queue_int+=1
        else:
            queue_int+=1
        if len(checked)==len(graph.keys()):
            print('No: {0} in graph'.format(desired_quality))
            return None
    print('{0} found'.format(desired_quality))
    node_routes = {len(route): route for route in parent[node]}
    shortest_route = node_routes[min(node_routes.keys())][::-1] + [node] 
    print('shortest route: {0}'.format('-'.join(shortest_route)))
    return shortest_route
def lowest_cost(costs,processed):
    lowest=float("inf")
    current_node = None
    for node in costs.keys():
        cost=costs[node]
        if cost < lowest and node not in processed:
            current_node = node
            lowest = cost
    return current_node
def dijkstra(start,end,graph):
    """Implementation of dijkstra algorithm
    Parameters
    -----------
    start : string
        start point for the graph
    end : string
        end point for the graph
    graph : dictionary
        Dictionary should contain the 
        graph, with each dictonary element 
        containing the weighted elements
        example:
        {'a':{'b':2,'c':3},'b':{'a':2,'d':4},'c':{'a':3,'d':3},'d':{'b':4,'c':3}}
    Returns
    ----------
    cost : int/float
        cost of getting to end node
    route : list of strings
        the nodes to get to end node
    """
    # establish initial parents/costs
    parents={x:start for x in graph[start].keys()}
    costs=graph[start]
    processed=[]
    # establish cost of all nodes as infinite to start
    for node in graph.keys():
        if node not in costs.keys():
            costs[node]=float('inf')
    current_node=lowest_cost(costs, processed)
    # Main controlflow loop
    while current_node is not None:
        cost=costs[current_node]
        neighbours=graph[current_node]
        # loop through each node's neighbours
        for n in neighbours.keys():
            new_cost=cost+neighbours[n]
            if new_cost < costs[n]:
                costs[n]=new_cost
                parents[n]=current_node
        # add current node to processed, so not re-run
        processed.append(current_node)
        current_node=lowest_cost(costs,processed)
    # Calculate the route that got from start to end
    last=end
    route=[end]
    while last!=start:
        last=parents[last]
        route+=[last]
    # reverse the route so goes from start - end
    route=route[::-1]
    print('Cost to get from {0} to {1} is: {2}.'.format(start,end,costs[end]))
    print('Nodes to result: {0}'.format(route))
    return costs[end], route