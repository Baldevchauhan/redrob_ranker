import axios from "axios";
import.meta.env.VITE_API_URL

const API = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

export const getCandidates = () =>
  API.get("/candidates");

export const getCandidate = (id) =>
  API.get(`/candidate/${id}`);

export const exportCSV = () =>
  window.open(
    `${import.meta.env.VITE_API_URL}/export`,
    "_blank"
  );