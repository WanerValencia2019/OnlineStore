from apps.users.api.routes import urls as user_routes
from apps.products.api.routes import urls as product_routes

app_name = "api"
urlpatterns = []
urlpatterns += user_routes
urlpatterns += product_routes
