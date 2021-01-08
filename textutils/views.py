from django.http import HttpResponse
from  django.shortcuts import render

def index(request):
     return render(request,'index.html')
def analyze(request):
    # geting the text and analyze
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    cfirst=request.POST.get('cfirst','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')



    if removepunc=="on":
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_'''
        analyzed=""
        for i in djtext:
            if i not in punctuations:
                analyzed=analyzed+i

        params ={'purpose':'removed punctuations','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif(cfirst=="on"):
        analyzed=""
        for char in djtext:
            analyzed= analyzed + char.upper()
            params = {'purpose': 'Changed to uppercase', 'analyzed_text': analyzed}
            return render(request, 'analyze.html', params)
    elif(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char!="\n":
                analyzed=analyzed + char

        params = {'purpose': 'removed new line', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif(extraspaceremover=="on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if djtext[index]=="" and djtext[index+1]=="":
                pass
            else:
                analyzed=analyzed+char

    params = {'purpose': 'removed new line', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)






#def removepunc(request):
    #geting the text and analyze
 #   djtext=request.GET.get('text','default')
  #  print(djtext)
   # return HttpResponse('Remove punc')

def capfirst(request):
    return HttpResponse('cap first')

def newlineremove(request):
    return HttpResponse('New line remover')


def charcount(request):
    return HttpResponse('char counted')

