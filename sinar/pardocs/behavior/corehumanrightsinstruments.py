from zope.interface import alsoProvides, implements
from zope.component import adapts
from zope import schema
from plone.directives import form
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider

from plone.namedfile import field as namedfile
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.autoform import directives

from sinar.pardocs import MessageFactory as _

class ICoreHumanRightsInstruments(form.Schema):
    """
       Marker/Form interface for Core Human Rights Instruments
    """

    # -*- Your Zope schema definitions here ... -*-
    form.fieldset('categorization', fields=['pardocs_core_hr'])
    pardocs_core_hr= schema.List(
            title = _(u'Core International Human Rights Instruments'),
            value_type = schema.Choice(
                vocabulary = 'ploneun.vocabulary.core_human_rights',
                ),
            required=False,
            )

alsoProvides(ICoreHumanRightsInstruments,IFormFieldProvider)
