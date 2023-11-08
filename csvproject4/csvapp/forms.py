from django import forms
from csvapp.models import Bank
class BankForm(forms.ModelForm):
	class Meta:
		model=Bank
		fields='__all__'