from django.urls import path

from tender.con_views  import IndexView,WorkView, AddPlans, DownloadFile, ViewConfirmPlan, WorkStatus, RequsetFund,RequestFundsView



urlpatterns = [

    path('',IndexView.as_view()),
    path('work_view',WorkView.as_view()),
    path('add_plane',AddPlans.as_view()),
    path('download',DownloadFile.as_view()),
    path('view_confirm_plan',ViewConfirmPlan.as_view()),
    path('work_status',WorkStatus.as_view()),
    path('request_fund',RequsetFund.as_view()),
    path('request_funds_view',RequestFundsView.as_view()),


]
def urls():
    return urlpatterns,'contractor','contractor'