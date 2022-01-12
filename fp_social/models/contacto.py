# -*- coding: utf-8 -*-
# Copyright 2017 Pesol (<http://pesol.es>)
#                Angel Moya <angel.moya@pesol.es>
#                Luis Adan Jimenez Hernandez <luis.jimenez@pesol.es>
#                Guillermo Castillo <gcastillo@critean.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import models, api, fields, _
import time


class Partner(models.Model):
    _inherit = 'res.partner'

    ### FICHA PARTICIPANTES ###

    genero = fields.Selection(
        [('masculino', 'Masculino'),
         ('femenino', 'Femenino'),
         ('no_binario', 'No Binario')],
        string='Identidad de Género')

    telefono_2 = fields.Char(
        string='Teléfono 2')
    telefono_3 = fields.Char(
        string='Teléfono 3')

    fecha_solicitud = fields.Date(
        string='Fecha de solicitud')

    fecha_nacimiento = fields.Date(
        string='Fecha de Nacimiento')

    fecha_alta = fields.Date(
        string='Fecha alta')
    fecha_baja = fields.Date(
        string='Fecha baja')

    ### DATOS GENERALES/SOLICITUD ###

    nivel_estudios = fields.Selection(
        [('educaccion_primaria', 'Educacion Primaria'),
         ('1_eso', '1º ESO'),
         ('2_eso', '2º ESO'),
         ('3_eso', '3º ESO'),
         ('eso', 'ESO'),
         ('grado_bachillerato', 'Grado Medio/Bachillerato'),
         ('grado_superior', 'Grado Superior'),
         ('grado_universitario', 'Grado Universitario'),
         ('master', 'Master'),
         ('doctorado', 'Doctorado'),
         ('fpb', 'FPB'),
         ('pci', 'PCI'),
         ('otros', 'Otros')],
        string='Nivel de estudios')

    nivel_estudios_especifico = fields.Char(
        string='Especificar')

    opciones_solicita_ids = fields.Many2many(
        comodel_name='opciones.solicita',
        string='Opciones que solicita')

    datos_derivacion = fields.Selection(
        [('pagina_web', 'Página web'),
         ('a_traves_alumnado', 'A través del alumnado'),
         ('orientacion_centro_educativo', 'Orientación del Centro Educativo'),
         ('orientacion_centros_sociolaboral', 'Orientación de Centros Sociolaboral'),
         ('orientacion_centro_municipal_servicios_sociales', 'Orientación del Centro Municipal de Servicios Sociales')],
        string='Datos de derivación')

    observaciones_datos_generales = fields.Text(
        string='Observaciones')

    documentos = fields.Binary(
        string='Subir documentos')
    documentos_nombre = fields.Char(
        string='Nombre del documento')

    pasaporte = fields.Binary(
        string='Pasaporte')
    pasaporte_nombre = fields.Char(
        string='nombre del pasaporte')

    iai_documento = fields.Binary(
        string='Documento IAI')
    iai_nombre = fields.Char(
        string='Nombre IAI')

    cr = fields.Binary(
        string='CR')
    cr_nombre = fields.Char(
        string='Nombre CR')

    bl = fields.Binary(
        string='BL')
    bl_nombre = fields.Char(
        string='Nombre BL')

    otro_documento = fields.Binary(
        string='Otro Documento')
    otro_documento_nombre = fields.Char(
        string='Nombre otro documento')

    alergia_o_enfermedades = fields.Text(
        string='Alergias o enfermedades a tener en cuenta')

    ### DATOS SOCIALES ###

    nombre_genograma = fields.Char(
        string='Nombre genograma')

    genomana_download = fields.Binary(
        string='Genograma Download',
        related='self.genograma')

    genograma = fields.Binary(
        string='Genograma Familiar')

    nucleo_convivencia = fields.Text(
        string='Nucleo de convivencia')

    objetivos_area_social = fields.Text(
        string='Objetivos')

    # programa_sociales = fields.Selection(
    #     [('programa_1', 'Programa 1'),
    #      ('programa_2', 'Programa 2'),
    #      ('programa_3', 'Programa 3')],
    #     string='Programa sociales que intervienen')

    iai_texto = fields.Boolean(
        string='IAI')
    centro_municipal = fields.Boolean(
        string='Centro municipal/Servicios sociales')

    familia_numerosa = fields.Boolean(
        string='Familia Numerosa')
    familia_monoparental = fields.Boolean(
        string='Familia Monoparental')

    minoria_etnica = fields.Boolean(
        string='Minoria étnica')
    migrante = fields.Boolean(
        string='Migrante')

    menores = fields.Boolean(
        string='Menores')
    salud_mental = fields.Boolean(
        string='Salud mental')
    fiscalia = fields.Boolean(
        string='Fiscalía')
    tutela = fields.Boolean(
        string='Tutela de adultos')
    adicciones = fields.Boolean(
        string='Adicciones')
    otros = fields.Boolean(
        string='Otros')
    ingresos_inferiores_iprem = fields.Boolean(
        string='Ingresos inferiores al IPREM')

    diario = fields.Text(
        string='DIARIO')

    ### AREA FORMATIVO/LABORAL ###

    objetivos_area_formativa = fields.Text(
        string='OBJETIVOS')

    antecedentes_educativos = fields.Text(
        string='Antecedentes educativos')

    observaciones_area_formativo = fields.Text(
        string='OBSERVACIONES')

    senalar_procedan = fields.Selection(
        [('procedan_1', 'Procedan 1'),
         ('procedan_2', 'Procedan 2'),
         ('procedan_3', 'Procedan 3')],
        string='Señalar las que procedan')

    formacion_realizada = fields.Text(
        string='Formación realizada')

    contratos_trabajo_ids = fields.Many2many(
        comodel_name='contrato.trabajo',
        relation='res_partner_contrato_trabajo_rel',
        column1='contacto_id',
        column2='contrato_id',
        string='Laboral')

    orientaciones = fields.Text(
        string='ORIENTACIONES')

    estudiando = fields.Boolean(
        string='Estudiando')

    trabajando = fields.Boolean(
        string='Trabajando')

    desempleado = fields.Boolean(
        string='Desempleado')

    ### AREA DE SALUD ###

    discapacidad_fisica = fields.Boolean(
        string='Física')

    discapacidad_intelectual = fields.Boolean(
        string='Intelectual')

    discapacidad_sensorial = fields.Boolean(
        string='Sensorial')

    discapacidad_enf_mental = fields.Boolean(
        string='Enfermedad Mental')

    otros_problema_salud = fields.Text(
        string='OTROS PROBLEMAS DE SALUD')

    objetivos_area_salud = fields.Text(
        string='OBJETIVOS')

    observaciones_area_salud = fields.Text(
        string='OBSERVACIONES')

    certificado_discapacidad = fields.Binary(
        string='CERTIFICADO DE DISCAPACIDAD')

    nombre_certificado_discapacidad = fields.Text(
        string='Certificado discapacidad')

    dictamen_tecnico = fields.Text(
        string='Dictamen técnico')

    grado = fields.Text(
        string='Grado')

    ### AREA DE VIVIENDA ###

    pia = fields.Binary(
        string='PIA')
    pia_nombre = fields.Char(
        string='Nombre PIA')

    pai = fields.Binary(
        string='PAI')
    pai_nombre = fields.Char(
        string='Nombre PAI')

    # informes_cr_bl_pia_pai = fields.Text(
    #     string='Adjuntar informes CR/BL/PIA/PAI')

    registros = fields.Text(
        string='Diario')

    activity_count = fields.Integer(
        string='Activity Count',
        compute='_compute_partner_activities')

    activity_ids = fields.One2many(
        comodel_name='mail.activity',
        inverse_name='partner_id',
        string='Activities')

    relacion = fields.Char(
        string='Relación')

    documents_ids = fields.One2many(
        comodel_name='binary.file',
        inverse_name='partner_id',
        string='Documentos'
    )

    ### ADICIONALES ###

    origen_extranjero = fields.Boolean(
        string='Origen extranjero')

    familia_sin_empleo = fields.Boolean(
        string='Familia sin empleo')

    pais_de_origen = fields.Many2one(
        comodel_name='res.country',
        string='País de Origen')

    relaciones = fields.One2many(
        comodel_name='relation',
        inverse_name='src_partner_id',
        string='Relaciones')
