# Copyright 2022 user
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('list', views.list, name='list'),
    # path('list', views.NotesListView.as_view(), name='list'),
    path('notes/<int:pk>', views.detail, name='detail'),
    path('testing', views.HomeView.as_view(), name='testing'),
    path('authTest', views.AuthView.as_view(), name='authTest'),
    path('notes/new', views.NotesCreateView.as_view(), name='notes.new'),
    path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name='notes.edit'),
    path('notes/<int:pk>/delete', views.NotesDeleteView.as_view(), name='notes.delete'),
]