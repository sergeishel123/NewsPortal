from .models import *

from modeltranslation.translator import register, TranslationOptions
# импортируем декоратор для перевода и класс настроек, от которого будем наследоваться

@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('text',)

