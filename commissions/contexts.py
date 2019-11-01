""" Store commission relevant info that should be persistent on each page """

from .models import Quote

def user_quotes(request):
    """ Count number of quotes user has to respond to. """

    quotes = Quote.objects.filter(order__customer=request.user.id)

    count = 0
    for quote in quotes:
        if not quote.rejected and not quote.accepted:
            count += 1

    return {'count': count}
