from unittest import TestCase, main
from coral_client.book import *

class Test(TestCase):
    hotel_code = "HOTEL_CODE"
    prod_code = "PRODUCTION_CODE"
    book_code = "BOOK_CODE"
    book_info = {'name': '1,ali,osman,adult'}

    def __init__(self, *args, **kwargs):

        self.search_response = self.book.search({"pax": "1",
                                                "checkin": "2016-09-30",
                                                "checkout": "2016-10-03",
                                                "currency": "USD",
                                                "hotel_code": self.hotel_code,
                                                "client_nationality": "tr"})
        self.book = Book()
        self.book.login("USERNAME", "PASSWORD")
        super(Test, self).__init__(*args, **kwargs)

    def test_search(self):
        # self.assertEqual(200, self._search_resp.status_code)
        # resp = self._search_resp.json()
        self.assertGreaterEqual(self.search_response['count'], 1)
        self.assertIn('code', self.search_response['results'][0]['products'][0])

    def availability_test(self):
        availability_response = self.book.availability(self.prod_code)
        self.assertIsInstance(availability_response, dict)
        self.assertIn('meal_type', availability_response)
        self.assertIn('price', availability_response)
        self.assertIn('cost', availability_response)
        self.assertIsInstance(availability_response['rooms'], list)

    def provision_test(self):
        provision_response = self.book.provision(self.prod_code)
        self.assertIn('code', provision_response)

    def test_book_and_cancel(self):
        prov_code = self.book.provision(self.prod_code)['code']
        cancel_response = self.book.book(prov_code, self.book_info)
        self.assertIn('code', cancel_response)
        self.assertEqual('succeeded', cancel_response['status'])
        cancel_response = self.book.cancel(cancel_response['code'])
        self.assertIsInstance(cancel_response, dict)
        self.assertIn('code', cancel_response)

    def test_bookings(self):
        bookings_response = self.book.bookings()
        # self.assertEqual(200, resp.status_code)
        # resp = resp.json()
        self.assertIsInstance(bookings_response, list)

        bookings_response = self.book.bookings(self.book_code)
        # self.assertEqual(200, resp.status_code)
        # resp = resp.json()
        self.assertIsInstance(bookings_response, dict)

if __name__ == '__main__':
    main()