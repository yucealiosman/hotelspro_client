from coral_client import book
import getpass
""" We create sample variables to invoke functions   """
search_params = {'checkin': '2016-10-30', 'checkout': '2016-11-03',
                 'pax': '1', 'destination_code': '19122', 'client_nationality': 'tr', 'currency': 'USD'}
book_info = {'name': '1,Test,Test,adult'}
product_code = 'EEG0IV4hIAAAAAAAAAAAAAAAAAAAAAAAAAHAd2Xs9NqCR76uaz0dBhCaHf_9gAAAAAAAAAAAAAK0gAAAAAL8IOBOgJM0tYl0amtWABIAgAAAAAAAAAAABA'
book_code = 'BCHNPST36ZC3'
user_name = raw_input('Please Enter Username: ')
user_password = getpass.getpass('Please Enter Password: ')

""" We call all functions(search,provision,avab etc.) with using our book_instance object """
book_instance = book.Book()
book_instance.login(user_name, user_password)
book_instance.search(search_params)
print book_instance.availability(product_code)

book_instance.bookings()
