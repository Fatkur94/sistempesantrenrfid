from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from santri import views as santri_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_views.MyLoginView.as_view(template_name= 'users/login2.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name= 'users/login2.html'), name='logout'),
    path('register/', user_views.register, name='register'),
    path('liststaff/', user_views.list_staff, name='list_staff'),
    path('staff/<int:pk>/delete', user_views.delete_staff, name='staff-delete'),
    path('createstaff/', user_views.create_staff, name='create_staff'),
    path('createsuperuser/', user_views.create_superuser, name='create_superuser'),
    path('profile/', user_views.profile, name='profile'),

    # santri
    path('', user_views.index, name='home'),
    path('search/', user_views.search, name='search'),
    path('santrilist/', santri_views.SantriListView.as_view(), name='santri-list'),
    path('santricreate/', santri_views.SantriCreateView.as_view(), name='santri-create'),
    path('santri/<int:pk>/update/', santri_views.SantriUpdateView.as_view(), name='santri-update'),
    path('santri/<int:pk>/', santri_views.SantriDetailView.as_view(), name='santri-detail'),
    path('santri/<int:pk>/delete/', santri_views.SantriDeleteView.as_view(), name='santri-delete'),
    
    # anggota santri
    path('santri/<int:santri>/anggotakeluargacreate/', santri_views.AnggotaKeluargaCreateView.as_view(), name='anggotakeluarga-create'),
    path('santri/<int:santri>/anggotakeluarga/<int:anggotakeluarga>/update/', santri_views.update_anggotakeluarga, name='anggotakeluarga-update'),
    path('santri/<int:santri>/anggotakeluarga/<int:anggotakeluarga>/delete/', santri_views.delete_anggotakeluarga, name='anggotakeluarga-delete'),

    # santri keluar
    path('keluarlist/', santri_views.KeluarListView.as_view(), name='keluar-list'),
    path('santri/<int:pk>/keluarcreate/', santri_views.KeluarCreateView.as_view(), name='keluar-create'),
    path('santri/<int:santri>/keluar/<int:keluar>/update/', santri_views.update_keluar, name='keluar-update'),
    path('santri/<int:santri>/keluar/<int:keluar>/invoice/', santri_views.keluar_invoice, name='keluar-invoice'),

    #santri pulang
    path('pulanglist/', santri_views.PulangListView.as_view(), name='pulang-list'),
    path('santri/<int:pk>/pulangcreate/', santri_views.PulangCreateView.as_view(), name='pulang-create'),
    path('santri/<int:santri>/pulang/<int:pulang>/update/', santri_views.update_pulang, name='pulang-update'),
    path('santri/<int:santri>/pulang/<int:pulang>/invoice/', santri_views.pulang_invoice, name='pulang-invoice'),

    # santri sambang
    path('sambanglist/', santri_views.SambangListView.as_view(), name='sambang-list'),
    path('santri/<int:pk>/sambangcreate/', santri_views.SambangCreateView.as_view(), name='sambang-create'),
    path('santri/<int:santri>/sambang/<int:sambang>/update/', santri_views.update_sambang, name='sambang-update'),
    path('santri/<int:santri>/sambang/<int:sambang>/invoice/', santri_views.sambang_invoice, name='sambang-invoice'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)