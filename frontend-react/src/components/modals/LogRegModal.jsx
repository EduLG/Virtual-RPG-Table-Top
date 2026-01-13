import React, { useState } from "react";
import { Button } from "primereact/button";
import { Dialog } from "primereact/dialog";

const LoginModal = ({ visible, setVisible, mode }) => {
  return (
    <div className="card flex justify-content-center">
      <Dialog
        visible={visible}
        onHide={() => {
          if (!visible) return;
          setVisible(false);
        }}
      >
        {mode === "login" ? <p>Login</p> : <p>Register</p>}
      </Dialog>
    </div>
  );
};

export default LoginModal;
