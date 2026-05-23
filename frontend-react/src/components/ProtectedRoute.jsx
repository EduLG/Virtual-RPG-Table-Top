import { useEffect, useState } from "react";
import { Navigate, Outlet } from "react-router-dom";
import { apiFetch } from "../utils/apiFetch";

const ProtectedRoute = () => {
  // Initialize directly from localStorage — no synchronous setState inside the effect
  const [status, setStatus] = useState(
    () => localStorage.getItem("token") ? "checking" : "unauthorized"
  );

  useEffect(() => {
    if (!localStorage.getItem("token")) return; // already "unauthorized" from initial state

    const controller = new AbortController();

    apiFetch("/api/v1/users/me", { method: "GET", signal: controller.signal })
      .then((res) => {
        if (res.ok) {
          setStatus("ok");
        } else {
          localStorage.removeItem("token");
          localStorage.removeItem("refresh_token");
          setStatus("unauthorized");
        }
      })
      .catch((err) => {
        if (err.name !== "AbortError") setStatus("unauthorized");
      });

    return () => controller.abort();
  }, []);

  if (status === "checking") return null;
  if (status === "unauthorized") return <Navigate to="/login" replace />;
  return <Outlet />;
};

export default ProtectedRoute;
