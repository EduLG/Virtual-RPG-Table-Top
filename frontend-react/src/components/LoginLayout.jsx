import { Outlet } from "react-router-dom";
import loginImage from "../assets/resources/dawn_of_the_explorers.png";

const LoginLayout = () => {
  return (
    <div
      style={{
        minHeight: "100vh",
        backgroundImage: `url(${loginImage})`,
        backgroundSize: "cover",
        backgroundPositionX: "center",
        backgroundPositionY: "30%",
        margin: "0px",
      }}
    >
      <Outlet />
    </div>
  );
};

export default LoginLayout;
