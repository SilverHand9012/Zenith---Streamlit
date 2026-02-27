"""
Zenith — Domain Exception Hierarchy.

All application-specific exceptions derive from ZenithException,
enabling the Controller layer to catch domain errors with a single
base class while preserving specific error semantics for logging.
"""


class ZenithException(Exception):
    """Base exception for all Zenith application errors."""
    pass

class ConfigurationError(ZenithException):
    """Raised when critical configuration (like API Keys) is missing or invalid."""
    pass

class ValidationError(ZenithException):
    """Raised when user telemetry input is invalid or incomplete."""
    pass

class ExternalServiceError(ZenithException):
    """Raised when an external service (e.g. Gemini API) fails or times out."""
    pass

class DataParsingError(ZenithException):
    """Raised when the models fail to parse data returned by an external service."""
    pass
