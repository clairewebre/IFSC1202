class User():
    def __init__(self,username,password):
        self.Username = username
        self.Password = password
class UserList():
    def __init__(self,filename):
        self.userlist = []
        self.filename = filename
    def ReadUserFile(self):
        userfile = open(self.filename, "r")
        x = userfile.readline()
        while x != "":
            username, password = x.split(",")
            user = User(username.strip(), password.strip())
            self.userlist.append(user)
            x = userfile.readline()
        userfile.close()
    def WriteUserFile(self):
        userfile = open(self.filename, "w")
        for i in range(len(self.userlist)):
            userfile.write(self.userlist[i].UserName + "," + self.userlist[i].Password + "\n")
    def DisplayUserList(self):
        print("{:>15s}{:>15s}".format("-"*15, "-"*15))
        for i in range(len(self.userlist)):
            if self.userlist[i].Username == username:
                return i
        return -1
    def FindUserName(self,username):
        for i in range(len(self.userlist)):
            if self.userlist[i].Username == username:
                return i
        return -1
    def ChangePassword(self, username, passwordchange):
        index = self.FindUserName(username)
        if index != -1:
            Strength = self.Strength(passwordchange)
            if Strength >= 5:
                self.userlist[index].Password = passwordchange
                print("Password Changed")
            else:
                print ("Password is weak")
        else:
            print("Username not found")
    def AddUser(self, username, password):
        if self.FindUserName(username) == -1:
            Strength = self.Strength(password)
            if strength >= 5:
                newuser = User(username,password)
                self.UserList.append(newuser)
                print ("User added")
            else:
                print("This password is weak -3")
        else:
            print("Username already exists")
    def DeleteUser(self.username):
        index = self.FindUserName(username)
        if index != -1:
            del self.UserList[index]
            print("User deleted")
        else:
            print("Username not found")
    def Strength(self,password):
        power = 0
        special = "~!@#$%^&*()_+|-={}[]:;<>?/"
        number = "0123456789"
        if len(password) >= 8:
            power += 1
        lowercasefound = False
        uppercasefound = False
        specialfound = False
        numberfound = False
        for i in range(len(password)):
            if password[i].isLowerCase():
                lowercasefound = True
            if password[i].isUpperCase():
                uppercasefound = True
            for j in range(len(special)):
                if password[i] == special[j]:
                    specialfound = True
            for j in range(len(number)):
                if password[i] == number[j]:
                    numberfound = True
        if lowercasefound == True:
            power += 1
        if uppercasefound == True:
            power += 1
        if specialfound == True:
            power += 1
        if numberfound == True:
            power += 1
        return power
userlist = UserList("Final Project Passwords.txt")
userlist.ReadUserFile()
print("1) Add a New User")
print("2) Delete an Existing User")
print("3) Change Password on an Existing User")
print("4) Display All Users")
print("5) Save Changes to File")
print("6) Quit")
choose = input("Enter Selection: ")
while choose != "6":
    if choose == "1":
        username = input("Enter a UserName: ")
        password = input("Enter a Password: ")
        userlist.AddUser(username, password)
    elif choose == "2":
        username = input("Enter UserName to Delete: ")
        userlist.DeleteUser(username)
    elif choose == "3":
        username = input("Enter UserName: ")
        password = input("Enter a New Password: ")
        userlist.ChangePassword(username,password)
    elif choose == "4":
        userlist.display_UserList()
    elif choose == "5":
        userlist.WriteUserFile()
        print("Changes Saved")
    elif choice == "6":
        userlist.WriteUserFile()
        print("Exited Program")
    else:
        print("Invalid Selection")
    print("1) Add a New User")
    print("2) Delete an Existing User")
    print("3) Change Password on an Existing User")
    print("4) Display All Users")
    print("5) Save Changes to File")
    print("6) Quit")
    choose = input("Enter Selection: ")

