
class SearchBusiness:
    def __init__(self, interface):
        self.interface = interface
        self.connection = interface.connection

        # Filter variables #
        self.name = ''
        self.city = ''
        self.number_of_stars = ''
        self.order_by = ''

    def search_business(self):
        print('SEARCH BUSINESS: Enter an option number to change a filter. ')
        currentFilters = ('Name = \'' + self.name + '\', City = \'' + self.city + '\', Min # of Stars = \''
                          + self.number_of_stars + '\', Order by = \'' + self.order_by + '\'')
        print('Current Filters: ' + currentFilters + '.')
        print('Filter Options: (1) Name, (2) City, (3) Min # of Stars, (4) Order by, (r) Run Search,'
              ' (e) exit Search Business.')
        user_input = input("Enter your option: ").strip()
        self.spc()

        if user_input == '1':
            self.name_filter()
        elif user_input == '2':
            self.city_filter()
        elif user_input == '3':
            self.star_filter()
        elif user_input == '4':
            self.order_by_filter()
        elif user_input == 'e':
            self.exit_search_business()
        elif user_input == 'r':
            self.run_search()
        else:
            print('Invalid Input: your option input \'' + user_input + '\' is invalid, please try again.')
            self.spc()

    def name_filter(self):
        print('Name Filter: (To clear filter, enter nothing)')
        user_input = input('Enter a name to update filter: ').strip()
        self.spc()

        if len(user_input) == 0:
            print('You entered nothing, clearing the Name filter.')
            self.spc()
            self.name = ''
            return

        self.name = user_input
        print('Name filter has been updated to: \'' + user_input + '\'')
        self.spc()

    def city_filter(self):
        print('City Filter: (To clear filter, enter nothing)')
        user_input = input('Enter a city to update filter: ').strip()
        self.spc()

        if len(user_input) == 0:
            print('You entered nothing, clearing the Min # of stars filter.')
            self.spc()
            self.city = ''
            return

        self.city = user_input
        print('City filter has been updated to: \'' + user_input + '\'')
        self.spc()

    def star_filter(self):
        print('Min # of Stars Filter: Input number must be >= 1.0 and <= 5.0 (1.0 >= input <= 5.0),'
              ' and can only be up to one decimal place (e.g. 2.2).')
        print('(To clear filter, enter nothing)')
        user_input = input('Enter a number to update filter: ').strip()
        self.spc()

        # Checking if the number can be a float
        if len(user_input) == 0:
            print('You entered nothing, clearing the Min # of Stars filter.')
            self.spc()
            self.number_of_stars = ''
            return

        try:
            min_stars = float(user_input)
        except ValueError:
            print('Invalid input: your input \'' + user_input + '\' is not valid, please try again.')
            self.number_of_stars = ''
            self.spc()
            return

        if '.' in user_input:
            non_decimal, decimal = user_input.split('.')
            if len(decimal) > 1:
                print('Invalid star input: your input \'' + user_input + '\' is not valid, please try again.')
                self.number_of_stars = ''
                self.spc()
                return

        if min_stars < 1.0:
            print('Invalid star input: your number input \'' + user_input + '\' is less than 1.0. Please try again.')
            self.number_of_stars = ''
            self.spc()
            return

        if min_stars > 5.0:
            print('Invalid star input: your number input \'' + user_input + '\' is greater than 5.0. '
                                                                            'Please try again.')
            self.number_of_stars = ''
            self.spc()
            return

        print('Min # of Stars filter has been updated to \'' + user_input + '\'.')
        self.number_of_stars = user_input
        self.spc()

    def order_by_filter(self):
        print('Order by: (1) Name [a-z], (2) City [a-z], (3) Stars [small-big]. Enter nothing to clear filter.')
        user_input = input('Enter an option number to set filter: ').strip()
        self.spc()

        if len(user_input) == 0:
            print('You entered nothing, clearing Order by filter.')
            self.order_by = ''
            return

        if user_input == '1':
            self.order_by = 'name'
        elif user_input == '2':
            self.order_by = 'city'
        elif user_input == '3':
            self.order_by = 'stars'
        else:
            print('Invalid option input, please try again.')

    def run_search(self):
        sqlStatement = ('SELECT business_id, name, address, city, stars '
                        'FROM business')
        sqlWHERE = ' WHERE'

        filter_count = 0
        # Getting name variable
        if len(self.name) != 0:
            sqlWHERE += ' name LIKE \'%' + self.name + '%\''
            filter_count += 1

        # Getting city variable
        if len(self.city) != 0:
            if filter_count != 0:
                sqlWHERE += ' AND city = \'' + self.city + '\''
            else:
                sqlWHERE += ' city = \'' + self.city + '\''
            filter_count += 1

        # Getting stars variable
        if len(self.number_of_stars) != 0:
            if filter_count != 0:
                sqlWHERE += ' AND stars >= ' + self.number_of_stars
            else:
                sqlWHERE += ' stars >= ' + self.number_of_stars
            filter_count += 1

        if filter_count != 0:
            sqlStatement += sqlWHERE

        # Getting order by variable
        if len(self.order_by) != 0:
            sqlStatement += ' ORDER BY ' + self.order_by

        cursor = self.connection.cursor()
        cursor.execute(sqlStatement)

        row = cursor.fetchone()
        currentFilters = ('Name = \'' + self.name + '\', City = \'' + self.city + '\', Min # of Stars = '
                          + str(self.number_of_stars) + ', Order by = \'' + self.order_by + '\'')
        if row is None:
            print('Result is empty with current set of filters: ' + currentFilters + '.')
            cursor.close()
            self.spc()
            return

        self.spc()

        row_count = 0
        while row is not None:
            print('| Business ID: ' + str(row[0]) + ' | Name: ' + str(row[1]) + ' | Address: ' + str(row[2]) +
                  ' | City: ' + str(row[3]) + ' | Stars: ' + str(row[4]) + ' |')
            row = cursor.fetchone()
            row_count += 1
        print('You have ' + str(row_count) + ' results with current filters: ' + currentFilters)
        self.spc()
        cursor.close()

        while True:
            print('Choose what to do next: (1) Continue to search businesses, (2) Review a business, '
                  '(e) exit from Search Business')
            user_input = input('Enter option: ').strip()
            self.spc()

            if user_input == '1':
                return
            elif user_input == '2':
                self.go_to_review_business()
                return
            elif user_input == 'e':
                self.exit_search_business()
                return
            else:
                print('Invalid option input: please try again.')
                self.spc()

    def exit_search_business(self):
        self.name = ''
        self.city = ''
        self.number_of_stars = ''
        self.order_by = ''
        self.interface.updateCurrPage('main_menu')

    def go_to_review_business(self):
        self.name = ''
        self.city = ''
        self.number_of_stars = ''
        self.order_by = ''
        self.interface.updateCurrPage('review_business')

    def spc(self):
        print('\n')

    def run(self):
        self.search_business()