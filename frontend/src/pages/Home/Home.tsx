import { useLocation } from "react-router-dom";
import { User } from "../../interfaces/interfaces";
import "./Home.css";

function Home() {
  const { state }: { state: { user: User } } = useLocation();
  const { user }: { user: User } = state;

  return (
    <>
      <div>Home</div>
      <p>User: {JSON.stringify(user)}</p>
    </>
  );
}

export default Home;
