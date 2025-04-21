from odoo import models, fields, api

class KabaddiPlayer(models.Model):
    _name = 'kabaddi.player'
    _description = 'Kabaddi Player Information'

    name = fields.Char(string='Player Name', required=True)
    age = fields.Integer(string='Age')
    weight = fields.Float(string='Weight (kg)')
    height = fields.Float(string='Height (cm)')
    position = fields.Selection([
        ('raider', 'Raider'),
        ('defender', 'Defender'),
        ('allrounder', 'All-Rounder')
    ], string='Position')
    join_date = fields.Date(string='Join Date', default=fields.Date.today)
    active = fields.Boolean(string='Active', default=True)
    
    session_ids = fields.One2many('training.session', 'player_id', string='Training Sessions')
    total_sessions = fields.Integer(string='Total Sessions', compute='_compute_total_sessions')
    
    @api.depends('session_ids')
    def _compute_total_sessions(self):
        for player in self:
            player.total_sessions = len(player.session_ids)