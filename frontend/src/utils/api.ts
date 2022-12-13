import axios from "axios";
import { ListResponse } from "../interfaces/interfaces";
import { retrieveLocalToken } from "./auth";

// Vulnerability Endpoints

export const fetchVulnerabilitiesList = async (page: number = 1): Promise<ListResponse> => {
  const apiBaseUrl = process.env.REACT_APP_API_URL;
  let logoutUrl = apiBaseUrl + `vulnerabilities?page=${page}`;
  let token = retrieveLocalToken();

  return axios
    .get(logoutUrl, {
      headers: {
        Authorization: `Token ${token}`,
      },
    })
    .then((res) => res.data)
    .catch((err) => {
      console.error(err);
    });
};
