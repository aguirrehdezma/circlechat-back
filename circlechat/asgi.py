import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import chatrooms.routing
from chatrooms.token_auth import TokenAuthMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'circlechat.settings')

# What's going on here?
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': TokenAuthMiddleware(
        URLRouter( # Map the urls for connections
            chatrooms.routing.websocket_urlpatterns
        )
    )
})
