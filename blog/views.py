from django.shortcuts import render
from blog import models
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseServerError, HttpResponseForbidden, JsonResponse
import requests,datetime,json
# Create your views here.
def index(request):
    word = get_today_word()
    feeling = models.Feelings.objects.filter(feelings_id=int(len(models.Feelings.objects.all())))
    posts = models.Post.objects.all()
    categories = models.Category.objects.all()
    return render(request,'index.html',{"posts":posts,"categories":categories,'word':word,'feeling':feeling})

def detail(request,blog_id):
    post = models.Post.objects.get(blog_id=blog_id)
    word = get_today_word()
    return render(request,'detail.html',{'post':post,'word':word})

def feelings(request):
    feelings = models.Feelings.objects.all()
    return render(request,'feelings.html',{'feelings':feelings})

@csrf_exempt
def api_save(request):
    if request.is_ajax():
        if request.method == 'POST':
            title = request.POST['title']
            textarea = request.POST['textarea']

            models.Feelings.objects.create(title=title,textarea=textarea)
            return JsonResponse({'status': 'Record mood success!'})
        else:
            return HttpResponseForbidden()
    else:
        return HttpResponseServerError()

def get_today_word():
    today = datetime.date.today()
    word=models.Word.objects.filter(add_time__year=today.year,
                             add_time__month=today.month,
                             add_time__day=today.day).first()
    if word:
        return (json.loads(word.content),today.weekday()+1)
    else:
        s = requests.Session()
        url = "https://api.hibai.cn/api/index/index"
        data = {
            "TransCode": "030111", "OpenId": "123456789", "Body": ""
        }
        ret = s.post(url=url, data=data).content.decode('utf-8')
        models.Word.objects.create(content=ret)
        return (json.loads(ret),today.weekday()+1)