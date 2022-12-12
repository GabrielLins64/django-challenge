import { useState } from "react";
import { User } from "../../interfaces/interfaces";
import ProfileModal from "../ProfileModal/ProfileModal";
import "./Navbar.css";

interface NavbarProps {
  handleLogout: () => void;
  user: User | null;
}

function Navbar({ handleLogout, user }: NavbarProps) {
  const [isProfileModalVisible, setIsProfileModalVisible] = useState(false);

  return (
    <nav className="navbar">
      <div className="container-fluid">
        <h1 className="navbar-brand">VMS</h1>

        <div className="right-controls">
          <button
            onClick={(e) => setIsProfileModalVisible(true)}
            className="btn btn-light profile-btn"
          ></button>
          <button className="btn btn-outline-light" onClick={handleLogout}>
            Logout
          </button>
        </div>
      </div>
      <ProfileModal
        visible={isProfileModalVisible}
        setIsVisible={setIsProfileModalVisible}
        user={user}
      />
    </nav>
  );
}

export default Navbar;
