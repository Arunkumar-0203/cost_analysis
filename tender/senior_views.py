from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib import messages
from tender.download import download
from tender.models import Contractor, Work, AddPlan, WorkDetails, AddWorkStatus, FundRequest


class IndexView(TemplateView):
    template_name = 'senior/senior_index.html'


class WorkView(TemplateView):
    template_name = 'senior/view_work.html'

    def get_context_data(self, **kwargs):
        context = super(WorkView,self).get_context_data(**kwargs)
        user = self.request.user.id
        work = Work.objects.filter(user=user)
        context['work'] =  work
        return context


class AddWork(TemplateView):
    template_name = 'senior/add_work.html'

    def post(self, request,*args,**kwargs):
        user = User.objects.get(id=self.request.user.id)
        fullname = request.POST['name']
        estimate = request.POST['estimate']
        period = request.POST['period']
        tend = request.FILES['tender']
        last = request.POST['last']
        other = request.POST['other']


        pro = Work()
        pro.name = fullname
        pro.estiamount = estimate
        pro.user = user
        pro.periodcompltete = period
        pro.tenddocm = tend
        pro.status = 'Posted'
        pro.lastdatesub = last
        pro.othdesc = other
        pro.save()
        return redirect('/senior/')


class NewWorkView(TemplateView):
    template_name = 'senior/view_irrigation_work.html'

    def get_context_data(self, **kwargs):
        context = super(NewWorkView,self).get_context_data(**kwargs)
        works = WorkDetails.objects.all()
        context['works'] =  works
        return context

class PlanView(TemplateView):
    template_name = 'senior/view_con_plan.html'

    def get_context_data(self, **kwargs):
        context = super(PlanView,self).get_context_data(**kwargs)
        user = self.request.user.id
        plans = AddPlan.objects.filter(status='requested',work__user=user)
        context['pla'] =  plans
        return context


class DownloadFile(View):
    def dispatch(self, request, *args, **kwargs):
        path = request.GET['path']
        download(request,path)
        return redirect('/senior/plan_view')


class ConfirmPlan(View):

    def get(self, request, *args, **kwargs):
        user = User.objects.get(pk=self.request.user.id)
        id = self.request.GET['id']
        planid = self.request.GET['planid']
        co = AddPlan.objects.filter(work__user=user, work=id,status='Confirm').count()
        if co<=0:
            con = AddPlan.objects.get(pk=planid)
            con.status = 'Confirm'
            con.save()
            wor = Work.objects.get(pk=id)
            wor.status = 'Allocated'
            wor.save()
            return  redirect('/senior/plan_view')
        else:
            messages.success(request, 'You already confirmed')
            return redirect('/senior/plan_view')


class WorkStatusView(TemplateView):
    template_name = 'senior/view_work_status.html'

    def get_context_data(self, **kwargs):
        context = super(WorkStatusView,self).get_context_data(**kwargs)
        user = self.request.user.id
        sta = AddWorkStatus.objects.filter(plans__work__user=user)
        context['sta'] =  sta
        return context


class RequestFundsView(TemplateView):
    template_name = 'senior/fund_accept_view.html'

    def get_context_data(self, **kwargs):
        context = super(RequestFundsView,self).get_context_data(**kwargs)
        user = self.request.user.id
        re = FundRequest.objects.filter(work__user=user)
        context['re'] =  re
        return context


