from django.shortcuts import render, redirect

MY_NAME = "isaac"  # your name for boyfriend check

# Page 1: Greeting pages
def page1(request):
    if request.method == "POST":
        request.session['her_name'] = request.POST.get('name')
        return redirect('page2')  # redirects to Page 2 after submitting name
    return render(request, 'love/page1.html')

# Page 2: Ask for boyfriend name
def page2(request):
    her_name = request.session.get('her_name', '')
    return render(request, 'love/page2.html', {'name': her_name})

# Check boyfriend name
def check_boyfriend(request):
    if request.method == "POST":
        bf_name = request.POST.get('bf_name', '').lower()
        if bf_name == MY_NAME:
            return redirect('story')
        else:
            return redirect('wrong')

# Wrong name page
def wrong_name(request):
    return render(request, 'love/wrong_name.html')

# Story page
def story(request):
    return render(request, 'love/story1.html')

def story2(request):
    return render(request, "love/story2.html")

def story3(request):
    return render(request, "love/story3.html")

def story4(request):
    return render(request, "love/story4.html")

def story5(request):
    return render(request, "love/story5.html")

def story6(request):
    return render(request, "love/story6.html")

def story7(request):
    return render(request, "love/story7.html")

def story8(request):
    return render(request, "love/story8.html")

def end_story(request):
    return render(request, "love/end_story.html")

def story9(request):
    return render(request, "love/story9.html")

def story9_last(request):
    return render(request, "love/story9_last.html")

def story10(request):
    return render(request, "love/story10.html")