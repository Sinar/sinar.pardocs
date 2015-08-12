from collective.grok import gs
from sinar.pardocs import MessageFactory as _

@gs.importstep(
    name=u'sinar.pardocs', 
    title=_('sinar.pardocs import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('sinar.pardocs.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
