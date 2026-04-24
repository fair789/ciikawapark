# 場所: ciikawapark/config/urls.py

from django.contrib import admin
from django.urls import path
from sticker.views import dashboard  # ← stickerアプリのviewsからdashboardを呼ぶッ！

urlpatterns = [
    path('admin/', admin.site.urls),
    # ↓ ここを空欄 '' にすることで、http://127.0.0.1:8000/ を開いた瞬間に表示されます
    path('', dashboard, name='dashboard'), 
]