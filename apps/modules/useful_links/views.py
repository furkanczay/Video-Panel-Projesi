from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import UsefulLinks
from .forms import UsefulLinksForm
from django.contrib.auth.decorators import permission_required

def useful_links(request):
    links = UsefulLinks.objects.all()
    return render(request, 'modules/useful_links/list.html', {
        'links': links
    })

@permission_required('useful_links.useful_links_add')
def useful_links_add(request):
    if request.method == 'POST':
        form = UsefulLinksForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.instructor = request.user
            link.save()
            messages.success(request, 'Link başarıyla eklendi')
            return redirect('useful_links')
        else:
            messages.error(request, 'Link eklenirken bir hata oluştu')
            return redirect('useful_links')
    else:
        form = UsefulLinksForm()
    return render(request, 'modules/useful_links/add.html', {
        'form': form
    })

def useful_links_edit(request, pk):
    link = UsefulLinks.objects.get(pk=pk)
    return render(request, 'modules/useful_links/edit.html', {
        'link': link
    })

def useful_links_delete(request, pk):
    link = get_object_or_404(UsefulLinks, pk=pk)
    if link:
        link.delete()
        messages.success(request, 'Link başarıyla silindi')
        return redirect('useful_links')
    else:
        messages.error(request, 'Link silinirken bir hata oluştu')
        return redirect('useful_links')
