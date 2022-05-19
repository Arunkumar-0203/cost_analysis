from django.urls import path

from tender.senior_views  import IndexView, WorkView,  \
    AddWork, NewWorkView, PlanView, DownloadFile,ConfirmPlan, WorkStatusView, RequestFundsView

urlpatterns = [

    path('',IndexView.as_view()),
    path('work_view',WorkView.as_view()),
    path('add_work',AddWork.as_view()),
    path('new_work_view',NewWorkView.as_view()),
    path('plan_view',PlanView.as_view()),
    path('download',DownloadFile.as_view()),
    path('confirm_plan',ConfirmPlan.as_view()),
    path('work_status_view',WorkStatusView.as_view()),
    path('request_funds_view',RequestFundsView.as_view()),




]
def urls():
    return urlpatterns,'senior','senior'