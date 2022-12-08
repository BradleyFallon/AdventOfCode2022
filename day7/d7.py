class Fil:
    def __init__(self, name, size, parent):
        self.name = name
        self.parent = parent
        self.size = int(size)

class Dir(Fil):
    def __init__(self, name, parent):
        super().__init__(name, 0, parent)
        self.files = dict()
        self.dirs = dict()

    def get_size(self):
        size = 0
        for f in self.files.values():
            size += f.size
        for d in self.dirs.values():
            size += d.size
        return size

    def cd(self, target):
        if target == "..":
            return self.parent
        if target in self.dirs:
            return self.dirs[target]
        return None

    def mkdir(self, target):
        dir = Dir(target, self)
        self.dirs[target] = dir
        return dir

    def make(self, name, sz):
        self.files[name] = Fil(name, sz, self)
        self.update_size(self.files[name].size)

    def update_size(self, size):
        self.size += size
        if self.parent:
            self.parent.update_size(size)
        

    def get_dirs(self):
        return list(self.dirs.values())


def count(root, dir_sizes=[]):
    for name, dir in root.dirs.items():
        if dir.size < 100001:
            dir_sizes.append(dir.size)
            


def main():
    # Make filesystem representation
    root = Dir("", None)
    cwd = root
    with open('input.txt', 'r') as f:
        for line in f:
            if line.startswith("$"):
                # command
                # strip '$ '
                line = line[2:]
                cmd = line.split()[0]
                if cmd == "cd":
                    d_name = line.split()[1]
                    dir = cwd.cd(d_name)
                    if dir:
                        cwd = dir
                    else:
                        cwd = cwd.mkdir(d_name)
            else:
                # output
                sz, name = line.split()
                if sz == "dir":
                    cwd.mkdir(name)
                else:
                    cwd.make(name, sz)
    

    # count
    # print( sum(count(root)) )

    NEED = 30000000
    CAP =  70000000
    # DEL = NEED - AVAILABLE
    DEL = NEED - ( CAP - root.size )
    print("DELETE MINIMUM: ", DEL)

    # Using a list-stack, not recursion, because python recursion limit
    total = 0
    dir_q = [root]
    dir_sizes = list()
    while dir_q:
        dir = dir_q.pop()
        dir_q += dir.get_dirs()
        if dir.size > DEL:
            dir_sizes.append(dir.size)

    print(dir_sizes)
    
    print("Delete: ", min(dir_sizes))




main()

