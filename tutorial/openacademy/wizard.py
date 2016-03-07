# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Wizard(models.TransientModel):
    _name = 'openacademy.wizard'
    
    <!-- Define a default value for the session field in the wizard; 
    use the context parameter self._context to retrieve the current session. -->
    def _default_session(self):
        <-- Register for one session 
        return self.env['openacademy.session'].browse(self._context.get('active_id')) -->
        <-- Register for multiple sessions -->
        return self.env['openacademy.session'].browse(self._context.get('active_ids'))

    session_id = fields.Many2one('openacademy.session',
        string="Session", required=True, default=_default_session)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    
    <!-- Register attendees to one session 
    @api.multi
    def subscribe(self):
        self.session_id.attendee_ids |= self.attendee_ids
        return {} -->
        
    <!-- Register attendees to multiple sessions -->
    @api.multi
    def subscribe(self):
        for session in self.session_ids:
            session.attendee_ids |= self.attendee_ids
        return {}
