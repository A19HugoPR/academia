# -- coding: utf-8 -- 

from odoo import models, fields


class ProfesorRecord(models.Model):

    _name = "academia.profesor"
    _inherits = {'res.partner': 'partner_id'}

    nombre = fields.Char(string='Nombre',required=True)
    primer_apellido = fields.Char(string='Primer Apellido')
    segundo_apellido = fields.Char(string='Segundo Apellido')
    foto = fields.Binary(string='Foto')
    edad = fields.Integer(string='Edad')
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento")
    genero = fields.Selection([('h', 'Hombre'), ('m', 'Mujer'), ('o', 'Otro')], string='Género')
    nacionalidad = fields.Many2one('res.country', string='Nacionalidad')
    partner_id = fields.Many2one('res.partner',ondelete='cascade',require=True)

class AsignaturaRecord(models.Model):

    _name = "academia.asignatura"
    nombre = fields.Char(string='Nombre', required=True)
    temas = fields.Integer(string='Temas')
    tipo = fields.Selection([('c', 'Ciencias'), ('l', 'Letras'), ('i', 'Idiomas'), ('o', 'Otro')], string='Tipo')
    profesor = fields.Many2one('academia.profesor', string='Profesor')

    