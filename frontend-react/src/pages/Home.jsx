import React from "react";
import { Button } from "primereact/button";

const Home = () => {
  const handleClick = () => {
    alert("El botón funciona!");
  };

  return (
    <div style={{ padding: "2rem", textAlign: "center" }}>
      <h1>Prueba de PrimeReact Theme</h1>
      <Button
        label="Botón Lara Dark Blue"
        severity="primary"
        icon="pi pi-check"
        onClick={handleClick}
      />
    </div>
  );
};

export default Home;
