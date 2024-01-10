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

//PURPOSE
// SheScreen was created with women's health in mind, enabling women to take charge of their health and ensure all screening are current.
// At SheScreen we believe each woman deserves the opportunity to be informed with reliable information while providing one location for your all needs.

//DISCLAIMER
// this info is not ours it is generated through the NIH. the purpose of this app is informative, and not to provide medical advice.
// No personal identifying info will be stored. Contact a healthcare professional for any concerns or emergencies. Dial 911 or go to your
// nearest emergency room if you are experiencing a medical emergency.
