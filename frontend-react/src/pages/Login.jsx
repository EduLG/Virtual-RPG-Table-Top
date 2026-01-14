import React, { useState } from "react";
import LogRegModal from "../components/modals/LogRegModal";
import { Button } from "@radix-ui/themes";

const Login = () => {
  const [logRegVisible, setLogRegVisible] = useState(false);
  const [mode, setMode] = useState("login");

  return (
    <div
      style={{
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        minHeight: "100vh",
        gap: "1rem",
      }}
    >
      <Button
        label="Login"
        onClick={() => {
          setLogRegVisible(true);
          setMode("login");
        }}
      />
      <Button
        label="Register"
        onClick={() => {
          setLogRegVisible(true);
          setMode("register");
        }}
      />
      <LogRegModal
        visible={logRegVisible}
        setVisible={setLogRegVisible}
        mode={mode}
      />
    </div>
  );
};

export default Login;
