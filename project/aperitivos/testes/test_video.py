import pytest
from django.urls import reverse
from project.django_assertions import assert_contains


@pytest.fixture
def resp(client, video):
    return client.get(reverse('aperitivos:video', args=(video.slug,)))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp, video):
    assert_contains(resp, video.titulo)


def test_conteudo_video(resp, video):
    assert_contains(
        resp, f'<iframe src="https://player.vimeo.com/video/{video.vimeo_id}"')