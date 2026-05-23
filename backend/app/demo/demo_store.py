"""
DemoStore — in-memory state for demo sessions.

Each demo session is identified by a UUID (demo_session_id).
The store holds an isolated copy of seed data per session.
No SQLAlchemy, no DB writes.
"""

import copy
import threading
from datetime import datetime, timezone

from app.demo.demo_seed import build_seed


class DemoStore:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._sessions = {}
        return cls._instance

    # ------------------------------------------------------------------
    # Session lifecycle
    # ------------------------------------------------------------------

    def create_session(self, session_id: str) -> None:
        """Populate a fresh isolated state for this demo session."""
        state = build_seed()
        state["user"]["id"] = session_id
        self._sessions[session_id] = {
            "created_at": datetime.now(timezone.utc),
            **state,
        }

    def get_session(self, session_id: str) -> dict | None:
        return self._sessions.get(session_id)

    def destroy_session(self, session_id: str) -> None:
        self._sessions.pop(session_id, None)

    def session_exists(self, session_id: str) -> bool:
        return session_id in self._sessions


# Singleton instance used across the app
demo_store = DemoStore()
