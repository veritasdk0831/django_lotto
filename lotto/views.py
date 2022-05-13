from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm

def index(request):

    lottos = GuessNumbers.objects.all()
    # {'lottos':lottos} <- context라고 부름.
    return render(request, 'lotto/default.html', {'lottos':lottos})

def hello(request):
    return HttpResponse("<h1 style='color:red;'>Hello, world!</h1>")


def post(request):

    if request.method == 'POST':

        form = PostForm(request.POST)

        if form.is_valid():
            lotto = form.save(commit=False)
            lotto.generate() # <- self_save

            return redirect('index')


        # 방법 1!!!
        # user_name = request.POST['name']
        # user_text = request.POST['text']
        # row = GuessNumbers(name=user_name, text=user_text)
        # row.generate()
        # -> 이 방법은 form tag를 안쓰고 순수 저장할 때 이렇게 쓴다고 함.



        # 방법 2!!!
        # PostForm(request, POST) # 채워진 양식
        #
        # if form.is_valid(): #is_valid [타당한가, 그렇지 않은가]에 대한 함수.
        #     lotto = form.save(commit = False)
        #     print(type(lotto))
        #     print(lotto)
        #     lotto.generate()
        #     return redirect('index')
        #
        # print('\n\n\n===========================\n\n\n')
        # print(request.POST['csrfmiddlewaretoken'])
        # print(request.POST['name'])
        # print(request.POST['text'])
        # print('\n\n\n===========================\n\n\n')
        #
        # form = PostForm()
        # return render(request, 'lotto/form.html', {'form':form})

    else:
        form = PostForm() #empty form 형성
        return render(request, 'lotto/form.html', {'form':form})

def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk=lottokey)
    return render(request, "lotto/detail.html", {"lotto":lotto})
