from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal

class CustomerPortalExtended(CustomerPortal):

    @http.route(['/my/account'], type='http', auth="user", website=True)
    def account(self, **kw):
        partner = request.env.user.partner_id
        values = self._prepare_portal_layout_values()
        values.update({
            'partner': partner,
        })
        return request.render("customer_portal.portal_my_account", values)
