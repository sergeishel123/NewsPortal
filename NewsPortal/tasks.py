from django.contrib.auth.models import User
from .models import Usersubscriberscategory,Category,PostCategory,Post
from django.core.mail import EmailMultiAlternatives,send_mail
from django.template.loader import render_to_string
from celery import shared_task
import time
from datetime import timedelta,datetime

def send_mail():
    user_massiv = []
    for category in Category.objects.all():
        for user_category in category.usersubscriberscategory_set.all():
            user_massiv.append(user_category.user)
    user_massiv = set(user_massiv)
    for user in user_massiv:
        category_user_obj = Usersubscriberscategory.objects.filter(user = user)
        print(len(category_user_obj), user)
        for i in category_user_obj:
            if PostCategory.objects.filter(category=i.category).exists():
                html_content = render_to_string(
                    'categories_every_week.html',
                    {
                        'Category': i.category,
                        'User': user,
                        'Posts': [k.post for k in PostCategory.objects.filter(category = i.category)]
                    }
                )

                msg = EmailMultiAlternatives(
                    subject = 'Обновления в категории',
                    body = '',
                    from_email = 'sergeiazharkov@yandex.ru',
                    to = [user.email]
                )
                msg.attach_alternative(html_content,'text/html')

                msg.send(user.email)


@shared_task
def send_email_every_8_hours_on_monday():

    Users = User.objects.all()
    for user in Users:
        html_content = render_to_string(
            'send_email_every_8_hours_on_monday.html',
            {'User': user,
            'Posts': Post.objects.filter(time_in__gte=datetime.now() - timedelta(weeks=1))
            })
        msg = EmailMultiAlternatives(
            subject='Последние новости',
            body='',
            from_email='sergeiazharkov@yandex.ru',
            to=[user.email]
        )
        msg.attach_alternative(html_content, 'text/html')

        msg.send(user.email)

@shared_task
def send():
    send_mail(
        subject='Привет!',
        message = 'Plhfd',
        from_email = 'sergeiazharkov@yandex.ru',
        recipient_list = ['max155@mail.ru']
    )

@shared_task
def printer(N):
    for i in range(N):
        time.sleep(1)
        print(i+1)









