from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
                       url(r'^$', 'biblioteca.views.inicio', name='inicio'),
                       url(r'^biblioteca$', 'biblioteca.views.biblioteca', name='biblioteca'),
                       url(r'^ajustes$', 'biblioteca.views.ajustes', name='ajustes'),
                       url(r'^libro/(?P<libId>[0-9]+)/$', 'biblioteca.views.libroT', name='librete'),
                       url(r'^valorar/$', 'biblioteca.views.valorar', name='valorar'),
                       url(r'^usuario/nuevo$','biblioteca.views.nuevo_usuario', name='nuevo_usuario'),
                       url(r'^libro/nuevo$','biblioteca.views.nuevolibro', name='nuevolibro'),
                       url(r'^crear_libro/$','biblioteca.views.crear_libro', name='crear_libro'),
                       url(r'^enviar_mail/$','biblioteca.views.enviar_mail', name='enviar_mail'),
                      )