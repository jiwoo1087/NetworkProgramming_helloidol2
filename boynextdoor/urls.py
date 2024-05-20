from django.urls import path

from boynextdoor import views

app_name = 'boynextdoor'

urlpatterns = [
    path('', views.CharacterListView.as_view(), name='character-list'),

]