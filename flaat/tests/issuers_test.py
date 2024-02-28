import pytest

from flaat.issuers import IssuerConfig, is_url
from flaat.test_env import FLAAT_AT, FLAAT_ISS, environment


class TestURLs:
    class TestURLs:
        def test_valid_url_http(self):
            assert is_url("http://example.org")

        def test_valid_url_https(self):
            assert is_url("https://example.org")

        def test_valid_url_ftp(self):
            assert is_url("ftp://example.org")

        def test_valid_url_https_path(self):
            assert is_url("https://example.org/thi_s&is=difficult")

        def test_short_url(self):
            assert is_url("https://keycloak")

        def test_valid_url_port(self):
            assert is_url("https://keycloak.example.org:2880")

        def test_valid_url_dot(self):
            assert is_url("https://keycloak.example.org.")

        def test_valid_url_localhost(self):
            assert is_url("https://localhost")

        def test_valid_url_ip(self):
            assert is_url("https://192.0.2.200")

        def test_valid_url_ip_port(self):
            assert is_url("https://192.0.2.200:8443")

        def test_invalid_url(self):
            assert not is_url("htp://example.org")

        def test_invalid_url_dot(self):
            assert not is_url("http://.example.org")

        def test_invalid_url_slash(self):
            assert not is_url("http:/keycloak.example.org")

        def test_invalid_url_no_slash(self):
            assert not is_url("http:keycloak.example.org")

        def test_invalid_url_no_colon(self):
            assert not is_url("http//keycloak.example.org")

        def test_invalid_url_port_letters(self):
            assert not is_url("http://keycloak.example.org:nah")


def test_token_introspection():
    client_id = environment.get("FLAAT_CLIENT_ID")
    client_secret = environment.get("FLAAT_CLIENT_SECRET")
    if client_id is None or client_secret is None:  # pragma: no cover
        pytest.skip("FLAAT_CLIENT_ID and FLAAT_CLIENT_SECRET are not set")

    issuer_config = IssuerConfig.get_from_string(FLAAT_ISS)
    assert issuer_config is not None
    issuer_config.client_id = client_id
    issuer_config.client_secret = client_secret
    introspection_info = issuer_config._get_introspected_token_info(FLAAT_AT)
    assert introspection_info is not None
