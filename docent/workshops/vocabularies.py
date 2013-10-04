from five import grok

from zope.schema.interfaces import IVocabularyFactory
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