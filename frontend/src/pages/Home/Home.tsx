import { useEffect, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import Navbar from "../../components/Navbar/Navbar";
import TableCard from "../../components/TableCard/TableCard";
import { User } from "../../interfaces/interfaces";
import { isLoggedIn, logout } from "../../utils/auth";
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
    let { user: locationUser }: { user: User } = state;
    setUser(locationUser);
  };

  const columns = [
    {
      name: "Coluna1",
      key: "col1",
    },
    {
      name: "Coluna2",
      key: "col2",
    },
  ];

  const data = [
    {
      col1: "blabla",
      col2: 123,
    },
    {
      col1: "blabla",
      col2: 123,
    },
    {
      col1: "blabla",
      col2: 123,
    },
    {
      col1: "blabla",
      col2: 123,
    },
    {
      col1: "blabla",
      col2: 123,
    },
    {
      col1: "blabla",
      col2: 123,
    },
    {
      col1: "blabla",
      col2: 123,
    },
    {
      col1: "blabla",
      col2: 123,
    },
    {
      col1: "blabla",
      col2: 123,
    },
    {
      col1: "blabla",
      col2: 123,
    },
    {
      col1: "blabla",
      col2: 123,
    },
    {
      col1: "blabla",
      col2: 123,
    },
    {
      col1: "blabla",
      col2: 123,
    },
  ]

  return (
    <div className="homepage">
      <Navbar handleLogout={handleLogout} user={user} />
      <TableCard columns={columns} data={data} />
    </div>
  );
}

export default Home;
