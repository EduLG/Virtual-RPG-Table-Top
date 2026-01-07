import React, { useState } from "react";
import Modal from "../components/Modal";
import { Button } from "primereact/button";

const Login = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [visible, setVisible] = useState(false);

  return (
    <div>
      <Button
        label="log in"
        icon="pi pi-external-link"
        onClick={() => setVisible(true)}
      />

      <Modal visible={visible} setVisible={setVisible} />
    </div>
  );
};

export default Login;
