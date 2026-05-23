function _decodePayload(token) {
  if (!token || typeof token !== "string") return null;
  try {
    const parts = token.split(".");
    if (parts.length < 2) return null;
    const b64 = parts[1].replace(/-/g, "+").replace(/_/g, "/");
    const padded = b64 + "=".repeat((4 - (b64.length % 4)) % 4);
    const raw = atob(padded);
    const json = decodeURIComponent(
      raw
        .split("")
        .map((c) => "%" + ("00" + c.charCodeAt(0).toString(16)).slice(-2))
        .join(""),
    );
    return JSON.parse(json);
  } catch {
    return null;
  }
}

export function getUserIdFromToken(token) {
  const payload = _decodePayload(token);
  if (!payload) return null;
  return payload.sub ?? payload.user_id ?? payload.identity ?? null;
}

export function isDemoToken(token) {
  const payload = _decodePayload(token);
  return payload?.is_demo === true;
}

export default getUserIdFromToken;
