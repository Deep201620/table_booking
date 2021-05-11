import json
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import F
from .models import Table


# Create your views here.

def book_table(request):
    return render(request, "tbs/book_table.html")


def insert(request):
    person_name = request.POST.get('person_name', '')
    mob_number = request.POST.get('mob_number', '')
    members = request.POST.get('members', '')
    obj = Table.objects.last()
    remain_tables = getattr(obj, 'remain_tables')
    if members == 'How many Members?':
        return render(request, "tbs/booked.html")
    else:
        s1 = slice(2)
        members = members[s1]
        if remain_tables == 0:
            return HttpResponse("<h1><strong>No table Left! Sorry you have to wait....</h1></strong>")
        if int(members) <= 5:
            remain_tables2 = remain_tables - 1
            table = Table(person_name=person_name, mob_number=mob_number, members=members, remain_tables=remain_tables2)
        else:
            remain_tables2 = remain_tables-2
            table = Table(person_name=person_name, mob_number=mob_number, members=members,
                          remain_tables=remain_tables2)
        table.save()
        response = book_table(request)  #Calling this first view again
        return HttpResponse(response)
