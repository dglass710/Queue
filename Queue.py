class Queue(object):

    class Node(object):
        'A wrapper around a str with a recursive reference to another Node'
        def __init__(self, name, nxt = None):
            'sets the two fields (str/Node)'
            self.title = name
            self.next = nxt # name of the next element
        def getName(self):
            'returns title'
            return self.title
        def changeName(self, name):
            'sets title to name'
            self.name = name

    def __init__(self, someList = []):
        '''initilizes a Queue of Nodes, one for each str elem in someList
        The first element will be the first Node and the order of elems will be maintained'''
#        if any( type(element) != str for element in someList ):
#            raise('Non-String element found in list\nExpected only string values')
        self.first = None
        self.last = None
        self.length = 0
        if someList == []:
            return
        for j in range(len(someList)):
            self.length += 1
            i = len(someList) - (j + 1)
            if i == len(someList) - 1:
                self.last = self.Node(someList[i])
                self.first = self.last
            else:
                self.first = self.Node(someList[i], self.first)

    def add(self, someStr):
        'adds a Node to the Queue and assigns the val of someStr to its title field'
        self.length += 1
        if self.first == None:
            self.last = self.Node(someStr)
            self.first = self.last
        else:
            self.last.next = self.Node(someStr)
            self.last = self.last.next

    def seek(self):
        'seek returns the title of the first/next Node in the Queue'
        if self.emptyMessage():
            return None
        return self.first.getName()

    def pop(self):
        'both returns the title of and removes the first Node assigning its next to first'
        self.length -= 1
        if self.emptyMessage():
            return None
        retVal = self.seek()
        nxt = self.first.next
        del self.first
        self.first = nxt
        return retVal

    def queueToList(self):
        if self.emptyMessage():
            return []
        tmp = self.first
        retList = []
        while tmp != None:
            retList.append(tmp.getName())
            tmp = tmp.next
        return retList

    def emptyMessage(self):
        'returns True if we have an empty queue and prints End of Queue otherwise returns False'
        if self.first == None:
            print('End of Queue')
            return True
        return False

def main(someList = []):
    'A UI wrapper around the Queue class which mimics a command line allowing four distinct non-case sensitive commands'
    myQueue = Queue(someList)
    UI = ''
    print('\nAvailable commands:\nAdd, Seek, Pop, List\t(Not Case Sensitive)\nExit to quit\n\n')
    while UI.lower() != 'exit':
        UI = input('>>>\t')
        inputList = UI.split()
        if len(inputList) > 0:
            if inputList[0].lower() not in ('add', 'seek', 'pop', 'list', 'exit'):
                    print('That command is not recognized')
            elif inputList[0].lower() == 'add':
                if len(inputList) > 1:
                    myQueue.add(' '.join(inputList[1:]))
            elif not myQueue.emptyMessage():
                if inputList[0].lower() == 'seek':
                    print(myQueue.seek())
                if inputList[0].lower() == 'pop':
                    print(myQueue.pop())
                if inputList[0].lower() == 'list':
                    print('\n'.join(myQueue.queueToList()))
        
# main(['Song 1', 'Song 2', 'Song 3', 'Song 4', 'Song 5', 'Song 6', 'Song 7', 'Song 8', 'Song 9', 'Song 10', 'Song 11']) 
# main()
