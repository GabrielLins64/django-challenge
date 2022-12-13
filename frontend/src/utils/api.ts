import axios, { AxiosError, AxiosResponse } from "axios";
import { ListResponse, Vulnerability } from "../interfaces/interfaces";
import { retrieveLocalToken } from "./auth";

// Vulnerability Endpoints

export const fetchVulnerabilitiesList = async (
  page: number = 1
): Promise<ListResponse> => {
  const apiBaseUrl = process.env.REACT_APP_API_URL;
  let url = apiBaseUrl + `vulnerabilities?order_by=id,desc&page=${page}`;
  let token = retrieveLocalToken();

  return axios
    .get(url, {
      headers: {
        Authorization: `Token ${token}`,
      },
    })
    .then((res) => res.data)
    .catch((err) => {
      console.error(err);
    });
};

export const postVulnerability = async (
  vulnerability: Vulnerability
): Promise<AxiosResponse | AxiosError> => {
  const apiBaseUrl = process.env.REACT_APP_API_URL;
  let url = apiBaseUrl + `vulnerabilities/`;
  let token = retrieveLocalToken();

  return axios
    .post(url, vulnerability, {
      headers: {
        Authorization: `Token ${token}`,
      },
    })
    .then((res) => res)
    .catch((err: AxiosError) => err);
};

export const postVulnerabilityCSV = async (
  fileFormData: FormData
): Promise<AxiosResponse | AxiosError> => {
  const apiBaseUrl = process.env.REACT_APP_API_URL;
  let url = apiBaseUrl + `vulnerabilities/csv`;
  let token = retrieveLocalToken();

  return axios
    .post(url, fileFormData, {
      headers: {
        Authorization: `Token ${token}`,
        "Content-Type": "multipart/form-data",
      },
    })
    .then((res) => res)
    .catch((err: AxiosError) => err);
};
