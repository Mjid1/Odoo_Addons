
from odoo import models,fields

class primera(models.Model):
    _name = "dam"

    name = fields.Char("Nom",required=True)
    lastname = fields.Char("Cognoms")
    Genere= fields.Selection(selection=[("home","Home"),("done","Dona"),("sense especificar","Sense especificar"),("prefiero-no-decir","Prefiero-no-decir")])
    Edat = fields.Integer(String="Edat")
    DNI = fields.Char(String="DNI")
    checkbox1 = fields.Boolean("Cicle Formatiu:ARI",help="Que ciclo tienes?")
    checkbox2 = fields.Boolean("Cicle Formatiu:DAM",help="Que ciclo tienes?")
    checkbox3 = fields.Boolean("Cicle Formatiu:AF",help="Que ciclo tienes?")
    checkbox4 = fields.Boolean("Cicle Formatiu:CI",help="Que ciclo tienes?")
    checkbox5 = fields.Boolean("Cicle Formatiu:MP",help="Que ciclo tienes?")
    date=fields.Date(string="Data de la inscripcio")
    DNI_copia = fields.Binary("Fotocopia DNI")
    Image = fields.Image("Fotografia alumne")


