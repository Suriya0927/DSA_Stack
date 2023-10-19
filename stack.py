class myStack:
    def __init__(self):
        self.index = -1
        self.stack = []

    def push(self, ele, limit):
        self.index += 1
        if limit > self.index:
            self.stack.append(ele)
            return ele,' added into stack'
        else:
            self.index -= 1
            return f'Reached list size {limit}. No more push allowed'
        
    def pop(self):
        if self.index == -1:
            return 'List is EMPTY. We cannot pop'
        else:
            self.temp = self.stack[self.index]
            self.index -= 1
            self.stack.pop()
            return self.temp,' removed from stack'

    def peek(self):
        return 'TOP STACK IS: ',self.stack[self.index]

    def isEmpty(self):
        if self.index == -1:
            return 'Stack is EMPTY'
        else:
            return 'Stack is NOT EMPTY'


user_input=''
x=myStack()
limit = int(input('Enter list size: '))
while user_input != '0':
    print('')
    print('1.PUSH | 2.POP | 3.PEEK | 4.isEMPTY | 5.SHOW LIST | 0.EXIT')
    user_input=input('Enter: ')

    if user_input == '1': #PUSH
        push_input=input('enter push value: ')
        print(x.push(push_input, limit))
        print('STACK: ', x.stack)

    elif user_input == '2': #POP
        print(x.pop())
        print('STACK: ', x.stack)

    elif user_input == '3': #PEEK
        print(x.peek())
        
    elif user_input == '4': #CHECK IF EMPTY
        print(x.isEmpty())
        print(x.stack)

    elif user_input == '5': #SHOW LIST
        print(x.stack)
    elif user_input == '0': #EXIT
        print('EXITED!')