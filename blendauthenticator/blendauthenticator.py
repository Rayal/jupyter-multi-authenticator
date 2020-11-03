"""
Custom Authenticator to use both the FirstUseAuthenticator as well as GoogleOAutthenticator at the same time.
"""

from firstuseauthenticator.firstuseauthenticator import FirstUseAuthenticator
from oauthenticator.google import GoogleOAuthenticator
from jupyterhub.auth import Authenticator
from tornado.web import MissingArgumentError

class BlendAuthenticator(GoogleOAuthenticator, FirstUseAuthenticator):
    """Mixes FirstUseAuthenticator with GoogleOAuthenticator
    """

    def authenticate(self, handler, data=None):
        authenticator = None
        self.log.info(type(handler))
        try:
            handler.get_argument("code")
            authenticator = GoogleOAuthenticator.authenticate(self, handler, data)
        except MissingArgumentError:
            authenticator = FirstUseAuthenticator.authenticate(self, handler, data)
        return authenticator
        
    def get_handlers(self, app):
        handlers = FirstUseAuthenticator.get_handlers(self, app) + GoogleOAuthenticator.get_handlers(self, app)
        self.log.info(handlers)
        return handlers
    