from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from .forms import UserModelForm
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib import messages


# Create your views here.
class RegisterView(View):

    def get(self, request):
        form = UserModelForm()
        context = {'form': form}
        return render(request, 'signup.html', context)

    def post(self, request):
        # import ipdb; ipdb.set_trace()
        form = UserModelForm(request.POST)
        if form.is_valid():
            # import ipdb; ipdb.set_trace()
            form.save()
            user = authenticate(
                username=request.POST['username'],
                password=request.POST['password'])
            login(request, user)
            # return redirect('/')
            messages.success(request, 'Sucessfully posted')
            # return redirect(request, 'signup.html', context)

        context = {'form': form}
        return render(request, 'signup.html', context)

