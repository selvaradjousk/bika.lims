# -*- coding: utf-8 -*-
#
# This file is part of Bika LIMS
#
# Copyright 2011-2017 by it's authors.
# Some rights reserved. See LICENSE.txt, AUTHORS.txt.

from bika.lims.controlpanel.bika_instruments import InstrumentsView
from bika.lims import bikaMessageFactory as _


class InstrumentLocationInstrumentsView(InstrumentsView):

    def __init__(self, context, request):
        super(InstrumentLocationInstrumentsView, self).__init__(context, request)
        url = self.portal.absolute_url()
        url += "/bika_setup/bika_instruments/"
        self.context_actions = {_('Add'):
                                {'url': url + 'createObject?type_name=Instrument',
                                'icon': '++resource++bika.lims.images/add.png'}}

    def isItemAllowed(self, obj):
        location = obj.getInstrumentLocation() if obj else None
        return location.UID() == self.context.UID() if location else False
