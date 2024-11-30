from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path('', include('session_cookies.urls')),
    path('', include('orm_query.urls')),
    path('', include('deep_learning_sql.urls')),

]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
