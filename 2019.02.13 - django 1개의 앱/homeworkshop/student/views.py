from django.shortcuts import render

# Create your views here.
def info(request):
    # teacher = '주노'
    # students = {
    #   '학생이름': 나이, 
    # }
    return render(request, 'info.html')
    # return render(request, 'info.html', {'teacher':teacher, 'students': students})
    
def student(request, name):

    work = {
        '성연혁': 20,
        '최운우': 25,
        '김윤중': 23,
        '최비선': 22,
        '진순옥': 24,
        '천정은': 21
    }
    # age = students.get(name, 'unknown')   # 에러가 나도 None값을 반환한다
    # teacher = {'address': '대전', 'name': '준호', 'age': 40}
    return render(request, 'student.html', {'name': name, 'age': work[name]})
    