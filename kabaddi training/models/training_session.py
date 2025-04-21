from odoo import models, fields, api
from datetime import datetime

class TrainingSession(models.Model):
    _name = 'training.session'
    _description = 'Kabaddi Training Session'
    
    name = fields.Char(string='Session Name', required=True)
    date = fields.Date(string='Date', default=fields.Date.today)
    duration = fields.Float(string='Duration (hours)')
    focus_area = fields.Selection([
        ('raiding', 'Raiding'),
        ('defending', 'Defending'),
        ('stamina', 'Stamina'),
        ('teamwork', 'Teamwork')
    ], string='Focus Area')
    notes = fields.Text(string='Notes')
    
    player_id = fields.Many2one('kabaddi.player', string='Player', required=True)
    coach_id = fields.Many2one('res.users', string='Coach', default=lambda self: self.env.user)
    performance_rating = fields.Integer(string='Performance Rating (1-10)')