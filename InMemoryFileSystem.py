import pdb
    
class FileSystemNode:
    def __init__(self, name = ""):
        self.children = {}
        self.isFile = False
	self.name = name
	self.parent = None
	self.contents = ""
        

class FileSystem:
    def __init__(self):
        self.root = FileSystemNode("/")
        self.pwd = self.root #Present working directory
    
    def get_pwd(self):
        print("pwd -->" + str(self.pwd.name))
        return self.pwd

    def mkdir_using_path(self, path = ""):
	""" mkdir wont change  the pwd"""
        node = self.root
        dirs = path.split("/")
        for dr in dirs[1:]:
            if dr not in node.children:
		new_node = FileSystemNode(name = dr)
		new_node.parent = node
                node.children[dr] = new_node
            node = node.children[dr]

    def mkdir(self, dr = ""):
	"""Creates the dir in pwd"""
	new_dr = FileSystemNode(name = dr)
	new_dr.parent = self.pwd
	self.pwd.children[dr] = new_dr 

    def cd(self, cd_node_name = None):
	def cd_recur(node, cd_node_name):
	    for key, child in node.children.items():
		if(key == cd_node_name):
		    self.pwd = child
		    return
		else:
		    cd_recur(child, cd_node_name)

	if(cd_node_name):
	    cd_recur(self.root,cd_node_name)
	    if(not self.pwd.name == cd_node_name):
		print ("Dir not found")
	else:
	    pdb.set_trace()
	    #Go to parent of pwd
	    self.pwd = self.pwd.parent

    def ls(self, path =  None):
	if(not path):
	    print ("ls -> ")
	    print ( self.pwd.children.keys())
	else:
	    node = self.root
	    dirs = path.split("/")
	    if(len(path) == 1):
		print (self.root.children.keys())
	    for dr in dirs[1:]:
		if dr not in node.children:
		    return False
		node = node.children[dr]
	    print(node.children.keys())

    def __repr__(self):
        def recur(node, indent):
            return "".join(indent + key + ("$" if child.isFile else "") 
                                  + recur(child, indent + "  ") 
                for key, child in node.children.items())

        return recur(self.root, "\n")

    def delete(self, delete):
	del self.pwd.children[delete]

    def create_file(self, filename):
	fileNode = FileSystemNode(name = filename)
	fileNode.isFile = True
	self.pwd.children[filename] = fileNode

    def write_to_file(self, filename, contents):
	if filename not in self.pwd.children.keys():
	    print( "File Not Found")
	    return
	file = self.pwd.children[filename]
	if file.isFile == False:
	    print ("File Not Found")
	    return
	file.contents+= contents

    def get_file_contents(self, filename):
	if filename not in self.pwd.children.keys():
            print( "File Not Found")
            return
        file = self.pwd.children[filename]
        if file.isFile == False:
            print ("File Not Found")
            return
	print(file.contents)	

    def mv_file(self, filename, destn):
	if destn not in self.pwd.children.keys():
	    print "Destn not found in current directory"
	if filename not in self.pwd.children.keys():
	    print "File not found in current directory"
	if self.pwd.children[filename].isFile == False:
	    print "File not found in current directory"
	filename_node = self.pwd.children[filename]
	destn_node = self.pwd.children[destn]
	destn_node.children[filename] =  filename_node
	del self.pwd.children[filename]

    
	

obj = FileSystem()
obj.mkdir( "school") # makes dir in pwd
obj.cd("school")
obj.get_pwd()
obj.mkdir("homework")
obj.cd("homework")

obj.mkdir("math")
obj.mkdir("lunch")
obj.mkdir("history")
obj.mkdir("spanish")
obj.delete("lunch")
obj.ls()
obj.cd("math")
obj.mkdir("algebra")

print (obj)
print( "----")
#print(obj.list_all_paths(obj.root,"/"))
obj.get_pwd()
obj.create_file("fileA.txt")
obj.write_to_file("fileA.txt", "fileA contents")
obj.get_file_contents("fileA.txt")

print(obj)

obj.mv_file("fileA.txt","algebra")

print(obj)
