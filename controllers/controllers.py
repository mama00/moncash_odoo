# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import base64
import json
import logging
import requests
import werkzeug

from odoo import http, _
from odoo.http import request

_logger = logging.getLogger(__name__)

class MoncashController(http.Controller):

    """ Handles the redirection back from payment gateway to merchant site """
    _return_url = '/paymcent/monash/return/'

    def _get_return_url(self, **post):
        """ Extract the return URL from the data coming from moncash. """
        post = dict(post)
        return_url = '/shop/payment/validate'
        return return_url

    def moncash_validate_data(self, **post):
        """ Validate the data coming from moncash. """
        res = False
        reference = post['ORDERID']
        if reference:
            _logger.info('moncash: validated data')
            res = request.env['payment.transaction'
                              ].sudo().form_feedback(post, 'moncash_payment')
            return res

    @http.route('/payment/moncash/return', type='http', auth='none',
                methods=['GET', 'POST'], csrf=False)
    def moncash_return(self, **post):
        """ Gets the Post data from moncash after making payment """
        _logger.info('Beginning moncash form_feedback with post data %s',
                     pprint.pformat(post))  # debug
        return_url = self._get_return_url(**post)
        self.moncash_validate_data(**post)
        return werkzeug.utils.redirect(return_url)