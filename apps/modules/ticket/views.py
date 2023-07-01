from django.shortcuts import render
from apps.modules.ticket.models import Ticket
from django.contrib.auth.decorators import login_required


@login_required()
def tickets(request):
    user_tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'pages/tickets.html', {
        'tickets': user_tickets,
    })


@login_required()
def ticket_detail(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, 'pages/ticket_detail.html', {
        'ticket': ticket,
    })


@login_required()
def ticket_new(request):
    return render(request, 'pages/ticket_new.html', {})


@login_required()
def ticket_edit(request, ticket_id):
    return render(request, 'pages/ticket_edit.html', {})


@login_required()
def ticket_delete(request, ticket_id):
    pass


@login_required()
def ticket_comment(request, ticket_id):
    pass


@login_required()
def ticket_comment_edit(request, ticket_id, comment_id):
    pass


@login_required()
def ticket_comment_delete(request, ticket_id, comment_id):
    pass
