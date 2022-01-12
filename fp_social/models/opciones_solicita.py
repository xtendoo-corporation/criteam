# -*- coding: utf-8 -*-
# Copyright 2017 Pesol (<http://pesol.es>)
#                Angel Moya <angel.moya@pesol.es>
#                Luis Adan Jimenez Hernandez <luis.jimenez@pesol.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import models, fields


class OpcionesSolicita(models.Model):
    _name = 'opciones.solicita'
    _rec_name = 'nombre'

    nombre = fields.Char(
        string='Nombre')

    contacto_id = fields.Many2one(
        comodel_name='res.partner',
        string='Contacto')
