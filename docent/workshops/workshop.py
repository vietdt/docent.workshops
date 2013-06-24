from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.component import getMultiAdapter
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.interface import invariant, Invalid

from z3c.form import group, field
from z3c.form.interfaces import HIDDEN_MODE

from Products.CMFCore.utils import getToolByName

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder

from docent.workshops import MessageFactory as _


# Interface class; used to define content-type schema.

class IWorkshop(form.Schema, IImageScaleTraversable):
    """
    This is used to propose a new workshop and for the board to review and decide.  When approved the workshop will be available to the campers to sign up
    """

    # If you want a schema-defined interface, delete the form.model
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/workshop.xml to define the content type
    # and add directives here as necessary.

    form.model("models/workshop.xml")


# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class Workshop(dexterity.Item):
    grok.implements(IWorkshop)

    # Add your class methods and properties here


class EditForm(dexterity.EditForm):
    grok.context(IWorkshop)


class AddForm(dexterity.AddForm):
    grok.name('docent.workshops.workshop')

    def updateWidgets(self):
        """ """
        dexterity.AddForm.updateWidgets(self)
        # autofill 'your name' and 'your email' based on login
        portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
        member = portal_state.member()
        if not self.widgets['your_name'].value:
            self.widgets['your_name'].value = member.getProperty('fullname')
        if not self.widgets['your_email'].value:
            self.widgets['your_email'].value = member.getProperty('email')


# View class
# The view will automatically use a similarly named template in
# workshop_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class SampleView(grok.View):
    grok.context(IWorkshop)
    grok.require('zope2.View')

    # grok.name('view')