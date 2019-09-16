class UserData:

    group = 'shiyanlou-louplus'

    def __init__(self, ID, name):
        self.ID = ID
        self._name = name

    #def __repr__(self):
        #return 'ID:{} Name:{}'.format(self.ID, self._name)


class NewUser(UserData):
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if len(str(value))<=3:
            print('ERROR')
        else:
            self._name = value
    
    @classmethod
    def get_group(cls):
        return cls.group

    @staticmethod
    def format_userdata(user_id,user_name):
        print('{}\'s id is {}'.format(user_name, user_id))
    


        
if __name__ == '__main__':
    # 调用 NewUser 类继承的 UserData 类中的 __init__ 方法生成实例 user1 
    #user1 = NewUser(101, 'Jack')  
    # 调用实例的 set_name 方法修改私有属性 _name
    #user1.set_name('Jackie')      
    # 调用 NewUser 类继承的 UserData 类中的 __init__ 方法生成实例 user2
    #user2 = NewUser(102, 'Louplus')
    # 打印实例，调用 __repr__ 方法
    #print(user1)
    #print(user2)
    #print(NewUser.get_group())
    #NewUser.format_userdata(109,'Lucy')
    user1 = NewUser(101, 'Jack')
    user1.name = 'Lou'
    user1.name = 'Jackie'
    user2 = NewUser(102,'Louplus')
    print(user1.name)
    print(user2.name)




