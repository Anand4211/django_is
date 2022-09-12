from django.shortcuts import render, get_object_or_404, redirect
from blogs.models import Poost
from blogs.forms import PoostForm

# Create your views here.
def post(request):
    post=Poost.objects.filter(status='published')
    return render(request,'blogs/post_list.html',{'post':post})



def post_detail(request,year,month,day,post):

    st=get_object_or_404(Poost,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
    po={'st':st}
    return render(request,'blogs/post_detail.html',context=po)

def form(request):
    form=PoostForm()
    if request.method=="POST":
        form=PoostForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/admin')
    return render(request,'blogs/form.html',{'form':form})

