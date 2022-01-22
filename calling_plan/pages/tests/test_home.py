import pytest
from django.test import Client
from django.urls import reverse
from model_bakery import baker

from calling_plan.django_assertions import dj_assert_contains


@pytest.fixture
def resp(client: Client):
    return _resp(client)


def _resp(client):
    return client.get(reverse("pages:home"))


@pytest.fixture
def user(django_user_model):
    usr = baker.make(django_user_model)
    return usr


@pytest.fixture
def resp_with_user(user, client: Client):
    client.force_login(user)
    return _resp(client)


def test_profile_not_logged_user(resp):
    assert 302 == resp.status_code


"""def test_profile_status_code(resp_with_user):
    assert 200 == resp_with_user.status_code
"""
