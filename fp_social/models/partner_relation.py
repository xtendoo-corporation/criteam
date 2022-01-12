# -*- coding: utf-8 -*-
# Copyright 2017 Pesol (<http://pesol.es>)
#                Angel Moya <angel.moya@pesol.es>
#                Luis Adan Jimenez Hernandez <luis.jimenez@pesol.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import models, fields, api


class RelationType(models.Model):
    _name = 'relation.type'

    name = fields.Char(
        string='Relation Type')

    reverse_id = fields.Many2one(
        comodel_name='relation.type',
        string='Reverse Relation Type')


class Relation(models.Model):
    _name = 'relation'

    src_partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Source Partner')

    relation_type_id = fields.Many2one(
        comodel_name='relation.type',
        string='Relation Type')

    dst_partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Destination Partner')

    @api.model
    def create(self,vals):
        res = super(Relation, self).create(vals)
        # Create reverse relation
        reverse_relation_type = self.env['relation.type'].browse(
            vals['relation_type_id']).reverse_id
        super(Relation, self).create({
            'src_partner_id': vals['dst_partner_id'],
            'relation_type_id': reverse_relation_type.id,
            'dst_partner_id': vals['src_partner_id']
        })
        return res

    @api.multi
    def unlink(self):
        # Unlink reverse relation
        reverse_relation = self.env['relation'].search([
            ('src_partner_id', '=', self.dst_partner_id.id),
            ('relation_type_id', '=', self.relation_type_id.reverse_id.id),
            ('dst_partner_id', '=', self.src_partner_id.id)
        ])
        if reverse_relation:
            self += reverse_relation
            
        return super(Relation, self).unlink()
