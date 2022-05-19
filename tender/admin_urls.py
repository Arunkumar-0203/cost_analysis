from django.urls import path

from tender.admin_views import IndexView, ApproveView, RejectView, NewSeniorView, NewGuestView, EngineerView, \
    GuestView,NewContractorView,ViewContractor, AddWorkDetails, ViewConWithTender,WorkStatusView, RequestFund, \
    RequestFundAccept

urlpatterns = [

    path('',IndexView.as_view()),
    path('approve',ApproveView.as_view()),
    path('reject',RejectView.as_view()),
    path('new_guest',NewGuestView.as_view()),
    path('new_senoir',NewSeniorView.as_view()),
    path('new_contractor',NewContractorView.as_view()),
    path('eng_view',EngineerView.as_view()),
    path('guest_view',GuestView.as_view()),
    path('view_contractor',ViewContractor.as_view()),
    path('add_work_details',AddWorkDetails.as_view()),
    path('view_contractor_tender',ViewConWithTender.as_view()),
    path('work_status_view',WorkStatusView.as_view()),
    path('request_fund',RequestFund.as_view()),
    path('request_fund_accept',RequestFundAccept.as_view()),



]
def urls():
      return urlpatterns,'admin','admin'
