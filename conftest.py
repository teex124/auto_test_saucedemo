import re

from pytest import fixture
from playwright.sync_api import Page


@fixture()
def page(context):
    page: Page = context.new_page()
    yield page



@fixture()
def block_images(page):
    def abort_image(route):
        route.abort()

    page.route(re.compile('/media'), abort_image)
    yield