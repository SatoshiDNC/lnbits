import asyncio

from fastapi import APIRouter

from lnbits.db import Database
from lnbits.helpers import template_renderer
from lnbits.tasks import catch_everything_and_restart

db = Database("ext_cashu")

cashu_ext: APIRouter = APIRouter(prefix="/cashu", tags=["TPoS"])


def cashu_renderer():
    return template_renderer(["lnbits/extensions/cashu/templates"])


from .tasks import wait_for_paid_invoices
from .views import *  # noqa
from .views_api import *  # noqa


def cashu_start():
    loop = asyncio.get_event_loop()
    loop.create_task(catch_everything_and_restart(wait_for_paid_invoices))
