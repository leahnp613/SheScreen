import { Link } from "react-router-dom";

export default function AboutUs() {
  return (
    <>
      <div className="main">
        <div className="main__heading-primary">
          <h1>About Us</h1>
        </div>

        <p className="main__text">
          Want all the tools for preventative women&#39;s healthcare in one
          place? <br /> SheScreen is the app for you!
        </p>

        <Link to="/Signup">
          <button className="appeal-button">
            sign up for free, and begin your health journey
          </button>
        </Link>

        <p className="main__text">Already have a SheScreen account?</p>
        <Link to="/Login">
          <button className="appeal-button">take me to the login page</button>
        </Link>
      </div>
    </>
  );
}
