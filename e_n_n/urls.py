from django.urls import path

from e_n_n.views import ENNCreateAPIView, ENNListAPIView, ENNAPIView


urlpatterns = [
    path('enn/', ENNCreateAPIView.as_view(), name='enn'),
    path('enn/list/', ENNListAPIView.as_view(), name='enn_list'),
    path('enn/<pk>/', ENNAPIView.as_view(), name='enn_pk'),
    ]
