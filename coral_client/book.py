import  requests

class Book:
    def __init__(self):
        self.user_name = ''
        self.user_password = ''
        self.BASE_URL = 'http://localhost:8000/api/v2'
        self.SEARCH_URL = self.BASE_URL + '/search/?'
        self.AVAILABILITY = self.BASE_URL + '/availability/'
        self.PROVISION_URL = self.BASE_URL + '/provision/'
        self.BOOK_URL = self.BASE_URL + '/book/'
        self.CANCEL_URL = self.BASE_URL + '/cancel/'
        self.BOOKINGS_URL = self.BASE_URL + '/bookings'

    def login(self, user_name, user_pas):
        """ Authentication for CoralAPI """
        self.user_name, self.user_password = user_name, user_pas
        request = self.create_get_request(self.BASE_URL)
        if request.status_code != 200:
            print 'Wrong UserId or Password'
            exit()

    def create_get_request(self, url):
        return requests.get(url, auth=(self.user_name, self.user_password))

    def create_post_request(self, url, pay_load=None):
        return requests.post(url, auth=(self.user_name, self.user_password), data=pay_load)

    def search(self, params):
        for item in params:
            self.SEARCH_URL = self.SEARCH_URL + str(item) + '=' + str(params[item]) + '&'
        request = self.create_get_request(self.SEARCH_URL)

        if request.status_code == 200:
            return request.json()
        else:
            print "Search Error Code:", str(request.status_code)

    def availability(self, product_code):
        url = '{}{}'.format(self.AVAILABILITY, product_code)
        request = self.create_get_request(url)
        if request.status_code == 200:
            return request.json()
        else:
            print "Availability Error Code:", str(request.status_code)

    def provision(self, product_code):
        url = '{}{}'.format(self.PROVISION_URL, product_code)
        request = self.create_post_request(url)
        if request.status_code == 200:
            return request.json()
        else:
            print "Provision Error Code:", str(request.status_code)

    def book(self, provision_code, book_info):
        url = '{}{}'.format(self.BOOK_URL, provision_code)
        request = self.create_post_request(url, book_info)
        if request.status_code == 200:
            return request.json()
        else:
            print "Book Error Code:", str(request.status_code)

    def cancel(self, book_code):
        url = self.CANCEL_URL + str(book_code)
        request = self.create_post_request(url)
        if request.status_code == 200:
            return request.json()
        else:
            print "Cancel Error Code:", str(request.status_code)

    def bookings(self, book_code=''):
        url = self.BOOKINGS_URL + book_code
        request = self.create_get_request(url)
        if request.status_code == 200:
            return request.json()
        else:
            print "Bookings Error Code:", str(request.status_code)
