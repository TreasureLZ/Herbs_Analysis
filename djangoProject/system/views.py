import itertools
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Prescript,OriginPrice,HistoryPrice,OriginStatistics,Info
from collections import Counter
import re
import jieba

@login_required(login_url='/login/')
def index(request):
    return render(request,'system/index.html')

@login_required(login_url='/login/')
def chart1(request):
    info = {}
    keyword = request.POST.get("keyword")
    results = Prescript.objects.all().filter(tcmName=keyword).values('recipe_pz')
    recipe_pz_list = []
    for result in results:
        recipe_pz = eval(result['recipe_pz'])
        recipe_pz_list.append(recipe_pz)
    totals = Counter(i for i in list(itertools.chain.from_iterable(recipe_pz_list)))
    totals = sorted(totals.items(), key=lambda x: x[1], reverse=True)
    if len(totals):
        info['data'] = []
        for i in range(20):
            name = totals[i][0]
            value = totals[i][1]
            info['data'].append({'name':name,'value':value})
    elif keyword:
        info['error'] = True
    return render(request,'system/chart1.html',context={'info':info})

@login_required(login_url='/login/')
def chart2(request):
    info = {}
    keyword = request.POST.get("keyword")
    results = OriginPrice.objects.all().filter(keyword=keyword)
    if len(results):
        info['data'] = {'x_data':[],'y_data':[]}
        for result in results:
            origin = result.origin
            price = result.price
            info['data']['x_data'].append(origin)
            info['data']['y_data'].append(price)
    elif keyword:
        info['error'] = True
    return render(request, 'system/chart2.html', context={'info': info})

@login_required(login_url='/login/')
def chart3(request):
    info = {}
    keyword = request.POST.get("keyword")
    results = OriginStatistics.objects.all().filter(keyword=keyword)
    if len(results):
        info['data'] = []
        for result in results:
            origin = result.origin
            statistics = result.count
            info['data'].append({'name':origin,'value':statistics})
    elif keyword:
        info['error'] = True
    return render(request, 'system/chart3.html', context={'info': info})

@login_required(login_url='/login/')
def chart4(request):
    info = {}
    keyword = request.POST.get("keyword")
    results = HistoryPrice.objects.all().filter(keyword=keyword)
    if len(results):
        info['data'] = {'x_data':[],'y_data':[]}
        for result in results:
            updateTime = result.updateTime
            price = result.price
            info['data']['x_data'].append(updateTime)
            info['data']['y_data'].append(price)
    elif keyword:
        info['error'] = True
    return render(request, 'system/chart4.html', context={'info': info})

@login_required(login_url='/login/')
def chart5(request):
    info = {}
    keyword = request.POST.get("keyword")
    results = Info.objects.all().filter(keyword=keyword).values('title','content')
    if len(results):
        re_obj = re.compile(r"[!\"#$%&'()*+,-./:;<=>?@[\\\]`_{|}~·——！，。？、￥‘’“”（）【】《》\s：；·]+VR")
        content = ""
        for result in results:
            content += re_obj.sub('', result['title']+result['content'])
        content = jieba.cut(content)
        s = set()
        with open('./system/cn_stopword.txt', 'r', encoding='utf-8') as fp:
            for line in fp:
                s.add(line.strip())
        def removeStopWord(words):
            return [word for word in words if word not in StopWord]
        StopWord = s
        content = removeStopWord(content)
        word_counts = Counter(content)  # 对分词做词频统计
        word_counts_top = word_counts.most_common(200)
        info['data'] = []
        for key,value in word_counts_top:
            info['data'].append({'name':key,'value':value})
    elif keyword:
        info['error'] = True
    return render(request, 'system/chart5.html', context={'info': info})