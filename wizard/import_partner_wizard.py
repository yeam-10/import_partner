#-*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError
import pandas as pd
import io
import base64

class ImportCsv(models.TransientModel):
    _name = "import.partner.wizard"
    _description = "Import user"

    fields_csv = fields.Binary(string="Import csv")


    def action_import_partner(self):
        if not self.fields_csv:
            raise UserError(_('Select excel.'))
        arch_io = io.BytesIO(base64.b64decode(self.fields_csv))
        df = pd.read_excel(arch_io, engine='openpyxl')
        ContactsObj = self.env['res.partner']

        for res in arch_io:
            name = res.get('name')
            phone = res.get('phone')
            email = res.get('email')
            ContactsObj.create({
                'name': name,
                'phone': phone,
                'email': email,
        
            })
        
        
