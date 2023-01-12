import logging
from odoo import models

_logger = logging.getLogger(__name__)


class Sanitize(models.AbstractModel):
    _name = "sanitization"

    def init(self):
        _logger.error("SANITIZATION")
