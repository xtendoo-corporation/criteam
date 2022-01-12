# -*- coding: utf-8 -*-
# Copyright 2017 Pesol (<http://pesol.es>)
#                Angel Moya <angel.moya@pesol.es>
#                Luis Adan Jimenez Hernandez <luis.jimenez@pesol.es>
#                Guillermo Castillo <gcastillo@cxritean.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)


{
    'name': 'FP Social',
    'version': '11.0.1.0.2',
    'license': 'AGPL-3',
    'category': 'Education',
    'sequence': 1,
    'complexity': 'easy',
    'author': 'PESOL, CRITEAN, Odoo Community Association (OCA)',
    'depends': [
        'base',
        'contacts',
        'education',
        'education_crm',
        'education_timetable',
        'education_certification',
        'education_evaluation',
        'education_course_pack',
        'web_responsive',
        'base_location',
        'l10n_es',
        'l10n_es_account_invoice_sequence',
        'l10n_es_partner',
        'l10n_es_toponyms'
    ],
    'data': [
        'data/default_relations.xml',
        'views/res_partner_view.xml',
        'views/opciones_solicita_view.xml',
        'security/partner_security.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
}
