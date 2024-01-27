from datetime import datetime
import random
import string


class ReviewBusiness:
    def __init__(self, interface):
        self.interface = interface
        self.connection = interface.connection

    def review_business(self):
        print('REVIEW BUSINESS: case-sensitive. (Enter nothing to exit Review Business)')
        user_input = input('Enter a business ID to review for: ')
        self.spc()

        if len(user_input) == 0:
            self.exit_review_business()
            return

        check_business_id = self.search_business_id(user_input)
        if check_business_id is False:
            print('Invalid business ID: Cannot find business ID \'' + user_input + '\', please try again.')
            self.spc()
            return

        print('Business ID \'' + user_input + '\' found!')
        self.spc()

        while True:
            number_input = self.star_rating()
            if number_input == '0.0':
                print('You entered nothing, canceling review.')
                self.spc()
                return
            elif number_input == '0.1':
                print('Invalid star input, please try again.')
                self.spc()
            else:
                stars_input = number_input
                break

        # generating the reviewid and datetime
        review_id = self.generate_review_id()
        curr_datetime = self.get_curr_date()

        sqlStatement = ('INSERT INTO review(review_id, user_id, business_id, stars, useful, funny, cool, date) '
                        'VALUES(?,?,?,?,0,0,0,?) ')
        cursor = self.connection.cursor()
        cursor.execute(sqlStatement, review_id, self.interface.user_id, user_input, stars_input, curr_datetime)
        cursor.commit()

        if cursor.rowcount > 0:
            print('Review has been made for business ID \'' + user_input + '\'!')
        else:
            print('Review was not made. Please try again.')
        cursor.close()
        self.spc()

        while True:
            print('Choose what to do next: (1) Continue to review businesses, (e) exit from Review Business.')
            user_input = input('Enter option: ').strip()
            self.spc()

            if user_input == '1':
                return
            elif user_input == 'e':
                self.exit_review_business()
                return
            else:
                print('Invalid option input: Please try again.')
                self.spc()

    def search_business_id(self, business_id_input) -> bool:
        cursor = self.connection.cursor()
        cursor.execute('SELECT business_id '
                       'FROM business '
                       'WHERE business_id = \'' + business_id_input + '\'')

        row = cursor.fetchone()
        while row is not None:
            if row[0] == business_id_input:
                cursor.close()
                return True
            row = cursor.fetchone()

        cursor.close()
        return False

    def star_rating(self) -> str:
        while True:
            print('Business Star Rating: Input number must be >= 1 and <= 5 (1 >= input <= 5),'
                  ' and no decimals places (e.g. 2).')
            print('(Enter nothing to cancel review)')
            user_input = input('Enter your number for star rating: ')
            self.spc()

            # user cancels the review if they don't enter anything
            if len(user_input) == 0:
                return '0.0'

            try:
                min_stars = int(user_input)
            except ValueError:
                return '0.1'

            if min_stars < 1:
                return '0.1'

            if min_stars > 5:
                return '0.1'

            return user_input

    def generate_review_id(self) -> str:
        keep_generating = True
        new_review_ID = ''
        while keep_generating:
            new_review_ID = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=22))
            cursor = self.connection.cursor()
            cursor.execute('SELECT review_id '
                           'FROM review '
                           'WHERE business_id = \'' + new_review_ID + '\'')

            keep_generating = False
            for row in cursor:
                if row[0] == new_review_ID:
                    keep_generating = True
            cursor.close()

        return new_review_ID

    def get_curr_date(self) -> str:
        curr_date = datetime.now()
        string_date = curr_date.strftime('%d-%m-%Y %H:%M:%S')
        return string_date

    def exit_review_business(self):
        self.interface.updateCurrPage('main_menu')

    def spc(self):
        print('\n')

    def run(self):
        self.review_business()

