
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail')
]

'''
it starts with ^ again – "the beginning".
post/ just means that after the beginning, the URL should contain the word post and a /. So far so good.
(?P<pk>\d+) – this part is trickier. It means that Django will take everything that you place here and transfer it to a view as a variable called pk. \d also tells us that it can only be a digit, not a letter (so everything between 0 and 9). + means that there needs to be one or more digits there. So something like http://127.0.0.1:8000/post// is not valid, but http://127.0.0.1:8000/post/1234567890/ is perfectly OK!
/ – then we need a / again.
$ – "the end"!

pk is an abbreviation for primary key. This name is often used in Django projects. But you can name your variable however you like. (But remember: lowercase, and _ instead of whitespaces!) For example, instead of (?P<pk>\d+) we could have the variable post_id, so this bit would look like (?P<post_id>\d+

'''
