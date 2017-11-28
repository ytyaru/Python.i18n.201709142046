import gettext
import os
#gettext.install('hello')
#gettext.install('hello', os.path.join(os.path.dirname(__file__), 'locale'))
_ = gettext.translation(
        domain='hello',
        localedir=os.path.join(os.path.dirname(__file__)),
        fallback=True).gettext

print(_('Hello World !!'))
