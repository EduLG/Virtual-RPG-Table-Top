import { Outlet } from "react-router-dom";
import loginImage from "../assets/resources/loginImage.png";

const LoginLayout = () => {
  return (
    <div
      style={{
        minHeight: "100vh",
        backgroundImage: `url(${loginImage})`,
        backgroundSize: "cover",
        backgroundPosition: "center",
        margin: "0px",
      }}
    >
      <Outlet />
    </div>
  );
};

export default LoginLayout;
