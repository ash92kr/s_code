from django.shortcuts import render

# Create your views here.
def team(request):
    return render(request, 'about/team.html')
    

def members(request):
    starting_members = ['이상해씨', '파이리', '꼬부기']
    return render(request, 'about/members.html', {'startings': startings})