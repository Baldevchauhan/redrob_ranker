import { useEffect, useState } from "react";

import Navbar from "../components/Navbar";
import SearchBar from "../components/SearchBar";
import CandidateCard from "../components/CandidateCard";
import CandidateTable from "../components/CandidateTable";
import ExportButton from "../components/ExportButton";

import { getCandidates } from "../services/api";

export default function Dashboard() {

  const [candidates, setCandidates] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");

  useEffect(() => {

    getCandidates()
      .then((res) => {
        console.log("API DATA:", res.data);
        setCandidates(res.data);
      })
      .catch((err) => {
        console.error(err);
      });

  }, []);

  // filtered ko state ki jagah direct derive karo
  const filtered = candidates.filter(
    (candidate) =>
      candidate.candidate_id
        .toString()
        .includes(searchTerm)
  );

return (
  <>
    <Navbar />

    <div className="min-h-screen bg-gradient-to-br from-[#0f1117] via-[#111827] to-[#020617] p-8 text-gray-200">

      {/* Top Bar */}
      <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4 mb-8">
        <SearchBar
          searchTerm={searchTerm}
          setSearchTerm={setSearchTerm}
        />

        <ExportButton />
      </div>

      {/* Heading */}
      <h2 className="text-2xl font-bold text-gray-100 mb-6 tracking-tight">
        🏆 Top 3 Candidates
      </h2>

      {/* Top Candidates Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 mb-10">

        {filtered.slice(0, 3).map((candidate, index) => (
          <div
            key={candidate.candidate_id}
            className="transform hover:-translate-y-1 hover:scale-[1.02] transition-all duration-300"
          >
            <div className="bg-white rounded-2xl shadow-md hover:shadow-xl p-4 border border-gray-100">
              <CandidateCard
                candidate={candidate}
                rank={index + 1}
              />
            </div>
          </div>
        ))}

      </div>

      {/* Total Count */}
      <div className="flex items-center justify-between mb-4">
        <p className="text-gray-600 text-sm">
          Total Candidates: 
          <span className="ml-1 font-semibold text-gray-800">
            {filtered.length}
          </span>
        </p>
      </div>

      {/* Table Section */}
      <div className="bg-white rounded-2xl shadow-md border border-gray-100 p-4">
        <CandidateTable candidates={filtered} />
      </div>

    </div>
  </>
);
}