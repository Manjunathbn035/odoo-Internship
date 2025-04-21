# -*- coding: utf-8 -*-
##############################################################################
#
# Odoo, Open Source Management Solution
# Copyright (C) 2025 ZestyBeanz Technologies(<http://www.zbeanztech.com>)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'kabaddi_training',
    'version': '18.0.0.0',
    'summary': 'Manage Kabaddi Training Sessions and Players',
    'description': """
        This module helps manage kabaddi training sessions and track player progress.
    """,
    'author': 'manja',
    'website': 'www.zbeanztech.com',
    'category': 'Sports',
    'license': "LGPL-3",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/kabaddi_player_views.xml',
        'views/training_session_views.xml',
        'views/menu.xml',
    ],
    'test': [],
    'demo': [],
    'installable': True,
    'application': True,
}