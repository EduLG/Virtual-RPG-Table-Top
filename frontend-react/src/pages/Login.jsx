import React, { useState } from "react";
import LogRegModal from "../components/modals/LogRegModal";
import { Button } from "primereact/button";

const Login = () => {
  const [logRegVisible, setLogRegVisible] = useState(false);
  const [mode, setMode] = useState("login");

  return (
    <div>
      <Button
        label="Login"
        icon="pi pi-check"
        onClick={() => {
          setLogRegVisible(true);
          setMode("login");
        }}
      />
      <Button
        label="Register"
        icon="pi pi-check"
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
