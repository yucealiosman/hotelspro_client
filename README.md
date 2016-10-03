# README #

    This README would normally document whatever steps are necessary to get your application up and running.

# Booker #

    A python client library for CoralPro

    Version 1.0.0

    Learn : https://bitbucket.org/yuceali/coral_client/

# Installation #

    $ python setup.py install

# Usage #

    from coral_client import book

## Example : search() ##

    

    search_params = {'checkin': '2016-10-30', 'checkout': '2016-11-03',
                 'pax': '1', 'destination_code': '19122', 'client_nationality': 'tr', 'currency': 'USD'}
    book_info = {'name': '1,Ali,Yuce,adult'}             
    book_instance = book.Book()
    book_instance.login(user_name, user_password)
    book_instance.search(search_params)
    
### Response ###
    {
    u'client_nationality': u'tr',
    u'status': u'succeeded',
    u'hotel_payment_info': [
        {
        u'hotel_currency': None,
        u'hotel_price': None
        }
    ],
    u'code': u'BWEQNCK9CTQL',
    u'destination_code': u'206ec',
    u'nonrefundable': False,
    u'provider_args': [

    ],
    u'minimum_selling_price': None,
    u'created_at': u'2016-09-28 11:39:24.925080+00:00',
    u'hotel_code': u'135f3a',
    u'currency': u'GBP',
    u'confirmation_numbers': [
        {
        u'confirmation_number': u'164-2867477',
        u'agency_ref_id': u'N/A',
        u'cost': u'150.85',
        u'rooms': [
            {
            u'room_description': u'TWIN WITH SHARED BATHROOM',
            u'room_type': u'TWN-U02'
            }
        ],
        u'provider': u'hbeds',
        u'names': [
            u'TEST TEST'
        ]
        }
    ],
    u'pay_at_hotel': False,
    u'mealtype_code': u'BC',
    u'special_request': None,
    u'policies': [
        {
        u'ratio': u'0.33',
        u'days_remaining': 4
        }
    ],
    u'price': u'150.85',
    u'checkout': u'2016-10-03',
    u'checkin': u'2016-09-30',
    u'view': False
    }