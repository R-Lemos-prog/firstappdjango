import pytest
from django.urls import reverse
from project.django_assertions import assert_contains
from model_mommy import mommy
from project.modulos.models import Modulo


@pytest.fixture
def modulo(db):
    return mommy.make(Modulo)


@pytest.fixture
def aulas(modulo):
    return mommy.make(Aula, 3, modulo=modulo)


@pytest.fixture
def resp(client, modulo, aulas):
    resp = client.get(
        reverse('modulos:detalhe', kwargs={'slug': modulos.slug}))
    return resp


def test_titulos(resp, modulo: Modulo):
    assert_contains(resp, modulo.titulo)


def test_descricao(resp, modulo: Modulo):
    assert_contains(resp, modulo.descricao)


def test_publico(resp, modulo: Modulo):
    assert_contains(resp, modulo.publico)


def test_aula_modulo(resp, aulas):
    for aula in aulas:
        assert_contains(resp, modulo.titulo)
