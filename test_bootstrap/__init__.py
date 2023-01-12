import logging
from odoo import models

_logger = logging.getLogger(__name__)
class Sanitize(models.AbstractModel):
    def init(self):
        _logger.error("SANITIZATION")
