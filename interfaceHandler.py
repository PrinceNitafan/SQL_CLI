import pyodbc as pdb
import loginPage
import mainMenuPage
import searchBusinessPage
import searchUserPage
import makeFriendPage
import reviewBusinessPage


class InterfaceHandler:
    def __init__(self):
        self.connection = self.create_connection()
        self.running = True
        self.currPage = 'log_in'

        # Creating page objects #
        self.log_in = loginPage.LogIn(self)
        self.main_menu = mainMenuPage.MainMenu(self)
        self.search_business = searchBusinessPage.SearchBusiness(self)
        self.search_users = searchUserPage.SearchUsers(self)
        self.make_friend = makeFriendPage.MakeFriend(self)
        self.review_business = reviewBusinessPage.ReviewBusiness(self)

        # Log In Variables #
        self.user_id = None

    def currentPage(self):
        if self.currPage == 'log_in':
            self.log_in.run()
        elif self.currPage == 'main_menu':
            self.main_menu.run()
        elif self.currPage == 'search_business':
            self.search_business.run()
        elif self.currPage == 'search_users':
            self.search_users.run()
        elif self.currPage == 'make_friend':
            self.make_friend.run()
        elif self.currPage == 'review_business':
            self.review_business.run()
        elif self.currPage == 'quit':
            self.interfaceClosing()

    def updateCurrPage(self, newPage):
        self.currPage = newPage

    def spc(self):
        print('\n')
    def create_connection(self):
        DB_host = ''; DB_name = ''; DB_user = ''; DB_password = ''
        connection_str = ('Driver={SQL Server};Server=' + DB_host +
                          ';Database=' + DB_name + ';UID=' + DB_user+';PWD=' + DB_password + ';')
        connection = pdb.connect(connection_str)
        return connection

    def updateUserID(self, userID):
        self.user_id = userID

    def interfaceRunning(self):
        return self.running

    def interfaceClosing(self):
        print('The interface is closing.')
        self.connection.close()
        self.running = False

