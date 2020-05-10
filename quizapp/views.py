from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from quizapp.models import Questions
from quizapp.forms import QuestionForm
# Create your views here.

def index(request):
    return render(request,'quizapp/index.html')
def show(request):
    questionData = Questions.objects.all
    params = {'questionData' : questionData}
    return render(request, 'quizapp/show.html', params)
def create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass
    else:  
        form = QuestionForm()  
    
    return render(request, 'quizapp/create.html',{'form':form})

def quiz(request):
    ques = Questions.objects.all
    return render(request,
        'quizapp/quiz.html',
        {'ques':ques})
def result(request):
    print("result page")
    if request.method == 'POST':
        data = request.POST
        datas = dict(data)
        qid = []
        qans = []
        ans = []
        score = 0
        for key in datas:
            try:
                qid.append(int(key))
                qans.append(datas[key][0])
            except:
                print("Csrf")
        for q in qid:
            ans.append((Questions.objects.get(id = q)).answer)
        total = len(ans)
        for i in range(total):
            if ans[i] == qans[i]:
                score += 1
        # print(qid)
        # print(qans)
        # print(ans)
        print(score)
    return render(request,
        'quizapp/result.html',
        {'score':score,
        'total':total})
