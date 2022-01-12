# -*- coding: utf-8 -*-
# Copyright 2017 Pesol (<http://pesol.es>)
#                Angel Moya <angel.moya@pesol.es>
#                Luis Adan Jimenez Hernandez <luis.jimenez@pesol.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import models, fields


class ContratoTrabajo(models.Model):
    _name = 'contrato.trabajo'

    fecha = fields.Date(
        string='Fecha')

    puesto = fields.Text(
        string='Puesto')

    tipo_contrato = fields.Text(
        string='Tipo contrato')

    contacto_id = fields.Many2one(
        comodel_name='res.partner',
        string='Contacto')
