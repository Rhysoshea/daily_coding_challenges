"""
Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.
"""
import time

def longest_path_tree(input):
    files = input.split("\n")
    fs = {}

    current_path = []

    for f in files:
        indentations = 0

        while '\t' in f:
            indentations += 1
            f = f[1:]
        current_node = fs

        for subdir in current_path[:indentations]:
            current_node = current_node[subdir]

        if '.' in f:
            current_node[f] = True
        else:
            current_node[f] = {}

        current_path = current_path[:indentations]
        current_path.append(f)

    return fs

def count_length(tree): #recursion
    paths = []
    for key, node in tree.items():
        if node == True:
            paths.append(key)
        else:
            paths.append(key + '/' + count_length(node))

    paths = [path for path in paths if '.' in path]
    if paths:
        return max(paths, key=lambda path:len(path)) #returns max based on path length
    else:
        return ""

def solution1(input):
    return len(count_length(longest_path_tree(input)))

def construct_directory_tree(input):
    files = input.split("\n")
    fs = {}

    current_path = []
    max_length = 0

    for f in files:
        indentations = 0

        while '\t' in f:
            indentations += 1
            f = f[1:]

        current_node = fs

        for subdir in current_path[:indentations]:
            current_node = current_node[subdir]

        if '.' in f:
            current_node[f] = True
            max_length = sum([len(x) for x in current_path]) + len(f) + indentations
        else:
            current_node[f] = {}

        current_path = current_path[:indentations]
        current_path.append(f)

    return max_length


def solution2(input):
    max_length = construct_directory_tree(input)
    if max_length != 0:
        return max_length
    return ''


start1 = time.process_time()
str = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print(solution1(str))
time1 = time.process_time()-start1
print(time1)

start2 = time.process_time()
str = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print(solution2(str))
time2 = time.process_time()-start2
print(time2)

if time1 < time2:
    print (f'solution1 quicker by {((time2-time1)/time2)*100}%')
else:
    print (f'solution2 quicker by {((time1-time2)/time1)*100}%')

# assert solution1("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext") == 20
#
# assert solution1("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext") == 32
#
# assert solution2("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext") == 20
#
# assert solution2("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext") == 32
