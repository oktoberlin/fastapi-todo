from apps.users import views as users_views
from apps.todos import views as todos_views

router_configs = [
    (users_views.router, "/users", ["users"]),
    (todos_views.router, "/todo", ["todo"])
]