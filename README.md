# category_server
This is a simple server which performs CRUD for Category

# Installation Instruction

Clone this project. <br>
Create a virtual environment. <br>
Change to project root directory. <br>
Install all the dependencies using pip install -r requirements.txt. <br>
Run db migrations for storig data as python manage.py migrate. <br>
Run server as python manage.py runserver. <br>

At this point our server is able to handle CRUD for Category.

Endpoints: <br>

1. Get all Categories <br>
Url: http://localhost:8000/api/product/categories/ <br> 
Method: GET <br> 
Response: <br>
[
  {
        "id": 1,
        "created": "2018-08-28T18:58:50.120991Z",
        "modified": "2018-08-28T18:58:50.126300Z",
        "name": "Category1",
        "is_featured": false,
        "image": null,
        "is_active": true,
        "description": null,
        "parent": null
    }
]


2. Create a Category <br>
Url: http://localhost:8000/api/product/categories/ <br> 
Method: POST <br> 
Payload: {
  "name": "Category_Name" --all other fields are optional
} <br>
Response: <br>
{
        "id": 2,
        "created": "2018-08-28T18:58:50.120991Z",
        "modified": "2018-08-28T18:58:50.126300Z",
        "name": "Category2",
        "is_featured": false,
        "image": null,
        "is_active": true,
        "description": null,
        "parent": null
}

3. Get a Category <br>
Url: http://localhost:8000/api/product/categories/1 <br> 
Method: GET <br> 
Response: <br>
{
        "id": 1,
        "created": "2018-08-28T18:58:50.120991Z",
        "modified": "2018-08-28T18:58:50.126300Z",
        "name": "Category1",
        "is_featured": false,
        "image": null,
        "is_active": true,
        "description": null,
        "parent": null
}


4. Update a Category <br>
Url: http://localhost:8000/api/product/categories/1 <br> 
Method: PUT <br> 
Payload: {
  "name": "Category1 New",
  "description": "description"
} <br>
Response: <br>
{
    "id": 1,
    "created": "2018-08-28T12:39:28.782642Z",
    "modified": "2018-08-28T13:35:12.706647Z",
    "name": "Category1 New",
    "is_featured": false,
    "image": null,
    "is_active": true,
    "description": null,
    "parent": null
}

5. Delete a Category <br>
Url: http://localhost:8000/api/product/categories/1 <br> 
Method: DELETE <br> 
Response: 404 No Content

<h4>Filtering and Ordering</h4>

Ordering is done in models meta class.<br>
For filtering, dynamic filtering has been implemented using django-filter package. <br>
Endpoint looks something like <br>
http://localhost:8000/api/product/categories/?is_featured=False <br>

Dynamic filtering of fields can also be done.<br>
For that just separate the desired fields names with pipes as
http://localhost:8000/api/product/categories/?params=name|is_featured <br>

<hr>

<h3> For Email Notification </h3>
A message broker is needed for this module to run. <br>
<i>Note:</i> Here celery is configured to use rabbitmq.
After installing RabbitMQ, run it and then to run the worker as daemon use python manage.py celeryd -l info <br>
At this point worker process are running and are ready to take up any task from the queue. <br>
For email config set email id and password of gmail in environment. <br>
Uncomment the line trigger_email.delay(email_sub, email_msg) in project-root/product/views.py line 31 <br>

Now we should be receiving emails after 15 mins of Category created.



