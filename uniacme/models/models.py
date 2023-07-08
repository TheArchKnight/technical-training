from odoo import fields, models, api
from odoo.exceptions import ValidationError
class SedeModel(models.Model):
    _name = "sede"
    _description = "Sede de la universidad"

    pais = fields.Char(required=True)


class EstudianteModel(models.Model):
    _inherit = "res.partner"
    carrera = fields.Char(required=True)
    sede = fields.Many2one('sede', string='Sede')

    @api.constrains('vat')
    def check_unique_vat(self):
        for record in self:
            existing_partner = self.env['res.partner'].search([('vat', '=', record.vat)])
            if existing_partner:
                raise ValidationError('El número de identificación ya existe para otro estudiante.')

class CandidatoModel(models.Model):
    _inherit = "res.partner"
    @api.constrains('vat')
    def check_unique_vat(self):
        for record in self:
            existing_partner = self.env['res.partner'].search([('vat', '=', record.vat)])
            if existing_partner:
                raise ValidationError('El número de identificación ya existe para otro candidato.')


class VotacionModel(models.Model):
    _name="voting"
    _description="Votacion de la UNIACME"
    descripcion = fields.Text()
    periodo = fields.Datetime()
#    candidatos = fields.Many2many('uniacme.candidato', string="Candidato")

    estado=fields.Selection(string="Estado",
                            selection=[("borrador","Borrador"), ("en_proceso","En proceso"), ("cerrada","Cerrada")],
                            default="borrador")

    def estado_proceso(self):
        votaciones = self.filtered(lambda v: v.estado=="borrador")
        votaciones.write({'estado':'en_proceso'})
        return True
    

