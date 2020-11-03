"""
BlendAuthenticator to let users set their password on first use or use Google OAuth to login.

After installation, you can enable this with:

```
c.JupyterHub.authenticator_class = 'blendauthenticator.BlendAuthenticator'
```
"""

from blendauthenticator.blendauthenticator import BlendAuthenticator

__all__ = [BlendAuthenticator]

