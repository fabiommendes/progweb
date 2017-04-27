from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel


class HomePage(Page):
    text = models.TextField()
    is_important = models.BooleanField(default=True)
    
    # Wagtail admin     
    content_panels = Page.content_panels + [
        FieldPanel('text'),
    ]
    promote_panels = Page.promote_panels + [
        FieldPanel('is_important'),
    ]
    
    
