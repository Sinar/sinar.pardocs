from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

class categories(grok.GlobalUtility):
    grok.name('sinar.pardocs.categories')
    grok.implements(IVocabularyFactory)

    _terms = [{
        'value': 'agriculture',
        'title': 'Agriculture',
    },
    {
    'value': 'citizenship',
        'title': 'Citizenship',
    },
    {
    'value': 'civilservice',
        'title': 'Civil Service',
    },
    {
    'value': 'consumers',
        'title': 'Consumers',
    },
    {
        'value': 'corruption',
        'title': 'Corruption and Transparency',
    },
    {
    'value': 'defence',
        'title': 'Defence',
    },
    {
    'value': 'economy',
        'title': 'Economy',
    },
    {
    'value': 'education',
        'title': 'Education',
    },
    {
    'value': 'energy',
        'title': 'Energy',
    },
    {
    'value': 'environment',
        'title': 'Environment',
    },
    {
    'value': 'fishery',
        'title': 'Fishery',
    },
    {
    'value': 'foodsecurity',
        'title': 'Food Security',
    },
    {
    'value': 'foreignaffairs',
        'title': 'Foreign Affairs',
    },
    {
        'value': 'tariffsubsidy',
        'title': 'Tariffs and Subsidies',
    },
    {
    'value': 'glc',
        'title': 'GLC',
    },
    {
    'value': 'tax',
        'title': 'Taxation',
    },
    {
    'value': 'health',
        'title': 'Health',
    },
    {
    'value': 'homeaffairs',
        'title': 'Home Affairs',
    },
    {
    'value': 'humanresources',
        'title': 'Human Resources',
    },
    {
    'value': 'humanrights',
        'title': 'Human Rights',
    },
    {
    'value': 'indigenous',
        'title': 'Indigenous Affairs',
    },
    {
    'value': 'labour',
        'title': 'Labour Rights',
    },
    {
    'value': 'migrants',
        'title': 'Migrants and Refugees',
    },
    {
    'value': 'naturaldisasters',
        'title': 'Natural Disasters',
    },
    {
        'value': 'tourism',
        'title': 'Tourism',
    },
    {
        'value': 'gender',
        'title': 'Women and Gender',
        }
    ]

    def __call__(self, context):
        terms = []
        for i in self._terms:
            terms.append(SimpleTerm(**i))
        return SimpleVocabulary(terms)
