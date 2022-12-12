import axios from "axios";
import { Token, User } from "../interfaces/interfaces";

interface LoginPayload {
  username: string;
  password: string;
}

export const login = async (credentials: LoginPayload): Promise<User> => {
  const apiBaseUrl = process.env.REACT_APP_API_URL;
  let loginUrl = apiBaseUrl + "login/";

  return axios.post(loginUrl, credentials).then((response) => {
    let { token, user } = response.data;
    saveAuthData(token, user);
    return user;
  });
};

export const logout = () => {
  const apiBaseUrl = process.env.REACT_APP_API_URL;
  let logoutUrl = apiBaseUrl + "logout/";
  let token = retrieveLocalToken();

  if (token) {
    axios
      .get(logoutUrl, {
        headers: {
          Authorization: `Token ${token}`,
        },
      })
      .catch((err) => {});
  }

  clearAuthData();
};

const saveAuthData = (token: Token, user: User) => {
  localStorage.setItem("jwt", token);
  localStorage.setItem("user", JSON.stringify(user));
};

const clearAuthData = () => {
  localStorage.removeItem("jwt");
  localStorage.removeItem("user");
}

export const retrieveLocalToken = (): Token | null => {
  let token = localStorage.getItem("jwt");
  return token;
};

export const retrieveLocalUser = (): User | null => {
  let user = localStorage.getItem("user");

  if (user) {
    return JSON.parse(user);
  }

  return null;
};
