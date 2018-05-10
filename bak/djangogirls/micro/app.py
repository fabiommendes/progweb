from django.urls import path
import micro.urls


class App:
    def __init__(self):
        self.Model = Model

    def setting(self, **kwargs):
        pass

    def route(self, route, name=None):
        def decorator(func):
            url_name = name or func.__name__
            micro.urls.urlpatterns.append(
                path(route, func, name=url_name)
            )
            return func
        return decorator


class Model:
    pass