from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('accueil', views.home),
    path('article/<id_article>', views.view_article),
    path('articles/<str:tag>', views.list_articles_by_tag),
    path('articles/<int:year>/<int:month>', views.list_articles),
    path('redirection', views.view_redirection),
    path('date', views.date_actuelle),
    path('addition/<int:nb1>/<int:nb2>/', views.addition),
    path('', views.accueil, name='accueil'),
    path('art/<int:id>-<slug:slug>$', views.lire, name="lire"),
    path('image/', views.show_image),
    path('add-contact/', views.nouveau_contact),
    path('contacts/', views.contacts, name='contact'),
    #path('add-article/', views.add_article),
    path('voir-contacts/', views.voir_contacts),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion')
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)