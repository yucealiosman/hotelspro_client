import requests


class Book(object):
    def __init__(self):
        self.user_name = ''
        self.user_password = ''
        self.BASE_URL = 'http://localhost:8000/api/v2'
        self.SEARCH_URL = self.BASE_URL + '/search/?'
        self.AVAILABILITY = self.BASE_URL + '/availability/%s'
        self.PROVISION_URL = self.BASE_URL + '/provision/%s'
        self.BOOK_URL = self.BASE_URL + '/book/%s'
        self.CANCEL_URL = self.BASE_URL + '/cancel/%s'
        self.BOOKINGS_URL = self.BASE_URL + '/bookings/%s'

    def login(self, user_name, user_pas):
        """ Authentication for CoralAPI """
        self.user_name, self.user_password = user_name, user_pas
        response = self.create_get_request(self.BASE_URL)
        if response.status_code != 200:
            raise ValueError(response.json(), response.status_code)

    def create_get_request(self, url, params=None):
        return requests.get(url, params=params,
                            auth=(self.user_name, self.user_password))

    def create_post_request(self, url, data=None,):
        return requests.post(url, data=data,
                             auth=(self.user_name, self.user_password))

    def search(self, params):
        response = self.create_get_request(self.SEARCH_URL, params=params)
        if response.status_code == 200:
            return response.json(), response.status_code
        else:
            raise ValueError(response.json(), response.status_code)

    def availability(self, product_code):
        response = self.create_get_request(self.AVAILABILITY % product_code)
        if response.status_code == 200:
            return response.json(), response.status_code
        else:
            raise ValueError(response.json(), response.status_code)

    def provision(self, product_code):
        response = self.create_post_request(self.PROVISION_URL % product_code)
        if response.status_code == 200:
            return response.json(), response.status_code
        else:
            raise ValueError(response.json(), response.status_code)

    def book(self, provision_code, book_info):
        response = self.create_post_request(self.BOOK_URL % provision_code,
                                            data=book_info)
        if response.status_code == 200:
            return response.json(), response.status_code
        else:
            raise ValueError(response.json(), response.status_code)

    def cancel(self, book_code):
        response = self.create_post_request(self.CANCEL_URL % str(book_code))
        if response.status_code == 200:
            return response.json(), response.status_code
        else:
            raise ValueError(response.json(), response.status_code)

    def bookings(self, book_code=''):
        response = self.create_get_request(self.BOOKINGS_URL % book_code)
        if response.status_code == 200:
            return response.json(), response.status_code
        else:
            raise ValueError(response.json(), response.status_code)
