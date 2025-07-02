# README.md

# Press Media Project

## Overview
This project is a Django application for managing articles. It provides a RESTful API for creating, reading, updating, and deleting articles.

## Setup Instructions

### Prerequisites
- Python 3.x
- Django
- Django REST Framework

### Steps to Integrate Swagger into Your Django Project

1. **Install Django REST Framework and drf-yasg**:
   Run the following command to install the necessary packages:
   ```
   pip install djangorestframework drf-yasg
   ```

2. **Update Installed Apps**:
   Open `press_media/settings.py` and add `rest_framework` and `drf_yasg` to the `INSTALLED_APPS` list:
   ```python
   INSTALLED_APPS = [
       ...
       'rest_framework',
       'drf_yasg',
   ]
   ```

3. **Create Swagger Configuration**:
   In your `press_media/urls.py`, add the following code to configure Swagger:
   ```python
   from rest_framework import permissions
   from drf_yasg.views import get_schema_view
   from drf_yasg import openapi

   schema_view = get_schema_view(
       openapi.Info(
           title="Your API Title",
           default_version='v1',
           description="API documentation",
           terms_of_service="https://www.google.com/policies/terms/",
           contact=openapi.Contact(email="contact@yourapi.local"),
           license=openapi.License(name="BSD License"),
       ),
       public=True,
       permission_classes=(permissions.AllowAny,),
   )

   urlpatterns = [
       ...
       path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
       path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   ]
   ```

4. **Run the Server**:
   Start your Django development server:
   ```
   python manage.py runserver
   ```

5. **Access Swagger UI**:
   Open your web browser and navigate to `http://127.0.0.1:8000/swagger/` to view the Swagger UI.

6. **Access ReDoc**:
   You can also access the ReDoc documentation at `http://127.0.0.1:8000/redoc/`.

By following these steps, you will successfully integrate Swagger into your Django project for API documentation.