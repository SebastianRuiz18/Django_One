from django.views.generic import  TemplateView

# HomPageViews is extending TemplateView
class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'
