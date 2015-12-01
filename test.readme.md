FORMAT: 1A
HOST: http://scalebridge.appspot.com/api

# scalebridge

Scalebridge is an API solution to establish integrations among different partners.

In order to perform operations on ScaleBridge, you need to obtain a 'session_token' from the API first. Refer to Authentication into how obtain this session_token, once obtained simply bundle it on the request, either by using a header or by using a query string parameter.

## Messaging API [/messaging]
This resource is used to post a Message into ScaleBridge.


### Post a Message [POST]
+ Request

    + Headers

            session_token: "ab2b414bac2456469139a2bc32619919"
            Content-Type: <specify>
    + Body

            {}
+ Response 200 (application/json)

    + Headers

            x: y
    + Body

            {}

## Customer API [/api/customer]
This resource is used to interact with registered Customers.

## Customer Creation [/api/customer/]

## Create a Customer [POST]

+ Request
    + Headers
        session_token: "ab2b414bac2456469139a2bc32619919"
    + Body
        {
            'name': 'Google',
            'contact_email': 'eric.smith@google.com',
            'address': '1 Infinite Loop'
        }

+ Response 200 (application/json)
    + Body
        2f7a717abd1447449232e7fa73351204


## Retrieve a Customer [/api/customer/{customer_id}]
+ Parameters
    + customer_id: 2f7a717abd1447449232e7fa73351204 (required, guid) - ID of the Customer

## Retrieve a Customer [GET]
+ Request
    + Headers
        session_token: "ab2b414bac2456469139a2bc32619919"

+ Response 200 (application/json)
    + Body
        {
            'id': "2f7a717abd1447449232e7fa73351204",
            'name': 'Google',
            'email': 'eric.smith@google.com',
            'address': '1 Infinite Loop'
        }

## Update a Customer [PUT]

+ Request
    + Headers
        session_token: "ab2b414bac2456469139a2bc32619919"
    + Body
        {
            'id': "2f7a717abd1447449232e7fa73351204",
            'name': 'Google',
            'contact_email': 'eric.smith@google.com',
            'address': '1 Infinite Loop'
        }

+ Response 200 (application/json)
    + Body
        2f7a717abd1447449232e7fa73351204

## Delete a Customer [DELETE]

+ Request
    + Headers
        session_token: "ab2b414bac2456469139a2bc32619919"

+ Response 204

