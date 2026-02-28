"""
Zenith — Gemini Diagnostics Repository.

This module encapsulates all interactions with the Google Gemini API.
No business logic lives here — only SDK calls, response validation,
and structured error wrapping.
"""

import json
import logging

from google import genai
from google.genai import types

from config import GEMINI_MODEL
from ui_constants import SYSTEM_PROMPT
from domain.exceptions import ExternalServiceError, DataParsingError

logger = logging.getLogger(__name__)


class GeminiDiagnosticsRepository:
    """Repository layer responsible strictly for interacting with the Google Gemini API."""

    def __init__(self, api_key: str) -> None:
        if not api_key:
            raise ExternalServiceError(
                "Gemini API key is required but was not provided."
            )
        self.client = genai.Client(api_key=api_key)
        logger.info("GeminiDiagnosticsRepository initialised successfully.")

    def fetch_diagnosis(self, structured_prompt: str) -> dict:
        """Send the structured telemetry prompt to Gemini and return the raw JSON dictionary.

        Args:
            structured_prompt: The markdown-formatted prompt containing system specs and symptoms.

        Returns:
            A dictionary parsed from the Gemini JSON response.

        Raises:
            ExternalServiceError: If the API request fails, times out, or returns an empty payload.
            DataParsingError: If the response cannot be parsed as valid JSON.
        """
        logger.info("Sending diagnostic prompt to Gemini API (model=%s).", GEMINI_MODEL)

        try:
            response = self.client.models.generate_content(
                model=GEMINI_MODEL,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT,
                    response_mime_type="application/json",
                    temperature=0.3,
                ),
                contents=structured_prompt,
            )
        except Exception as exc:
            logger.error("Gemini API call failed: %s", exc)
            raise ExternalServiceError(f"Gemini API generation failed: {exc}") from exc

        if not response or not response.text:
            logger.error("Gemini API returned an empty response.")
            raise ExternalServiceError("Gemini API returned an empty response.")

        logger.info("Gemini API returned %d characters.", len(response.text))

        try:
            parsed = json.loads(response.text)
            return parsed
        except json.JSONDecodeError as exc:
            logger.error("Failed to parse Gemini response as JSON: %s", exc)
            raise DataParsingError(
                f"Failed to parse Gemini response as JSON: {exc}"
            ) from exc
