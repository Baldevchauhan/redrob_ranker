import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:5000/api",
});

export const getCandidates = () =>
  API.get("/candidates");

export const getCandidate = (id) =>
  API.get(`/candidate/${id}`);

export const exportCSV = () =>
  window.open(
    "http://localhost:5000/api/export",
    "_blank"
  );