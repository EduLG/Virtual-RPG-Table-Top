import React, { useState } from "react";
import LoginModal from "../components/modals/LoginModal";
import { Button } from "primereact/button";

const Login = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [visible, setVisible] = useState(false);

  return (
    <div>
      <Button label="Click Me" icon="pi pi-check" className="p-button-raised" />
    </div>
  );
};

export default Login;
