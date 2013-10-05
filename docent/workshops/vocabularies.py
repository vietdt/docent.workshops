from five import grok

from zope.schema.interfaces import IVocabularyFactory, IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from docent.workshops import MessageFactory as _

class YesNoVocab(object):
    """
    Return a vocab of Yes and No
    """
    grok.implements(IVocabularyFactory)
    
    def __call__(self, context):
        return SimpleVocabulary([SimpleTerm(value=None, title=_(u'-- Select --')),
                                 SimpleTerm(value=u'yes', title=_(u'Yes')),
                                 SimpleTerm(value=u'no', title=_(u'No'))])
grok.global_utility(YesNoVocab, name=u"docent.workshops.vocab.yesno")

class ClassLengthVocab(object):
    """
    Return a vocab of numbers for Class Length
    """
    grok.implements(IVocabularyFactory)
    
    def __call__(self, context):
        return SimpleVocabulary([SimpleTerm(value=None, title=_(u'-- Select --')),
                                 SimpleTerm(value=75, title=_(u'75')),
                                 SimpleTerm(value=150, title=_(u'150')),
                                 SimpleTerm(value=225, title=_(u'225')),
                                 SimpleTerm(value=300, title=_(u'300'))])
grok.global_utility(ClassLengthVocab, name=u"docent.workshops.vocab.class_length")

class ClassSizeLimitVocab(object):
    """
    Return a vocab of numbers for Class Size Limit
    """
    grok.implements(IVocabularyFactory)
    
    def __call__(self, context):
        return SimpleVocabulary([SimpleTerm(value=None, title=_(u'-- Select --')),
                                 SimpleTerm(value=10, title=_(u'10')),
                                 SimpleTerm(value=15, title=_(u'15')),
                                 SimpleTerm(value=20, title=_(u'20')),
                                 SimpleTerm(value=25, title=_(u'25'))])
grok.global_utility(ClassSizeLimitVocab, name=u"docent.workshops.vocab.class_size_limit")

class BudgetRequestedVocab(object):
    """
    Return a vocab of numbers for Budget Requested
    """
    grok.implements(IVocabularyFactory)
    
    def __call__(self, context):
        return SimpleVocabulary([SimpleTerm(value=5, title=_(u'5')),
                                 SimpleTerm(value=10, title=_(u'10')),
                                 SimpleTerm(value=15, title=_(u'15')),
                                 SimpleTerm(value=25, title=_(u'25')),
                                 SimpleTerm(value=20, title=_(u'50'))])
grok.global_utility(BudgetRequestedVocab, name=u"docent.workshops.vocab.budget_requested")

class EquipmentRequestedBinder(object):
    grok.implements(IContextSourceBinder)

    def __call__(self, context):
        return SimpleVocabulary([SimpleTerm(value='tv-vcr', title=_(u'TV/VCR')),
                                 SimpleTerm(value='tv-dvd', title=_(u'TV/DVD')),
                                 SimpleTerm(value='easel', title=_(u'Easel')),
                                 SimpleTerm(value='digital-projector', title=_(u'Digital Projector')),
                                 SimpleTerm(value='overhead-projector', title=_(u'Overhead Projector')),
                                 SimpleTerm(value='screen', title=_(u'Screen'))])
equipment_required_binder = EquipmentRequestedBinder()
