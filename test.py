from unittest import TestCase, main
from coral_client.book import Book


class Test(TestCase):
    search_params = {'checkin': '2016-11-30', 'checkout': '2016-12-03',
                     'pax': '1', 'destination_code': '19122',
                     'client_nationality': 'tr', 'currency': 'USD'}
    book_info = {'name': '1,test,test,adult'}
    book = Book()
    book.login("yucealiosman", "5")
    search_resp = book.search(search_params)

    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)

    def test_search(self):
        #import ipdb; ipdb.set_trace()
        self.assertGreaterEqual(self.search_resp[0]['count'], 1)
        self.assertIn('code', self.search_resp[0]['results'][0]['products'][0])
        self.assertEqual(200, self.search_resp[1])
        """Test failed situation"""
        with self.assertRaisesRegexp(ValueError, 'error_code'):
            self.book.search({'checki3n': '2016-10-30',
                              'checkout': '2016-11-03',
                              'pax': '1', 'destination_code': '19122',
                              'client_nationality': 'tr',
                              'currency': 'USD'})

        with self.assertRaises(TypeError):
            self.book.search()

    def test_availability(self):
        resp = self.book.availability(self.search_resp[0]
                                      ['results'][0]['products'][0]['code'])
        self.assertIsInstance(resp[0], dict)
        self.assertEqual(200, resp[1])

        with self.assertRaises(TypeError):
            self.book.availability()

        with self.assertRaises(ValueError):
            self.book.availability({"wrong_param"})

    def test_provision(self):
        resp = self.book.provision(self.search_resp[0]
                                   ['results'][0]['products'][0]['code'])
        self.assertIn('code', resp[0])
        self.assertEqual(200, resp[1])
        self.assertIsInstance(resp[0], dict)

        """Test failed situation"""
        with self.assertRaises(TypeError):
            self.book.provision()

        with self.assertRaises(ValueError):
            self.book.provision({"wrong_param"})

    def test_book(self):
        prov_response = self.book.provision(self.search_resp[0]
                                            ['results'][0]
                                            ['products'][0]['code'])
        prov_code = prov_response[0]['code']
        resp = self.book.book(prov_code, self.book_info)
        self.assertEqual(200, resp[1])
        self.assertIsInstance(resp[0], dict)
        self.assertIn('code', resp[0])
        self.book.cancel(resp[0]['code'])

        """Test failed situation"""
        with self.assertRaises(TypeError):
            self.book.book()
        with self.assertRaises(ValueError):
            self.book.availability({"wrong_param"})

    def test_cancel(self):
        prov_response = self.book.provision(self.search_resp[0]
                                            ['results'][0]
                                            ['products'][0]['code'])
        prov_code = prov_response[0]['code']
        #import ipdb; ipdb.set_trace()
        resp = self.book.book(prov_code, self.book_info)
        cancel_response = self.book.cancel(resp[0]['code'])
        self.assertEqual(200, cancel_response[1])
        self.assertIsInstance(cancel_response[0], dict)

        """Test failed situation"""
        with self.assertRaises(TypeError):
            self.book.cancel()

        with self.assertRaises(ValueError):
            self.book.cancel({"wrong_param"})

    def test_bookings(self):
        resp = self.book.bookings()
        self.assertIsInstance(resp[0], list)
        self.assertEqual(200, resp[1])
        #import ipdb; ipdb.set_trace()
        prov_response = self.book.provision(self.search_resp[0]
                                            ['results'][0]
                                            ['products'][2]['code'])
        prov_code = prov_response[0]['code']
        resp = self.book.book(prov_code, self.book_info)
        bookings_response = self.book.bookings(resp[0]['code'])
        self.assertIsInstance(bookings_response[0], dict)
        self.assertEqual(200, bookings_response[1])
        self.book.cancel(resp[0]['code'])

        """Test failed situation"""
        with self.assertRaises(ValueError):
            self.book.bookings("wrong_param")

if __name__ == '__main__':
    main()
