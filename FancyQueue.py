class Queue(object):

    class Node(object):
        'A wrapper around a str with a recursive reference to another Node'
        def __init__(self, name, nxt = None):
            'sets the two fields (str/Node)'
            self.title = name
            self.next = nxt # pointer to the next element
        def getName(self):
            'returns title'
            return self.title
        def changeName(self, name):
            'sets title to name'
            self.name = name

    def __init__(self, someList = []):
        '''initilizes a Queue of Nodes, one for each str elem
        The first element will be the first Node and the order of elems will be maintained'''
#        if any( type(element) != str for element in someList ):
#            raise('Non-String element found in list\nExpected only string values')
        self.first = None # First or next element of the queue
        self.last = None # Last element in the queue
        self.length = len(someList)
        if someList:
            for j in range(len(someList)):
                i = len(someList) - (j + 1)
                if i == len(someList) - 1:
                    self.last = self.Node(someList[i])
                    self.first = self.last
                else:
                    self.first = self.Node(someList[i], self.first)

    def next(self, someStr):
        'This method is not a traditional functionality of a Queue but does exist in several instances including music queues of popular music streaming services'
        'This allows you to add a Node not to the end but to the front where it will be next'
        self.length += 1
        if self.first == None:
            self.last = self.Node(someStr)
            self.first = self.last
        else:
            self.first = self.Node(someStr, self.first)

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

def myNext(myQueue, inputList):
    if len(inputList) > 1:
        myQueue.next(' '.join(inputList[1:]))
def myAdd(myQueue, inputList):
    if len(inputList) > 1:
        myQueue.add(' '.join(inputList[1:]))
def mySeek(myQueue, inputList):
    if not myQueue.emptyMessage():
        print(myQueue.seek())
def myPop(myQueue, inputList):
    if not myQueue.emptyMessage():
        print(myQueue.pop())
def myList(myQueue, inputList):
    if not myQueue.emptyMessage():
        print('\n'.join(myQueue.queueToList()))

def main(someList = []):
    'A UI wrapper around the Queue class which mimics a command line allowing six distinct non-case sensitive commands, two of which are redundant (list & ls)'
    'Unlike the Queue class I defined, the nodes in this Queue must be used to store strings'
    if any( type(element) != str for element in someList ):
        raise('Non-String element found in list\nExpected only string values')
    myQueue = Queue(someList)
    switch = {'next' : myNext, 'add' : myAdd, 'seek' : mySeek, 'pop' : myPop, 'list' : myList, 'ls' : myList}
    print('\nAvailable commands:\nSeek, Pop, Add, Next, List, LS\t(Not Case Sensitive)\nAdd and Next take an argument\t(ex: add Hello World)\nExit to quit\n\n')
    UI = input('>>>\t')
    while UI.lower() != 'exit':
        inputList = UI.split()
        if len(inputList) > 0:
            try:
                switch[inputList[0].lower()](myQueue, inputList)
            except:
                    print('That command is not recognized')
        UI = input('>>>\t')

# These are sample ways of calling my main function. The first involves a situation where you'd like to initilize a non-empty Queue specifically for 11 songs.
main(['Song 1', 'Song 2', 'Song 3', 'Song 4', 'Song 5', 'Song 6', 'Song 7', 'Song 8', 'Song 9', 'Song 10', 'Song 11']) 
# main()
