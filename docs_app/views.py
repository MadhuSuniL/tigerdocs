from django.shortcuts import render,redirect
from .models import Document
from datetime import datetime,date


def indian_currency_format(ruppes):
    final_ruppes = ""
    count = 0
    if ruppes < 1000:
        return str(ruppes)
    elif ruppes > 999 and ruppes < 9999:
        for i in str(ruppes):
            if count == 1:
                final_ruppes+=","+i
            else:
                final_ruppes+=i
            count += 1
        return final_ruppes
    elif ruppes > 9999 and ruppes < 99999:
        for i in str(ruppes):
            if count == 2:
                final_ruppes+=","+i
            else:
                final_ruppes+=i
            count += 1
        return final_ruppes
    else:
        for i in str(ruppes):
            if count == 1 or count == 3:
                final_ruppes+=","+i
            else:
                final_ruppes+=i
            count += 1
        return final_ruppes    






def start(request):
    docs = Document.objects.all()
    data = []
    for doc in docs:
        # if doc.given_amt == 200000:
        #     doc.date = date(2022,12,17)
        #     doc.save()
        obj = {
            'id':doc.id,
            'name':doc.name,
            'date':doc.date.strftime('%d-%m-%Y'),
            'amt':indian_currency_format(doc.given_amt)
        }
        data.append(obj)
    return render(request, 'documents.html',context={'data':data})

def getfor_doc(request):
    docs = Document.objects.all()
    data = []
    for doc in docs:
        obj = {
            'name':doc.name,
            'date':doc.date,
            'amt':indian_currency_format(doc.given_amt)
        }
        data.append(obj)
    return render(request, 'documents.html',context={'data':data})    

def getfor_rec(request,pk=None):
    doc = Document.objects.get(pk=pk)
    data = doc.records['objects']
    
    days = datetime.now().date() - doc.date
    days = str(days).split(' ')[0]
    if days == '0:00:00':
        days = '0'
    sum = 0
    for i in data:
        try:
            sum += int(i['amt'])
        except:
            break
    r_days = sum
    for d in data:
        d['amt'] = indian_currency_format(int(d['amt']))
        
    return render(request, 'records.html',context={
        'data':data,
        'name':doc.name,
        'date':doc.date,
        'days': days,
        'amt':indian_currency_format(doc.given_amt),
        'r_days':indian_currency_format(r_days),
        'id':doc.id
        })
                    
                
def postfor_record(request,pk=None):
    amt = request.GET['amt']
    amt = int(str(amt).replace(',', ''))
    date = request.GET['date']
    date = str(date).split('-')
    date = date[-1] +'-'+ date[-2] +'-'+ date[-3]
    print(date)
    doc = Document.objects.get(pk=pk)
    data = {
        'date':date,
        'amt':amt
    }
    doc.records['objects'].append(data)
    doc.save()
    doc = Document.objects.get(pk=pk)
    data = doc.records['objects']
    days = datetime.now().date() - doc.date
    days = str(days).split(' ')[0]
    if days == '0:00:00':
        days = '0'
    sum = 0
    for i in data:
        try:
            sum += int(i['amt'])
        except:
            break
    r_days = sum//doc.daily_amt
    
    return render(request, 'records.html',context={'data':data,
        'name':doc.name,
        'date':doc.date,
        'days': days,
        'amt':indian_currency_format(doc.given_amt),
        'r_days':indian_currency_format(r_days),
        'id':doc.id
        })              
    
def postfor_doc(request):
    name = request.POST['name']
    date = request.POST['date']
    amt = int(str(request.POST['amt']).replace(',', ''))
    daily_amt = amt//100
    record = {
        'objects':[]
    }    
    Document.objects.create(name=name,given_amt=amt,date=date,daily_amt=daily_amt,records=record)
    return redirect('/')        

from django.http import JsonResponse

def delfor_rec(request,pk=None):
    doc = Document.objects.get(pk=pk)
    doc.records['objects'].pop(-1)
    doc.save()
    return JsonResponse({'msg':'Done'})

def delfor_doc(request,pk=None):
    doc = Document.objects.last()
    doc.delete()
    return JsonResponse({'msg':'Done'})


