from zope.interface import alsoProvides, implements
from zope.component import adapts
from zope import schema
from plone.directives import form
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider

from plone.namedfile import field as namedfile
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.formwidget.contenttree import ObjPathSourceBinder

from sinar.pardocs import MessageFactory as _

class ICategories(form.Schema):
    """
       Marker/Form interface for Categories
    """

    # -*- Your Zope schema definitions here ... -*-
    pardocs_categories = schema.List(
            title = _(u'Categories'),
            value_type = schema.Choice(
                vocabulary = "sinar.pardocs.categories",
                ),
            required=False,
            )


alsoProvides(ICategories,IFormFieldProvider)
