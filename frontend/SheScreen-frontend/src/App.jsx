import { BrowserRouter, Routes, Route } from "react-router-dom";
import MainPage from "./MainPage";
import Signup from "./Signup";
import Login from "./Login";
import "./main.css";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="/Signup" element={<Signup />} />
        <Route path="/Login" element={<Login />} />
        <Route path="/UserProfileEdit" element={< UserProfileEdit />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
