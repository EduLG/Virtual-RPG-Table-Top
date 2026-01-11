import bgImage from "../assets/resources/bgImage.png";

const MainLayout = ({ children }) => {
  return (
    <div
      style={{
        minHeight: "100vh",
        backgroundImage: `url(${bgImage})`,
        backgroundSize: "cover",
        backgroundPosition: "center",
        margin: "0px",
      }}
    >
      {children}
    </div>
  );
};

export default MainLayout;
