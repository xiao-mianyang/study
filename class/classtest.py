#!/usr/bin/env python3

class UserData:
    def __init__(self, ID, Name):
        self.ID = ID
        self.Name = Name
        print('ID:{} Name:{}'.format(self.ID, self.Name))
    




if __name__ == '__main__':
    user1 = UserData(101, 'Jack')
    user2 = UserData(102, 'Louplus')
    #print(user1)
    #print(user2)




