from odoo import fields, models

class LibraryBookCategory(models.Model):
    _name = "library.book.category"
    _description = "Library Book Category"

    name = fields.Char(
        string="Name",
        required=True
    )

    _sql_constraints = [
        (
            "name_unique",
            "UNIQUE(name)",
            "Category name must be unique."
        )
    ]

