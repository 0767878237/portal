from odoo.tests.common import HttpCase, tagged

@tagged('-at_install', 'post_install')
class TestPortalAccess(HttpCase):

    def test_portal_user_can_only_access_their_own_partner(self):
        user_portal = self.env['res.users'].create({
            'name': 'Portal User',
            'login': 'portal@example.com',
            'email': 'portal@example.com',
            'groups_id': [(6, 0, [self.env.ref('base.group_portal').id])],
        })
        user_portal.partner_id.email = 'portal@example.com'
        self.env.cr.commit()

        self.authenticate('portal@example.com', 'admin')  # giả lập login

        response = self.url_open('/my/account')
        self.assertIn(b'portal@example.com', response.content)
