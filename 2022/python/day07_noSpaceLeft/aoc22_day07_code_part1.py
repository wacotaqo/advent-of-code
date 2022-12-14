# This program is an exercise/challenge from the 2022 advent of code competition
#
#
import os
import re
import utils

filename = "adventofcode2022_day07_input.txt"
filename = "adventofcode2022_day07_input_test.txt"

if utils.detect_ide() == utils.IDE_VSCODE:
    filename = 'python\\day07_noSpaceLeft\\%s' % filename

class DirectoryItem:
    def __init__(self, name, parentItem=None):
        self.parentItem = parentItem
        self.name = name

    def getSize(self):
        return 0

    def getDescriptionStr(self, prefix=""):
        return "%s- DirectoryItem: %s" % (prefix, self.name)

    def __str__(self):
        return "%s(%s)" % (self.__class__.__name__, self.name)

class Directory(DirectoryItem):
    def __init__(self, name, parentItem=None):
        super().__init__(name, parentItem)
        self.children = []

    def getChild(self, childname):
        for child in self.children:
            if child.name == childname:
                return child
        return None

    def getDirs(self, recursive=False):
        output = []
        for child in self.children:
            if child.__class__.__name__ == 'Directory':
                output.append(child)
                if recursive:
                    output.extend(child.getDirs(recursive=True))
        return output

    def addChild(self, child):
        self.children.append(child)
        return child

    def cdDir(self, childname, force_create=False):
        global current_dir
        child = self.getChild(childname)
        if child:
            current_dir = child
        elif not child and force_create:
            current_dir = self.addChild(Directory(childname))

    def cdDotDot(self):
        global current_dir
        global root_dir
        if self.parentItem:
            current_dir = self.parentItem
        else:
            current_dir = root_dir

    def getPath(self):
        if self.parentItem == None:
            return '<rootdir>'
        else:
            return '%s/%s' % (self.parentItem.getPath(), self.name)

    def getSize(self):
        size = 0
        size += sum(child.getSize() for child in self.children)
        return size

    def getDescriptionStr(self, prefix=""):
        output = []
        output.append("%s- %s (dir) (size: %s, children: %s)" % (prefix, self.name, self.getSize(), len(self.children)))
        for child in self.children:
            output.append(child.getDescriptionStr(prefix + "  "))
        return '\n'.join(output)

class File(DirectoryItem):
    def __init__(self, name, size, parentItem=None):
        super().__init__(name, parentItem)
        self.size = int(size)

    def getSize(self):
        return self.size

    def getDescriptionStr(self, prefix=""):
        return "%s- %s (file, size=%s)" % (prefix, self.name, self.size)

fh = open(os.path.join(os.getcwd(), filename), "r")
assignment_input = fh.read().splitlines()
fh.close()

# Patterns
# $ <command> [paramater]
pattern_command = re.compile('\$ ([a-z]+)\s?(.*)?')
# dir <dirname>
pattern_dir = re.compile('dir ([a-z]+)')
# <filesize> <filename>
pattern_file = re.compile('([0-9]+) ([a-z.]+)')

# Process input
root_dir = Directory('/')
current_dir = root_dir
MODE_NONE = 0
for row in assignment_input:
    print("%20s: Parsing '%s'." % (current_dir.getPath(), row))
    # $ <command> [<param>]
    match_obj = re.match(pattern_command, row)
    if match_obj:
        (command, param1) = match_obj.groups()
        if command == "cd": # Goto dir
            dirname = param1
            if dirname == '/':
                current_dir = root_dir
            elif dirname == '..':
                current_dir.cdDotDot()
            else:
                current_dir.cdDir(param1)
        elif command == "ls":
            pass # Do nothing for list dir
        else:
            print("Found unknown command/param: %s, %s" %(command, param1))
    # dir <firname>
    match_obj = re.match(pattern_dir, row)
    if match_obj:
        dirname = match_obj.groups()[0]
        newDir = Directory(dirname, current_dir)
        current_dir.addChild(newDir)
    # <filesize> <filename>
    match_obj = re.match(pattern_file, row)
    if match_obj:
        (filesize, filename) = match_obj.groups()
        current_dir.addChild(File(filename, filesize, current_dir))

print("Directory snapshot:")
print(root_dir.getDescriptionStr())
print()
all_dirs = [(dir.name, dir.getSize()) for dir in root_dir.getDirs(recursive=True)]
all_max_100000_dirs = [(dirname, dirsize) for (dirname, dirsize) in all_dirs if dirsize <= 100000]
print("Total dir size: %s" % root_dir.getSize())
print("All dirs: %s" % all_dirs)
print("All dirs (maxsize 100000): %s" % all_max_100000_dirs)
print("sum of these sizes: %s" % sum([dirsize for (dirname, dirsize) in all_max_100000_dirs]))

