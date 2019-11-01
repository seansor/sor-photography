from django import forms
from .models import CommissionOrder, Quote


class OrderForm(forms.ModelForm):
    """Order form to request commissions"""

    class Meta:
        model = CommissionOrder
        exclude = ['customer', 'date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update(
            {'placeholder': 'Please provide as much detail as possible.'})
        self.fields['size'].widget.attrs.update(
            {'placeholder': 'Enter desired size, e.g. 297mm x 210mm.'})

class QuoteForm(forms.ModelForm):
    """Quote form to for requested commissions"""

    class Meta:
        model = Quote
        exclude = ['price_total', 'date', 'accepted', 'rejected']
