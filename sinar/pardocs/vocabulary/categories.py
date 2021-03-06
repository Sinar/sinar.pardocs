from five import grok
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory


class categories(grok.GlobalUtility):
    grok.name('sinar.pardocs.categories')
    grok.implements(IVocabularyFactory)

    # this should be written to automatically be generated from csv
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
        'value': 'constitution',
        'title': 'Constitutional',
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
        'value': 'employment',
        'title': 'Employment',
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
        'value': 'finance',
        'title': 'Finance',
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
        'value': 'gender',
        'title': 'Women and Gender',
        },
        {
        'value': 'glc',
        'title': 'GLC',
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
        'value': 'housing',
        'title': 'Housing',
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
        'value': 'localgov',
        'title': 'Local Government',
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
        'value': 'sports',
        'title': 'Sports and Recreation',
        },
        {
        'value': 'tariffsubsidy',
        'title': 'Tariffs and Subsidies',
        },
        {
        'value': 'tax',
        'title': 'Taxation',
        },
        {
        'value': 'trade',
        'title': 'Trade',
        },
        {
        'value': 'transportation',
        'title': 'Transportation',
        },
        {
        'value': 'tourism',
        'title': 'Tourism',
        }, ]

    def __call__(self, context):
        terms = []
        for i in self._terms:
            terms.append(SimpleTerm(**i))
        return SimpleVocabulary(terms)
