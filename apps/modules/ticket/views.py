from django.shortcuts import render


def tickets(request):
    return render(request, 'pages/tickets.html', {})


def ticket(request, ticket_id):
    return render(request, 'pages/ticket.html', {})


def ticket_new(request):
    return render(request, 'pages/ticket_new.html', {})


def ticket_edit(request, ticket_id):
    return render(request, 'pages/ticket_edit.html', {})


def ticket_delete(request, ticket_id):
    pass


def ticket_comment(request, ticket_id):
    pass


def ticket_comment_edit(request, ticket_id, comment_id):
    pass


def ticket_comment_delete(request, ticket_id, comment_id):
    pass
