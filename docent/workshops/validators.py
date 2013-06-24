import re

from z3c.form.validator import SimpleFieldValidator

from zope.interface import Invalid

from docent.workshops import MessageFactory as _

class EmailValidator(SimpleFieldValidator):
    regex = r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"

    def validate(self, value):
        super(EmailValidator, self).validate(value)
        if not re.match(self.regex, value) or value.endswith('.'):
            raise Invalid(_("Not a valid e-mail address"))

