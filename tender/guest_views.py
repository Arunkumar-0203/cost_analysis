from django.views.generic import TemplateView

from tender.models import Work,AddPlan, AddWorkStatus


class IndexView(TemplateView):
    template_name = 'guest/guest_index.html'


class WorkViews(TemplateView):
    template_name = 'guest/view_works.html'

    def get_context_data(self, **kwargs):
        context = super(WorkViews,self).get_context_data(**kwargs)
        work = Work.objects.filter(status='Posted')
        context['work'] =  work
        return context

class WorkingTenders(TemplateView):
    template_name = 'guest/now_doing_work.html'

    def get_context_data(self, **kwargs):
        context = super(WorkingTenders,self).get_context_data(**kwargs)
        plans = AddPlan.objects.filter(status='Confirm')
        context['plan'] =  plans
        return context



class CompletedWorks(TemplateView):
    template_name = 'guest/completed_works.html'

    def get_context_data(self, **kwargs):
        context = super(CompletedWorks,self).get_context_data(**kwargs)
        com = AddWorkStatus.objects.filter(status='Work Completed')
        context['com'] =  com
        return context