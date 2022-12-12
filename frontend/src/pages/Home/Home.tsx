import { useLocation, useNavigate } from "react-router-dom";
import { User } from "../../interfaces/interfaces";
import { logout } from "../../utils/auth";
import "./Home.css";

function Home() {
  const { state }: { state: { user: User } } = useLocation();
  const { user }: { user: User } = state;
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate("/");
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
