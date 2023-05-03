# Исходя из того, что дерево создается один раз и не модифицируется,
# потом из него только достаются данные, можно потратить время и память
# чтобы получение данных сделать быстрым.

class TreeStore: 
    def __init__(self, items: list) -> None:
        self._nodes = {}

        for item in items:
            if isinstance(item, dict) and "id" in item and "parent" in item:
                if item["id"] not in self._nodes:
                    self._nodes[item["id"]] = item
                else:
                    raise UniqueIdException(item)
            else:
                raise RequiredFieldsException(item)
        
        self._children = {key: [] for key in self._nodes.keys()}
        self._all_parents = {key: [] for key in self._nodes.keys()}

        for _, item in self._nodes.items():
            if item["parent"] != "root":
                self._children[item["parent"]].append(item)

        path = []
        def dfs(node):
            path_node = path.copy()
            path_node.reverse()
            self._all_parents[node["id"]] = path_node
            path.append(node)

            children = self.getChildren(node["id"])
            if len(children) == 0:
                path.pop()
                return
            
            for child in children:
                dfs(child)

            path.pop()
        
        root_node = None
        for _, node in self._nodes.items():
            if node["parent"] == "root":
                root_node = node

        dfs(root_node)

    def getAll(self):
        return list(self._nodes.values())
    
    def getItem(self, id):
        return self._nodes[id]

    def getChildren(self, id):
        return self._children[id]

    def getAllParents(self, id):
        return self._all_parents[id]


class RequiredFieldsException(Exception):
    def __init__(self, obj: object) -> None:
        self.obj = obj

    def __str__(self) -> str:
        return f"The object must have 'id' and 'parent' fields." \
               f"Object: {self.obj}"


class UniqueIdException(Exception):
    def __init__(self, obj: object) -> None:
        self.obj = obj

    def __str__(self) -> str:
        return f"The object`s 'id' field must be unique in the Tree." \
               f"Object: {self.obj}"
