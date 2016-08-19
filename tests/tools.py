import random
from collections import namedtuple

from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from django.core import mail
from django.template.response import ContentNotRenderedError
from django.test import Client
from django.test import RequestFactory
from django.urls import reverse

UserTuple = namedtuple('UserTuple', ['name', 'email', 'password'])

_FACTORY = RequestFactory()


def last_mail():
    return mail.outbox[-1]


def random_user(name):
    name = '%s.%010d' % (name, random.randint(0, 1000000000))
    return UserTuple(name=name, email='%s@chalab.test' % name, password='sadhasdjasdqwdnasdbkj')


def make_user(u):
    return User.objects.create(username=u.name, email=u.email, password=u.password)


def make_request(url, user=None):
    r = _FACTORY.get(url)

    if user is not None:
        r.user = make_user(user)

    return r


def html(r):
    try:
        c = r.content
    except ContentNotRenderedError:
        r.render()
        c = r.content

    return BeautifulSoup(c, 'html.parser')


def register(c, u):
    r = c.post(reverse('account_signup'),
               {'username': u.name, 'email': u.email,
                'password1': u.password, 'password2': u.password})
    return r


def q2(f, c=None):
    c = c or Client()
    r = c.get(reverse(f))
    return r, html(r)


def q(f, c=None):
    _, html = q2(f, c=c)
    return html
