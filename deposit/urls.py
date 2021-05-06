"""deposit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import deposit1.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', deposit1.views.Deposit1ListView.as_view(), name='depo-list'),
    path('deposit1/<int:pk>', deposit1.views.Deposit1DetailView.as_view(), name='depo-detail'),
    path('add_deposit', deposit1.views.AddDeposit1View.as_view()),
]
