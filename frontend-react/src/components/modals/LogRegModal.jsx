import React, { useState } from "react";
import { Button } from "primereact/button";
import { Dialog } from "primereact/dialog";
import { InputText } from "primereact/inputtext";

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
        {mode === "login" ? (
          <>
            <h2>Log in</h2>
            <p>User Name:</p>
            <InputText />
            <p>Password:</p>
            <InputText />
          </>
        ) : (
          <>
            <h2>Register</h2>
            <p>Email:</p>
            <InputText />
            <p>User Name:</p>
            <InputText />
            <p>Password:</p>
            <InputText />
          </>
        )}
      </Dialog>
    </div>
  );
};

export default LoginModal;
