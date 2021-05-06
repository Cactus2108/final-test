from django.shortcuts import render
from django.views.generic import View, ListView, FormView, DetailView
from django.urls import reverse_lazy
from deposit1.models import Deposit
from deposit1.forms import Deposit1Form

class Deposit1ListView(ListView):

    model = Deposit
    template_name = 'depo_list.html'


class Deposit1DetailView(DetailView):

    model = Deposit
    template_name = 'depo_details.html'


class AddDeposit1View(FormView):

    form_class = Deposit1Form
    template_name = 'add_deposit.html'
    success_url = reverse_lazy('depo-list')

    def form_valid(self, form):
        form.save()

        response = super().form_valid(form)
        return response



        return render(
            template_name='depo_list.html',
            request=request,
            context=context,
        )

