from django.shortcuts import render
from django.views.generic import ListView
from boynextdoor.models import Character

# Create your views here.

class CharacterListView(ListView):
    model = Character  # 여기서 'modle'을 'model'로 수정
    # character_list = Character.objects.all() #DB에 Character 데이터 다 가져오자
    # return render(request, 'boynextdoor.list.html', context = {'character_list : character_list})
    # 모델_list.html에 모델_list라는 키로 DB에서 가져온 데이터 넣어서 render 하자
