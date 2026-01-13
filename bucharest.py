# Université de Sherbrooke
# Code préparé par Audrey Corbeil Therrien
# Laboratoire 1 - Interaction avec prolog

from swiplserver import PrologMQI, PrologThread
from dataclasses import dataclass

@dataclass
class Node:
    parents: list['Node']
    city: str
    cost: int
    costRoute: int

def get_successors(node: Node, prolog_thread: PrologThread):
    query = f"s({node.city}, Cities)."
    results = prolog_thread.query(query)[0]['Cities']
    successors = []
    for city in results:
        destination = city
        cost = prolog_thread.query(f"d({node.city}, {destination}, Cost).")[0]['Cost']
        h = prolog_thread.query(f"h({city},H).")[0]['H']
        successor_node = Node(
            parents=node.parents + [node] if node.parents else [node],
            city=destination,
            cost=node.costRoute + cost + h,
            costRoute=node.costRoute + cost
        )
        successors.append(successor_node)
    return successors

def a_star(start_node: Node, goal_city: str, prolog_thread: PrologThread):
    open_list = [start_node]
    closed_list = []

    while open_list:
        open_list.sort(key=lambda x: x.cost)
        current_node = open_list.pop(0)

        if current_node.city == goal_city:
            return current_node.parents + [current_node]

        closed_list.append(current_node)

        successors = get_successors(current_node, prolog_thread)

        for successor in successors:
            if any(closed_node.city == successor.city for closed_node in closed_list):
                continue

            existing_node = next((node for node in open_list if node.city == successor.city), None)
            if existing_node:
                if successor.cost < existing_node.cost:
                    open_list.remove(existing_node)
                    open_list.append(successor)
            else:
                open_list.append(successor)

    return None

if __name__ == '__main__':
    with PrologMQI() as mqi_file:
        with mqi_file.create_thread() as prolog_thread:
            # Load a prolog file
            result = prolog_thread.query("[prolog/roumanie].")

            if not result:
                print("Erreur lors du chargement du fichier prolog/roumanie.pl")
                exit(1)
                
            start_node = Node(parents=None,city="arad", cost=0, costRoute=0)
            goal_city = "bucharest"
            path = a_star(start_node, goal_city, prolog_thread)
            print("Chemin trouvé :")
            for node in path:
                print(f"{node.city} (Coût: {node.costRoute})")
            
    

    

