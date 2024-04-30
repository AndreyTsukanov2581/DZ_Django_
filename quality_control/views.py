from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import BugReport, FeatureRequest

def index(request):
    bug_list_url = reverse('quality_control:bug_list')
    improvements_req_url = reverse('quality_control:feature_list')
    html = f"<h1>Система контроля качества</h1><a href='{bug_list_url}'>Список всех багов</a><br /><a href='{improvements_req_url}'>Запросы на улучшение</a>"
    return HttpResponse(html)
    
def bug_list_url(request):
    return HttpResponse("Cписок отчетов об ошибках")

def improvements_req_url(request):
    return HttpResponse("Список запросов на улучшение")

def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    response_html = f'<h1>Детали бага {bug.name}</h1>'
    return HttpResponse(response_html)

def feature_id_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    response_html = f'<h1>Детали улучшения {feature.name}</h1>'
    return HttpResponse(response_html)
