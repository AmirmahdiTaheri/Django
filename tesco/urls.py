from  django.urls import path
from . import views

urlpatterns = [
    path(''                               , views.home                  , name="home"            ),
    path('txt/<int:txt_id>/'              , views.txt_detail            , name='txt_detail'      ),
    path('about/'                         , views.about_view            , name='about'           ),
    path('contact/'                       , views.contact_view          , name='contact'         ),
    path('categories/'                    , views.category_list_view    , name='category_list'   ),
    path('categories/<int:category_id>/'  , views.category_detail_view  , name='category_detail' ),
]