from aiogram import Router
from . import form

router = Router()

router.include_router(form.router)