# cambios gcastillo  #
    causas_baja = fields.Selection(
        [('incorporacion_laboral', 'Incorporación al mundo laboral'),
         ('incorporacion_otro_proceso_formativo', 'Incorporación en otro proceso formativo'),
         ('motivos_familiares_personales', 'Motivos familiares/personales'),
         ('cambio_domicilio', 'Cambio de domicilio'),
         ('abandono', 'Abandono'),
         ('inasistencia_reiterada', 'Inasistencia reiterada'),
         ('incumplimiento_grave_normas', 'Incumplimiento grave de las normas de convivencia'),
         ('otros', 'Otros')],
        string='Causas de baja')

    @api.multi
    def _compute_partner_activities(self):
        for record in self:
            activiy_obj = self.env['mail.activity'].search_count([
                ('partner_id', '=', record.id)
            ])
            record.activity_count = activiy_obj


class MailActivity(models.Model):
    _inherit = 'mail.activity'

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Partner')


class BinaryFile(models.Model):
    _name = 'binary.file'

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Partner'
    )

    filename = fields.Char(
        string='File Name'
    )

    file = fields.Binary(
        string='File'
    )

    notes = fields.Char(
        string='File Notes'
    )

    date = fields.Datetime(
        string='Date',
        default=lambda *a: time.strftime('%Y-%m-%d %H:%M:%S'))
