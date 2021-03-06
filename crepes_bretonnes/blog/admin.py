from django.contrib import admin
from .models import Categorie, Article
from django.utils.text import Truncator


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date', 'apercu_contenu')
    list_filter = ('auteur', 'categorie', )
    date_hierarchy = 'date'
    ordering = ('date', )
    search_fields = ('titre', 'contenu')
    fieldsets = (
        ('Général', {
            'classes': ['collapse',],
            'fields': ('titre', 'auteur', 'categorie')
        }),
        ('Contenu de l\'article', {
            'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
            'fields': ('contenu', )
        })
    )
    prepopulated_fields = {'slug': ('titre', ), }

    def apercu_contenu(self, article):
        return Truncator(article.contenu).chars(40, truncate='...')

    apercu_contenu.short_description = 'Aperçu du contenu'


admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)


