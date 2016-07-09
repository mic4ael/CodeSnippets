#!/bin/env python

import gettext

en = gettext.translation('gettext_tests', 'locales_dir')
fr = gettext.translation('gettext_tests', 'locales_dir', languages=['fr'])

en.install()
print _('New message')
fr.install()
print _('New message')
