import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import Navbar from "../../components/Navbar/Navbar";
import { User } from "../../interfaces/interfaces";
import { isLoggedIn, logout, retrieveLocalUser } from "../../utils/auth";
import VulnerabilityTable from "../VulnerabilityTable/VulnerabilityTable";
import "./Home.css";

function Home() {
  const { state }: { state: { user: User } } = useLocation();
  const [user, setUser] = useState<User | null>(null);
  const navigate = useNavigate();

  useEffect(() => {
    (async () => {
      await testLoginStatus();
      loadUser();
    })();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const handleLogout = () => {
    logout();
    navigate("/login");
  };

  const handleExpiredLogout = () => {
    logout();
    navigate("/login?token_expired=true");
  };

  const testLoginStatus = async () => {
    if (!(await isLoggedIn())) {
      handleExpiredLogout();
    }
  };

  const loadUser = () => {
    try {
      let { user: locationUser }: { user: User } = state;
      setUser(locationUser);
    } catch {
      let retrievedUser = retrieveLocalUser();
      if (retrievedUser) setUser(retrievedUser);
      else handleExpiredLogout();
    }
  };

  return (
    <div className="homepage">
      <Navbar handleLogout={handleLogout} user={user} />
      <VulnerabilityTable />
    </div>
  );
}

export default Home;
