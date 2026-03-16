from pytest import fixture
from playwright.sync_api import Page


@fixture()
def page(context):
    page: Page = context.new_page()
    yield page