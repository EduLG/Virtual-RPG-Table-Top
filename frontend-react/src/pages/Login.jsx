import React, { useState } from "react";
import LogRegModal from "../components/modals/LogRegModal";
import { Button } from "@radix-ui/themes";

const Login = () => {
  const [logRegVisible, setLogRegVisible] = useState(false);
  const [mode, setMode] = useState("login");
  const [userName, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");

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
        onClick={() => {
          setLogRegVisible(true);
          setMode("login");
        }}
      >
        Login
      </Button>
      <Button
        onClick={() => {
          setLogRegVisible(true);
          setMode("register");
        }}
      >
        Register
      </Button>
      <LogRegModal
        visible={logRegVisible}
        setVisible={setLogRegVisible}
        mode={mode}
        userName={userName}
        setUserName={setUserName}
        password={password}
        setPassword={setPassword}
        email={email}
        setEmail={setEmail}
      />
    </div>
  );
};

export default Login;
