from django.urls import path

from tender.guest_views  import IndexView, WorkViews, WorkingTenders, CompletedWorks

urlpatterns = [

    path('',IndexView.as_view()),
    path('work_view',WorkViews.as_view()),
    path('working_tenders',WorkingTenders.as_view()),
    path('completed_works',CompletedWorks.as_view()),


]
def urls():
    return urlpatterns,'guest','guest'