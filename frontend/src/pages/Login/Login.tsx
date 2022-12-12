import { AxiosError } from "axios";
import { SyntheticEvent, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import Swal from "sweetalert2";
import { User } from "../../interfaces/interfaces";
import { isLoggedIn, login, retrieveLocalUser } from "../../utils/auth";
import "./Login.css";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    testLoginStatus();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const testLoginStatus = async () => {
    if (await isLoggedIn()) {
      let user = retrieveLocalUser();
      navigate("/home", { state: { user: user } });
    }
  };

  const handleSubmit = async (event: SyntheticEvent) => {
    event.preventDefault();

    login({ username, password })
      .then((user: User) => {
        navigate("/home", { state: { user: user } });
      })
      .catch((error) => {
        handleLoginFail(error);
      });
  };

  const handleLoginFail = (error: AxiosError) => {
    console.error(error);

    let errorTitle = "";
    let errorMessage = "";

    if (error?.response?.status === 401) {
      errorTitle = "Credenciais inválidas";
      errorMessage = "O usuário ou a senha inseridos estão incorretos.";
    } else {
      errorTitle = "Falha na conexão";
      errorMessage =
        "Houve um problema na conexão com o servidor. Por favor reporte o ocorrido a um administrador do sistema.";
    }

    Swal.fire({
      title: errorTitle,
      text: errorMessage,
      icon: "error",
      confirmButtonColor: "#9c2219",
      focusConfirm: false,
    });
  };

  return (
    <div className="whole-page-container">
      <div className="login-form-container">
        <form className="login-form">
          <h2>VMS Login</h2>

          <div className="input-box">
            <input
              className="form-control"
              id="username"
              placeholder="Usuário"
              value={username}
              onChange={(event) => {
                setUsername(event.target.value);
              }}
            />
            <input
              className="form-control"
              id="password"
              placeholder="Senha"
              type="password"
              value={password}
              onChange={(event) => {
                setPassword(event.target.value);
              }}
            />
          </div>

          <button
            type="submit"
            className="btn btn-success"
            onClick={handleSubmit}
          >
            Entrar
          </button>
        </form>
      </div>
    </div>
  );
}

export default Login;
