"""
OpenData - Python API for OpenGIN (Open General Information Network)

A comprehensive Python package for managing and processing government information,
including entity attributes, organizational charts, and data visualization.
"""

__version__ = "0.1.0"
__author__ = "GI-SERVICE Team"
__license__ = "MIT"

# Import public API components
from .models import (
    ENTITY_PAYLOAD,
    ATTRIBUTE_PAYLOAD,
    WRITE_PAYLOAD,
)

from .services import (
    IncomingServiceAttributes,
    IncomingServiceOrgchart,
    WriteAttributes,
)

from .dependencies import get_config

# Define public API
__all__ = [
    # Version info
    "__version__",
    "__author__",
    "__license__",
    
    # Models
    "ENTITY_PAYLOAD",
    "ATTRIBUTE_PAYLOAD",
    "WRITE_PAYLOAD",
    
    # Services
    "IncomingServiceAttributes",
    "IncomingServiceOrgchart",
    "WriteAttributes",
    
    # Dependencies
    "get_config",
]

