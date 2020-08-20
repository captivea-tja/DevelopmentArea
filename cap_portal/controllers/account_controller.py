# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl)
import base64
from odoo import fields as odoo_fields, http, tools, _, SUPERUSER_ID
from odoo.exceptions import ValidationError, AccessError, MissingError, UserError
from odoo.http import content_disposition, Controller, request, route
from odoo.tools import consteq

from odoo.addons.portal.controllers.portal import CustomerPortal

CustomerPortal.OPTIONAL_BILLING_FIELDS.append('x_test_file')

class CustomCustomerPortal(CustomerPortal):

    @route(['/my/account'], type='http', auth='user', website=True)
    def account(self, redirect=None, **post):
        
        content = post.get('content')
        FileData = content.read()
        file_base64 = base64.encodestring(FileData)
        
        res = super(CustomCustomerPortal, self).account(redirect=None, **post)
        
        #test_file = post.get('x_test_file')
        #file_base64 = base64.encodestring(test_file.read())
        
        #post.update({'x_test_file': file_base64})
        
        return res

    
    
