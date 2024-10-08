from django.urls import path
from .views import TaskList, TaskDetail,TaskCreate, TaskUpdate,TaskDelete,CustomLoginView,RegisterPage,GuestPage
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='guest-page'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('guest-page/', GuestPage.as_view(), name='guest-page'),

    path('', TaskList.as_view(), name='tasks'),
    path('task/<uuid:pk>/', TaskDetail.as_view(), name="task"),
    path('task-create/', TaskCreate.as_view(), name="task-create"),
    path('task-update/<uuid:pk>/', TaskUpdate.as_view(), name="task-update"),
    path('task-delete/<uuid:pk>/', TaskDelete.as_view(), name="task-delete"),

]