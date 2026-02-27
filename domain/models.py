from dataclasses import dataclass
from typing import Optional, List


def _safe_int(value: object, default: int = 0) -> int:
    """Coerce a value to int safely, returning default on failure."""
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _clamp(value: int, min_val: int, max_val: int) -> int:
    """Clamp an integer between min_val and max_val inclusive."""
    return max(min_val, min(max_val, value))

@dataclass
class TelemetryInput:
    """
    Represents the raw, structured input telemetry gathered from the user.
    This model contains the critical specifications required to contextually
    diagnose performance issues.
    """
    cpu: str
    gpu: str
    ram: str
    storage: str
    os_name: str
    application: str
    symptoms: str

    def format_prompt(self) -> str:
        return (
            f"## System Specs\n"
            f"- **CPU**: {self.cpu}\n"
            f"- **GPU**: {self.gpu}\n"
            f"- **RAM**: {self.ram}\n"
            f"- **Storage**: {self.storage}\n"
            f"- **OS**: {self.os_name}\n\n"
            f"## Target Application\n"
            f"{self.application}\n\n"
            f"## Reported Symptoms\n"
            f"{self.symptoms}\n"
        )

@dataclass
class Diagnosis:
    """
    Represents the core determination of the system bottleneck.
    Includes both a machine-readable category and plain-english rationale.
    """
    bottleneck_type: str
    severity: int
    plain_english: str
    reasoning: str
    secondary_bottleneck: Optional[str] = None

@dataclass
class Compatibility:
    """
    Represents the compatibility assessment of the target application
    running on the provided operating system and hardware tier.
    """
    score: int
    note: str

@dataclass
class Tweak:
    """
    Represents a single, safe, and reversible optimization recommendation
    provided to the user, including terminal commands and revert instructions.
    """
    title: str
    type: str
    safety: str
    steps: List[str]
    rationale: str
    commands: List[str]
    revert: str

@dataclass
class DoNotDo:
    """
    Represents a specific, explicit anti-pattern or dangerous action
    that the user is warned against attempting.
    """
    action: str
    reason: str

@dataclass
class DiagnosticResponse:
    """
    The top-level container for a complete, parsed diagnostic result
    returned from the Gemini reasoning engine.
    """
    diagnosis: Diagnosis
    compatibility: Optional[Compatibility]
    tweaks: List[Tweak]
    do_not_do: List[DoNotDo]

    @classmethod
    def from_dict(cls, data: dict) -> 'DiagnosticResponse':
        """Safely parses raw JSON dict into domain models."""
        
        diag_data = data.get("diagnosis", {})
        diagnosis = Diagnosis(
            bottleneck_type=str(diag_data.get("bottleneck_type", "Unknown")),
            severity=_clamp(_safe_int(diag_data.get("severity", 0)), 0, 10),
            secondary_bottleneck=diag_data.get("secondary_bottleneck"),
            plain_english=str(diag_data.get("plain_english", "")),
            reasoning=str(diag_data.get("reasoning", ""))
        )

        compat_data = data.get("compatibility")
        compatibility = None
        if compat_data:
            compatibility = Compatibility(
                score=_clamp(_safe_int(compat_data.get("score", 0)), 0, 100),
                note=str(compat_data.get("note", ""))
            )

        tweaks = []
        for t in data.get("tweaks", []):
            tweaks.append(Tweak(
                title=t.get("title", ""),
                type=t.get("type", ""),
                safety=t.get("safety", ""),
                steps=t.get("steps", []),
                commands=t.get("commands", []),
                revert=t.get("revert", ""),
                rationale=t.get("rationale", "")
            ))

        do_not_do = []
        for dnd in data.get("do_not_do", []):
            do_not_do.append(DoNotDo(
                action=dnd.get("action", ""),
                reason=dnd.get("reason", "")
            ))

        return cls(
            diagnosis=diagnosis,
            compatibility=compatibility,
            tweaks=tweaks,
            do_not_do=do_not_do
        )
