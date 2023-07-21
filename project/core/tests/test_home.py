import pytest
from django.urls import reverse
from project.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('core:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Python Pro - home</title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("core:home")}">Python Pro')


def test_email_link(resp):
    assert_contains(resp, 'href="mailto:ramalho@python.pro.br"')
