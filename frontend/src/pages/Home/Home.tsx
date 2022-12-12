import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { User } from "../../interfaces/interfaces";
import { isLoggedIn, logout } from "../../utils/auth";
import "./Home.css";

function Home() {
  const { state }: { state: { user: User } } = useLocation();
  const [user, setUser] = useState({});
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
    let { user: locationUser }: { user: User } = state;
    setUser(locationUser);
  };

  return (
    <>
      <div>Home</div>
      <p>User: {JSON.stringify(user)}</p>
      <div>
        <button className="btn btn-secondary" onClick={handleLogout}>
          Logout
        </button>
      </div>
    </>
  );
}

export default Home;
