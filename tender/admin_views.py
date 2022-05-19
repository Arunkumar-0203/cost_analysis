from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib import messages
from tender.models import  Senior, Guest, Work, Contractor, WorkDetails, AddPlan, AddWorkStatus, FundRequest


class IndexView(TemplateView):
    template_name = 'admin/admin_index.html'


class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.save()
        return render(request,'admin/admin_index.html',{'message':" Account Approved"})
        # if user.is_staff == 1:
        #     return HttpResponseRedirect("newhostels",{'message':"Hostel Approved"})
        # else:
        #     return HttpResponseRedirect("newusers",{'message':"Hostel Approved"})


class RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'
        user.is_active='0'
        user.save()
        return render(request,'admin/admin_index.html',{'message':"Account Removed"})
        # if user.is_staff=='1':
        #     return HttpResponseRedirect("newhostels",{'message':"Hostel Approved"})
        # else:
        #     return HttpResponseRedirect("newusers",{'message':"Hostel Approved"})



class NewGuestView(TemplateView):
    template_name = 'admin/new_guest.html'

    def get_context_data(self, **kwargs):
        context = super(NewGuestView,self).get_context_data(**kwargs)
        # Product.objects.get(company__account=account, company__pk=company_pk, pk=product_pk)

        # user = User.objects.filter(last_name='0',is_staff='1')
        # user = User()
        guest = Guest.objects.filter(user__last_name='0',user__is_staff='0')
        # context['users'] = user
        context['guest'] =  guest
        return context

class NewSeniorView(TemplateView):
    template_name = 'admin/new_senoir.html'

    def get_context_data(self, **kwargs):
        context = super(NewSeniorView,self).get_context_data(**kwargs)
        # Product.objects.get(company__account=account, company__pk=company_pk, pk=product_pk)

        # user = User.objects.filter(last_name='0',is_staff='1')
        # users = User()
        engineer = Senior.objects.filter(user__last_name='0',user__is_staff='0')
        # context['users'] = user
        context['engineer'] =  engineer
        return context



class EngineerView(TemplateView):
    template_name = 'admin/eng_view.html'

    def get_context_data(self, **kwargs):
        context = super(EngineerView,self).get_context_data(**kwargs)
        # Product.objects.get(company__account=account, company__pk=company_pk, pk=product_pk)

        # user = User.objects.filter(last_name='0',is_staff='1')
        # user = User()
        seniors = Senior.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')
        # context['users'] = user
        context['senior'] =  seniors
        return context

class GuestView(TemplateView):
    template_name = 'admin/guest_view.html'

    def get_context_data(self, **kwargs):
        context = super(GuestView,self).get_context_data(**kwargs)
        # Product.objects.get(company__account=account, company__pk=company_pk, pk=product_pk)

        # user = User.objects.filter(last_name='0',is_staff='1')
        # user = User()
        guests = Guest.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')
        # context['users'] = user
        context['guest'] =  guests
        return context


class NewContractorView(TemplateView):
    template_name = 'admin/new_contractor.html'

    def get_context_data(self, **kwargs):
        context = super(NewContractorView,self).get_context_data(**kwargs)
        # Product.objects.get(company__account=account, company__pk=company_pk, pk=product_pk)

        # user = User.objects.filter(last_name='0',is_staff='1')
        # user = User()
        contractor = Contractor.objects.filter(user__last_name='0',user__is_staff='0')
        # context['users'] = user
        context['contractor'] =  contractor
        return context

class ViewContractor(TemplateView):
    template_name = 'admin/contratcor_view.html'

    def get_context_data(self, **kwargs):
        context = super(ViewContractor,self).get_context_data(**kwargs)
        # Product.objects.get(company__account=account, company__pk=company_pk, pk=product_pk)

        # user = User.objects.filter(last_name='0',is_staff='1')
        # user = User()
        Contractors = Contractor.objects.filter(user__last_name='1',user__is_staff='0',user__is_active='1')
        # context['users'] = user
        context['Contractors'] =  Contractors
        return context


class AddWorkDetails(TemplateView):
    template_name = 'admin/add_work_details.html'
    def post(self, request,*args,**kwargs):
        name = request.POST['name']
        place = request.POST['place']
        details = request.POST['details']


        pro = WorkDetails()
        pro.name = name
        pro.place = place
        pro.details = details
        pro.save()
        return redirect('/admin/')



class ViewConWithTender(TemplateView):
    template_name = 'admin/view_tendered_contractor.html'

    def get_context_data(self, **kwargs):
        context = super(ViewConWithTender,self).get_context_data(**kwargs)
        Contractors = AddPlan.objects.filter(status='Confirm')
        context['Contractors'] =  Contractors
        return context


class WorkStatusView(TemplateView):
    template_name = 'admin/view_work_status.html'

    def get_context_data(self, **kwargs):
        context = super(WorkStatusView,self).get_context_data(**kwargs)
        id = self.request.GET['id']
        sta = AddWorkStatus.objects.filter(plans__work=id)
        context['sta'] =  sta
        return context


class RequestFund(TemplateView):
    template_name = 'admin/fund_request_view.html'

    def get_context_data(self, **kwargs):
        context = super(RequestFund,self).get_context_data(**kwargs)
        id = self.request.GET['id']
        re = FundRequest.objects.filter(work=id, status='requested').count()
        if re>0:
            e = FundRequest.objects.get(work=id, status='requested')
            context['re'] = e
            pl = AddPlan.objects.get(work=id,status='Confirm')
            context['pl'] = pl
            st = 'True'
            context['st'] = st
            return context
        else:
            st = 'False'
            context['st'] = st
            return context


class RequestFundAccept(TemplateView):

    def dispatch(self, request, *args, **kwargs):
        id = self.request.GET['id']
        fund = FundRequest.objects.get(work=id)
        amo = fund.amount
        add = AddPlan.objects.get(work=id, status='Confirm')
        esti = add.estimate

        total = int(esti)-int(amo)
        if total <= 0:

            messages.success(request, 'Cant Allocate fund Amount')
            return redirect('/admin')
        else:
            fund.status = 'FundAllocated'
            fund.save()
            add.estimate = total
            add.save()
            messages.success(request, 'Fund Successfully Released')
            return redirect('/admin')






