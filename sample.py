from coral_client import book
import getpass
""" We create sample variables to invoke functions   """
search_params = {'checkin': '2016-09-30', 'checkout': '2016-10-03',
                 'pa33x': '1', 'destination_code': '19122', 'client_nationality': 'tr', 'currency': 'USD'}
book_info = {'name': '1,Ali,Yuce,adult'}
product_code = 'GcNhIT4ZIAAAAAAAAAAAAAAAAAAAAAAAAAHA7IuWF1ubQJWweN6xotOAwf_9gAAAAAAAAAAAABqbAAAAABqbEECK' \
               'gJQeolO-Lmz4AAIRgAAAAAAAAAAABA'
book_code = 'BCHNPST36ZC3'
user_name = raw_input('Please Enter Username: ')
user_password = getpass.getpass('Please Enter Password: ')

""" We call all functions(search,provision,avab etc.) with using our book_instance object """
book_instance = book.Book()
book_instance.login(user_name, user_password)
print book_instance.search(search_params)
book_instance.availability(product_code)
book_instance.provision(product_code)
book_instance.cancel(book_code)
book_instance.bookings()
