from unittest import TestCase, main
from coral_client.book import Book

class Test(TestCase):
    product_code = "EEG0IV4hIAAAAAAAAAAAAAAAAAAAAAAAAAHAd2Xs9NqCR76uaz0dBhCaHf_9gAAAAAAAAAAAAAK0gAAAAAL8IOBOgJM0tYl0amtWABIAgAAAAAAAAAAABA"
    book_code = "BVGZGTUAMEBH"
    search_params = {'checkin': '2016-10-30', 'checkout': '2016-11-03',
                     'pax': '1', 'hotel_code': '1041b4', 'client_nationality': 'tr', 'currency': 'USD'}

    book_info = {'name': '1,test,test,adult'}
    book = Book()
    book.login("yucealiosman", "5")
    search_resp = book.search(search_params)

    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)

    def test_search(self):
        self.assertGreaterEqual(self.search_resp['count'], 1)
        self.assertIn('code', self.search_resp['results'][0]['products'][0])

    def test_availability(self):
        resp = self.book.availability(self.product_code)
        self.assertIsInstance(resp, dict)
        self.assertIn('price', resp)
        self.assertIn('cost', resp)
        self.assertIsInstance(resp['policies'], list)

    def test_provision(self):
        resp = self.book.provision(self.product_code)
        self.assertIn('code', resp)

    def test_book_and_cancel(self):
        prov_code = self.book.provision(self.product_code)['code']
        resp = self.book.book(prov_code, self.book_info)
        self.assertEqual('succeeded', resp['status'])
        resp = self.book.cancel(resp['code'])
        self.assertIsInstance(resp, dict)
        self.assertIn('code', resp)

    def test_bookings(self):
        resp = self.book.bookings()
        self.assertIsInstance(resp, list)

if __name__ == '__main__':
    main()