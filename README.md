
#  Vendor Management System with Performance Metrics

## Introduction

Welcome to the Vendor Management System with Performance Metrics! This system is built using Django and Django REST Framework to handle vendor profiles, track purchase orders, and calculate vendor performance metrics.

## Core Features

1. **Vendor Profile Management**
   - Create, retrieve, update, and delete vendor profiles.
   - Store vendor information including name, contact details, address, and a unique vendor code.

2. **Purchase Order Tracking**
   - Create, retrieve, update, and delete purchase orders.
   - Track details of each purchase order such as PO number, vendor reference, order date, items, quantity, and status.

3. **Vendor Performance Evaluation**
   - Calculate performance metrics including:
     - On-Time Delivery Rate
     - Quality Rating Average
     - Average Response Time
     - Fulfillment Rate

## Requirements.

- **Python** (-Version 3.x)
- **Django**
- **Django REST Framework**

## **Setup Requirements.**


## Create a Virtual Environment.
  - pip install virtualenv
  - python -m virtualenvname

##  Install Requirements:
- pip install django
- pip install djangorestframework
- pip install python

## **Setup a new project with a single application.**

- django-admin startproject Vendor_system
- cd Vendor_system
- python manage.py startapp vendor

## Database migration:
 - python manage.py migrate
 - python manage.py makemigrations
 - python manage.py migrate

## Superuser Creation & Token generation:
 - python manage.py createsuperuser
 - curl -X POST -d "username=your_superuser_username&           password=your_superuser_password" http://localhost:8000/api-token-auth/

## Run the server.
 - python manage.py runserver

## Access Django Admin.
 - Access the Django administration interface at http://127.0.0.1:8000/admin/ and authenticate with the superuser credentials to manage the database.

 ## Experimenting with or Interacting with the API endpoints.
  - we can test API endpoints using curl or http commands

## Create a Vendor User.

 - curl -H "Authorization: Token your_obtained_token" -X POST http://127.0.0.1:8000/api/vendors/ -d "vendor_code="5c6c24bb-78d6-4c0f-b379-de69e782a2f5"&name=Vendor+1&contact_details=Contact+1&address=Address+1"

## Using httpie:

 - http POST http://127.0.0.1:8000/api/vendors/ vendor_code=01 name="Vendor 1" contact_details="Contact 1" address="Address 1" "Authorization: Token your_obtained_token"

## About this API endpoint.

 - here this endpoint is used to create a vendor by providing the vendor details

## **List all vendors details.**

 ## Using this curl:
  - curl -H "Authorization: Token your_obtained_token" http://127.0.0.1:8000/api/vendors/

## using httpie:
 - http http://127.0.0.1:8000/api/vendors/ "Authorization: Token your_obtained_token"


## About this API endpoint.
 - here this endpoint is used to get the details of all vendors.

## Retrive a specific vendors details.
 ## using curl:
  - curl -H "Authorization: Token your_obtained_token" http://127.0.0.1:8000/api/vendors/{vendor_id}/

## using httpie:

 -  http http://127.0.0.1:8000/api/vendors/{vendor_id}/ "Authorization: Token your_obtained_token"


## About this API endpoint.
 - here this endpoint is used to get the details of vendor with vendor_id which was mentioned in the command.

## Update a vendors details.

## using curl.

## PUT method.

 - curl -H "Authorization: Token your_obtained_token" -X PUT http://127.0.0.1:8000/api/vendors/{vendor_id}/ -d "vendor_code=updated code&name=Updated Vendor Name&contact_details=Updated Contact Details&address=Updated Address"

## PATCH method.

 - curl -H "Authorization: Token your_obtained_token" -X PATCH http://127.0.0.1:8000/api/vendors/{vendor_id}/ -d "name=Updated Vendor Name"

## using httpie.

## PUT method.

 - http PUT http://127.0.0.1:8000/api/vendors/{vendor_id}/ vendor_code="updated vendor code" name="Updated Vendor Name" contact_details="Updated Contact Details" address="Updated Address" "Authorization: Token your_obtained_token"

## PATCH method.

 - http PATCH http://127.0.0.1:8000/api/vendors/{vendor_id}/ name="Updated Vendor Name" contact_details="Updated Contact Details" address="Updated Address" "Authorization: Token your_obtained_token"


## About this API endpoint:

 - here this endpoint we have two commands with different http methods (PUT,PATCH).As we have a primary key in the model the PUT method works as POST method (which means it creates a new vendor with given details). The PATCH method is used to update the vendor's details except vendor's id. here PUT handles updates by replacing the entire entity, so it creates a new entity. but where the PATCH handles by only updating the given fields.

## Delete a vendor.

## using curl.

 - curl -H "Authorization: Token your_obtained_token" -X DELETE http://127.0.0.1:8000/api/vendors/{vendor_id}/

## using httpie.

 - http DELETE http://127.0.0.1:8000/api/vendors/{vendor_id}/ "Authorization: Token your_obtained_token"

## About this API endpoint.

 - here this endpoint is used to delete the vendor with given {vendor_id}

## Create a purchase_order.

 ## using curl.

  - curl -H "Authorization: Token your_obtained_token" -X POST http://127.0.0.1:8000/api/purchase_orders/ -d "id": 1&po_number: 01&order_date: 2024-05-06T06:15:08.890422Z&delivery_date: 2024-05-06T11:37:00Z&"items":[ {"name": "Item 1","quantity": 10,"price": 25.5}]"quantity": 4&status: "completed"&quality_rating": 1.0&issue_date: 2024-05-06T06:15:08.890422Z&acknowledgment_date: 2024-05-06T11:40:00Z&vendor: 1"


