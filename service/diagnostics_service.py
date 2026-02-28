"""
Zenith — Diagnostics Service Layer.

Coordinates telemetry validation, prompt construction, Gemini API
invocation via the Repository layer, and domain model hydration.
All business logic for the diagnostic flow lives here.
"""

import os
import logging
from domain.models import TelemetryInput, DiagnosticResponse
from domain.exceptions import (
    ConfigurationError,
    ValidationError,
    ExternalServiceError,
    DataParsingError,
)
from repository.gemini_client import GeminiDiagnosticsRepository

logger = logging.getLogger(__name__)


class DiagnosticsService:
    """Service layer coordinating telemetry analysis."""

    def __init__(self):
        # We fetch the API key from the environment securely in the service layer
        self.api_key = os.environ.get("GOOGLE_API_KEY", "").strip()
        if not self.api_key:
            logger.critical(
                "Failed to initialize DiagnosticsService: GOOGLE_API_KEY environment variable is not set."
            )
            raise ConfigurationError("GOOGLE_API_KEY environment variable is not set.")

        self.repository = GeminiDiagnosticsRepository(api_key=self.api_key)

    def _validate_telemetry(self, input_data: TelemetryInput) -> None:
        """Ensures all required telemetry fields are present."""
        if (
            not input_data.cpu.strip()
            or not input_data.gpu.strip()
            or not input_data.application.strip()
            or not input_data.os_name
            or not input_data.storage
        ):
            logger.warning(f"Telemetry validation failed. Input: {input_data}")
            raise ValidationError(
                "Missing arguments. Please fill in all required telemetry fields."
            )

    def run_diagnostics(self, telemetry: TelemetryInput) -> DiagnosticResponse:
        """Executes the core diagnostic sequence for a set of telemetry data.

        Args:
            telemetry (TelemetryInput): The system specifications and symptoms.

        Returns:
            DiagnosticResponse: The safely parsed and typed diagnostic results.

        Raises:
            ValidationError: If the telemetry input is incomplete.
            ConfigurationError: If the API key is missing.
            ExternalServiceError: If the LLM interaction fails.
            DataParsingError: If the returned JSON cannot be deserialized into known models.
        """
        self._validate_telemetry(telemetry)
        try:
            prompt = telemetry.format_prompt()
            raw_dict = self.repository.fetch_diagnosis(prompt)

            # Hydrate the domain models
            return DiagnosticResponse.from_dict(raw_dict)
        except ExternalServiceError as exc:
            logger.error(f"External service failure during diagnosis: {exc}")
            raise
        except Exception as exc:
            logger.error(f"Failed to hydrate domain models from payload: {exc}")
            raise DataParsingError(
                f"Failed to hydrate domain models from payload: {exc}"
            ) from exc
