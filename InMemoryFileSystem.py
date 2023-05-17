import pdb


class FileSystem:
    def __init__(self):
        self.file_system_map = {}
        self.root = "/"
        self.pwd = self.root
    
    def get_pwd(self):
        return self.pwd

    def cd (self, cd_node):
        if(not bool(self.file_system_map) or self.pwd == self.root):
            return self.root
        else: 
            # file_system_map is not empty
            # cd defaulting to move one level up in the path hierarchy
            node = self.file_system_map
            cd_node_parent = {i for i in node if node[i] == cd_node}
            print(cd_node_parent)
            self.pwd = cd_node_parent[cd_node]

    def mkdir(self, path):
        node = self.file_system_map
        dirs = path.split("/")
        for dr in dirs[1:]:
            node = node.setdefault(dr, {})

    def ls(self, path):
        node = self.file_system_map
        path = path.split("/")
        if(len(path) == 1):
            return self.file_system_map.keys()
        for p in path[1:]:
            node = node.setdefault(p, {})
        if type(node) == str:
            pdb.set_trace()
            return [path[-1]]
        self.pwd = node    
        return node.keys()

obj = FileSystem()
obj.mkdir("/Users/yo")
obj.mkdir("/Users/yms/Personal")
obj.ls("/Users")
pdb.set_trace()
obj.cd("yms")
print(obj.get_pwd())

