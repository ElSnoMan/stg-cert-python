import pytest

from copart.pages.pages import CopartPages


@pytest.fixture
def copart(py):
    pages = CopartPages(py)
    py.visit('https://copart.com')
    return pages