## using httpie:

 - http POST http://127.0.0.1:8000/api/purchase_orders/ "id": 1&po_number: 01&order_date: 2024-05-06T06:15:08.890422Z&delivery_date: 2024-05-06T11:37:00Z&"items":[ {"name": "Item 1","quantity": 10,"price": 25.5}]"quantity": 4&status: "completed"&quality_rating": 1.0&issue_date: 2024-05-06T06:15:08.890422Z&acknowledgment_date: 2024-05-06T11:40:00Z&vendor: 1"
"Authorization: Token your_obtained_token"

## About this API endpoint .

 - here this endpoint is used to create a purchase_order with given details


## List all purchase_order details.

## using curl:

 - curl -H "Authorization: Token your_obtained_token" http://127.0.0.1:8000/api/purchase_orders/


## About this API endpoint:

 - here this endpoint is used to get the details of all purchase_orders

## Retrive a specific purchase_orders details:

## using curl:

 - curl -H "Authorization: Token your_obtained_token" http://127.0.0.1:8000/api/purchase_orders/{id}/

## using httpie:

 - http http://127.0.0.1:8000/api/purchase_orders/{id}/ "Authorization: Token your_obtained_token"

## About this API endpoint:

 - here this endpoint is used to get the details of purchase_order with given po_id.


## Update a purchase_order's details:

## using curl:

## PUT method:

 - curl -H "Authorization: Token your_obtained_token" -X PUT http://127.0.0.1:8000/api/purchase_orders/{id}/ -d "id": 1&po_number: 01&order_date: 2024-05-06T06:15:08.890422Z&delivery_date: 2024-05-06T11:37:00Z&"items":[ {"name": "Item 1","quantity": 10,"price": 25.5}]"quantity": 4&status: "completed"&quality_rating": 1.0&issue_date: 2024-05-06T06:15:08.890422Z&acknowledgment_date: 2024-05-06T11:40:00Z&vendor: 1"
"

## PATCH method:

 - curl -H "Authorization: Token your_obtained_token" -X PATCH http://127.0.0.1:8000/api/purchase_orders/{id}/ -d "vendor=updatedvno&quality_rating=1.0"

## using httpie: 

## PUT method.

 - http PUT http://127.0.0.1:8000/api/purchase_orders/{id}/ ""id": 1&po_number: 01&order_date: 2024-05-06T06:15:08.890422Z&delivery_date: 2024-05-06T11:37:00Z&"items":[ {"name": "Item 1","quantity": 10,"price": 25.5}]"quantity": 4&status: "completed"&quality_rating": 1.0&issue_date: 2024-05-06T06:15:08.890422Z&acknowledgment_date: 2024-05-06T11:40:00Z&vendor: 1"
"Authorization: Token your_obtained_token"

## PATCH method:

 - http PATCH http://127.0.0.1:8000/api/purchase_orders/{id}/""id": 1&po_number: 01&order_date: 2024-05-06T06:15:08.890422Z&delivery_date: 2024-05-06T11:37:00Z&"items":[ {"name": "Item 1","quantity": 10,"price": 25.5}]"quantity": 4&status: "completed"&quality_rating": 1.0&issue_date: 2024-05-06T06:15:08.890422Z&acknowledgment_date: 2024-05-06T11:40:00Z&vendor: 1"
"Authorization: Token your_obtained_token"

## About this API endpoint:

 - here this endpoint we have two commands with different http methods (PUT,PATCH).As we have a primary key in the model the PUT method works as POST method (which means it creates a new purchase_order with given details). The PATCH method is used to update the purchase_order's details except purchase_order's number. here PUT handles updates by replacing the entire entity, so it creates a new entity. but where the PATCH handles by only updating the given fields.(we can provide any no of fields in PATCH mathod.)

## Delete a purchase_order:

## using curl:

 - curl -H "Authorization: Token your_obtained_token" -X DELETE http://127.0.0.1:8000/api/purchase_orders/{id}/

## using httpie:

 - http DELETE http://127.0.0.1:8000/api/purchase_orders/{id}/ "Authorization: Token your_obtained_token"

## About this API endpoint:

 - here this endpoint is used to delete a purchase_order with given po_id

## Retrive a vendor's performance metrics:

## using curl:

 - curl -H "Authorization: Token your_obtained_token"http://127.0.0.1:8000/api/historical_performance/1/

## using httpie:

 - http://127.0.0.1:8000/api/historical_performance/1/ "Authorization: Token your_obtained_token"


## About this API endpoint:

## 1.Retrieving performance metrics:

 - Use this endpoint to fetch performance metrics for a vendor with the specified vendor_id.

 - These metrics include:

   - On-time Delivery Rate
   - Quality Rating Average
   - Average Response Time
   - Fulfillment Rate

## 2.On-time Delivery Rate Calculation:

 -  Calculated when a Purchase Order (PO) status changes to "completed".
 - Represents the percentage of POs delivered by or before the delivery_date.
 - It's determined by dividing the number of completed POs delivered on time by the total number of completed POs for that vendor.

## 3.Quality Rating Average Calculation:

   -  Calculated after every PO completion.
   -  Represents the average of all ratings given to the vendor for specific POs.
   -  Provides insight into the overall quality of the vendor's performance.

## 4.Average Response Time Calculation:

  - Calculated each time a PO is acknowledged by the vendor.
  - Represents the average time taken for the vendor to acknowledge or respond to POs.
  - Calculated by finding the time difference between issue_date and acknowledgment_date for each PO and then averaging these times across all POs for the vendor.

## 5.Fulfillment Rate Calculation:

 - Calculated when a PO status is set to "completed".
 - Represents the percentage of POs successfully fulfilled without issues.
 - Determined by dividing the number of successfully fulfilled POs (status = "completed" without issues) by the total number of POs issued to the vendor.



## License

[MIT](https://choosealicense.com/licenses/mit/)

