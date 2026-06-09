from django.shortcuts import render
from .models import CooperativeInfo, ImportantInfo, Contact, Document, News, WorkReport, FinancialReport


def home(request):
    news = News.objects.filter(is_published=True)[:5]
    info = CooperativeInfo.objects.first()
    return render(request, 'home.html', {'news': news, 'info': info})


def about(request):
    info = CooperativeInfo.objects.first()
    return render(request, 'about.html', {'info': info})


def important_info(request):
    info = ImportantInfo.objects.first()
    contacts = Contact.objects.all()
    return render(request, 'info.html', {'info': info, 'contacts': contacts})


def documents(request):
    docs = Document.objects.filter(is_published=True)
    categories = {}
    category_order = ['charter', 'protocol', 'regulation', 'other']
    category_labels = {
        'charter': 'Устав и учредительные документы',
        'protocol': 'Протоколы собраний',
        'regulation': 'Положения и правила',
        'other': 'Прочие документы',
    }
    for key in category_order:
        cat_docs = [d for d in docs if d.category == key]
        if cat_docs:
            categories[category_labels[key]] = cat_docs
    return render(request, 'documents.html', {'categories': categories})


def reports(request):
    work_reports = WorkReport.objects.all()
    financial_reports = FinancialReport.objects.all()
    return render(request, 'reports.html', {
        'work_reports': work_reports,
        'financial_reports': financial_reports,
    })
