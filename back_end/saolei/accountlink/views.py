from .models import AccountLinkQueue
from userprofile.models import UserProfile
from django.http import HttpResponseForbidden, HttpResponseBadRequest, JsonResponse, HttpResponse, HttpResponseNotFound
from utils.response import HttpResponseConflict
from django.views.decorators.http import require_GET, require_POST

private_platforms = [""] # 私人账号平台

# 为自己绑定账号，需要指定平台和ID
@require_POST
def add_link(request):
    user = UserProfile.objects.filter(id=request.user.id).first()
    if user == None:
        return HttpResponseForbidden()
    platform = request.POST.get('platform')
    if platform == None:
        return HttpResponseBadRequest()
    accountlink = AccountLinkQueue.objects.filter(platform=platform, userprofile=user).first()
    if accountlink:
        return HttpResponseConflict() # 每个平台只能绑一个账号
    accountlink = AccountLinkQueue.objects.create(platform=platform, identifier=request.POST.get('identifier'), userprofile=user)
    return HttpResponse()

# 解绑自己的账号，只需要指定平台
@require_POST
def delete_link(request):
    user = UserProfile.objects.filter(id=request.user.id).first()
    if user == None:
        return HttpResponseForbidden()
    platform = request.POST.get('platform')
    if platform == None:
        return HttpResponseBadRequest()
    accountlink = AccountLinkQueue.objects.filter(platform=platform, userprofile=user).first()
    if accountlink:
        accountlink.delete()
        return HttpResponse()
    return HttpResponseNotFound()

@require_GET
def get_link(request):
    userid = request.GET.get("id")
    user = UserProfile.objects.filter(id=userid).first()
    accountlink = AccountLinkQueue.objects.filter(userprofile=user).values("platform","identifier","verified")
    if not request.user.is_staff and request.user != user:
        accountlink = accountlink.exclude(platform__in=private_platforms) # 非管理员不能查其他人的私人账号
    return JsonResponse(list(accountlink), safe=False)

