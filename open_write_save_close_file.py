import os
# open and read file data_test.txt (he must be in project folder)
f = open('data_test.txt')
content = f.read()
print(content)

# open and read file data_test.txt (he must be in project folder, if file does not exist print 'FILE NOT FOUND')
try:
    with open('data_test.txt') as k:
        content = k.read()
except FileNotFoundError:
    content = 'FILE NOT FOUND'
print(content)

#
with open('data_test.txt', 'a') as tw:
    tw.write('some data')
    print('new line 2', file=tw)

path = os.path.join(as.path.abspath(os.path.dirname(__file__)), 'data_test.txt')
os.remove(path)