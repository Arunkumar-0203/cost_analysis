from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import TemplateView, View

from tender.download import download
from tender.models import Work, AddPlan, AddWorkStatus, FundRequest
from django.contrib import messages

class IndexView(TemplateView):
    template_name = 'contractor/conindex.html'


class WorkView(TemplateView):
    template_name = 'contractor/view_work.html'

    def get_context_data(self, **kwargs):
        context = super(WorkView,self).get_context_data(**kwargs)
        work = Work.objects.all()
        context['work'] =  work
        return context


class AddPlans(TemplateView):
    template_name = 'contractor/add_plane.html'

    def get_context_data(self, **kwargs):
        context = super(AddPlans,self).get_context_data(**kwargs)
        id = self.request.GET['id']
        context['id']= id
        return context

    def post(self, request,*args,**kwargs):
        user = User.objects.get(id=self.request.user.id)




        plan = request.FILES['plan']
        complete = request.POST['complete']
        estimate = request.POST['estimate']
        deposit = request.POST['deposit']
        desc = request.POST['description']
        id = request.POST['work_id']

        work = Work.objects.get(pk=id)
        a = AddPlan.objects.filter(user=user, work=work).count()
        if a<=0:
            pr = AddPlan()
            pr.user = user
            pr.plan = plan
            pr.work = work
            pr.periodcompltete = complete
            pr.estimate = estimate
            pr.deposit = deposit
            pr.status = 'requested'
            pr.othdesc = desc
            pr.save()
            return redirect('/contractor/work_view')
        else:
            messages.success(request, 'You already requested')
            return redirect('/contractor/work_view')


class DownloadFile(View):
    def dispatch(self, request, *args, **kwargs):
        path = request.GET['path']
        download(request,path)
        return redirect('/contractor/work_view')


class ViewConfirmPlan(TemplateView):
    template_name = 'contractor/confirm_plan.html'

    def get_context_data(self, **kwargs):
        context = super(ViewConfirmPlan,self).get_context_data(**kwargs)
        user = User.objects.get(id=self.request.user.id)
        Con = AddPlan.objects.filter(status='Confirm',user=user)
        context['Con'] =  Con
        return context


class WorkStatus(TemplateView):
    template_name = 'contractor/add_work_status.html'

    def get_context_data(self, **kwargs):
        context = super(WorkStatus,self).get_context_data(**kwargs)
        id = self.request.GET['id']
        context['id'] = id
        return context

    def post(self, request,*args,**kwargs):

        desc = request.POST['desc']
        file = request.FILES['files']
        sta = request.POST['status']
        id = request.POST['plan']
        print(id)

        plan = AddWorkStatus.objects.filter(plans_id=id).count()

        if plan>0:
           pla = AddWorkStatus.objects.get(plans_id=id)
           pla.descri = desc
           pla.files = file
           pla.status = sta

           pla.save()
           messages.success(request, 'Status Updated')
           return redirect('/contractor/view_confirm_plan')

        else:
           pla = AddWorkStatus()
           pla. descri = desc
           pla.files = file
           pla.status = sta
           pl = AddPlan.objects.get(pk=id)

           pla.plans = pl

           pla.save()
           messages.success(request, 'Status Updated')
           return redirect('/contractor/view_confirm_plan')




class RequsetFund(TemplateView):
    template_name = 'contractor/request_for_fund.html'

    def get_context_data(self, **kwargs):
        context = super(RequsetFund,self).get_context_data(**kwargs)
        id = self.request.GET['id']
        context['id']= id
        return context

    def post(self, request,*args,**kwargs):

         user = User.objects.get(id=self.request.user.id)

         amount = request.POST['amount']
         desc = request.POST['desc']
         id = request.POST['works']

         requ = FundRequest.objects.filter(work_id=id,status = 'requested').count()

         if requ>0:
             messages.success(request, 'Your early request is not confirmed')
             return redirect('/contractor/view_confirm_plan')
         else:
             work = Work.objects.get(pk=id)
             pr = FundRequest()
             pr.user = user
             pr.amount = amount
             pr.work = work
             pr.status = 'requested'
             pr.description = desc
             pr.save()
             messages.success(request, 'Your request sent')
             return redirect('/contractor')


class RequestFundsView(TemplateView):
    template_name = 'contractor/fund_request_accept.html'

    def get_context_data(self, **kwargs):
        context = super(RequestFundsView,self).get_context_data(**kwargs)
        user = self.request.user.id
        re = FundRequest.objects.filter(user=user)
        context['re'] =  re
        return context








