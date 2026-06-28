import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getCandidate } from "../services/api";

export default function CandidateDetails() {
  const { id } = useParams();

  const [candidate, setCandidate] = useState(null);

  useEffect(() => {
    getCandidate(id)
      .then((res) => {
        setCandidate(res.data);
      })
      .catch((err) => {
        console.error(err);
      });
  }, [id]);

  if (!candidate) {
    return <div className="p-6 text-white">Loading...</div>;
  }

 return (
    <div className="min-h-screen bg-gradient-to-br from-[#0f1117] via-[#111827] to-[#0f172a] text-gray-200 p-6">

      {/* TITLE */}
      <h1 className="text-3xl font-bold mb-6 text-white">
        Candidate Details
      </h1>

      <div className="grid grid-cols-1 lg:grid-cols-4 gap-6">

        {/* ================= LEFT PROFILE CARD ================= */}
        <div className="bg-[#16171d] rounded-3xl p-6 border border-gray-800 shadow-xl text-center">

          <img
            src="https://i.pravatar.cc/100"
            alt="profile"
            className="w-24 h-24 rounded-full mx-auto border-4 border-yellow-400"
          />

          <h2 className="text-xl font-semibold text-white mt-4">
            {candidate.candidate_id}
          </h2>

          <p className="text-gray-400 text-sm">
            Full Stack Developer
          </p>

          <button className="mt-4 px-5 py-2 bg-yellow-400 text-black rounded-full font-medium hover:scale-105 transition">
            Send Message
          </button>

          {/* SKILLS */}
          <div className="mt-6">
            <h3 className="text-sm text-gray-400 mb-2">Skills</h3>
            <div className="flex flex-wrap justify-center gap-2">
              {candidate.skills?.slice(0, 6).map((skill, i) => (
                <span
                  key={i}
                  className="bg-gray-800 px-3 py-1 rounded-full text-xs"
                >
                  {skill}
                </span>
              ))}
            </div>
          </div>
        </div>

        {/* ================= RIGHT SIDE ================= */}
        <div className="lg:col-span-3 space-y-6">

          {/* ABOUT CARD */}
          <div className="bg-gradient-to-r from-teal-500 to-cyan-600 rounded-2xl p-6 text-white shadow-md">
            <h2 className="text-lg font-semibold mb-2">About Me</h2>
            <p className="text-sm opacity-90">
              I am a developer with {candidate.experience} years of experience.
              Passionate about building scalable apps, solving real-world
              problems, and continuously learning new technologies.
            </p>
          </div>

          {/* ================= STATS ================= */}
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">

            <div className="bg-gradient-to-br from-green-500/80 to-emerald-600/80 backdrop-blur rounded-xl p-4 shadow-lg text-white">
              <p className="text-sm">Response Rate</p>
              <p className="text-2xl font-bold">
                {(candidate.response_rate * 100).toFixed(1)}%
              </p>
            </div>

            <div className="bg-gradient-to-br from-blue-500/80 to-cyan-600/80 backdrop-blur rounded-xl p-4 shadow-lg text-white">
              <p className="text-sm">Interview Rate</p>
              <p className="text-2xl font-bold">
                {(candidate.interview_rate * 100).toFixed(1)}%
              </p>
            </div>

            <div className="bg-gradient-to-br from-purple-500/80 to-pink-600/80 backdrop-blur rounded-xl p-4 shadow-lg text-white">
              <p className="text-sm">Profile Score</p>
              <p className="text-2xl font-bold">
                {candidate.profile_completeness}%
              </p>
            </div>

          </div>

          {/* ================= PROJECTS =================
          <div>
            <h2 className="text-lg font-semibold mb-4 text-white">
              Projects
            </h2>

            <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">

              <div className="relative rounded-xl overflow-hidden h-44 group cursor-pointer">
                <img
                  src="https://images.unsplash.com/photo-1501973801540-537f08ccae7b"
                  alt="project"
                  className="w-full h-full object-cover group-hover:scale-110 transition"
                />
                <div className="absolute inset-0 bg-black/40 flex items-end p-3">
                  <p className="text-white font-semibold">Bon Voyage</p>
                </div>
              </div>

              <div className="relative rounded-xl overflow-hidden h-44 group cursor-pointer">
                <img
                  src="https://images.unsplash.com/photo-1497534446932-c925b458314e"
                  alt="project"
                  className="w-full h-full object-cover group-hover:scale-110 transition"
                />
                <div className="absolute inset-0 bg-black/40 flex items-end p-3">
                  <p className="text-white font-semibold">Fresh Job</p>
                </div>
              </div>

              <div className="relative rounded-xl overflow-hidden h-44 group cursor-pointer">
                <img
                  src="https://images.unsplash.com/photo-1513258496099-48168024aec0"
                  alt="project"
                  className="w-full h-full object-cover group-hover:scale-110 transition"
                />
                <div className="absolute inset-0 bg-black/40 flex items-end p-3">
                  <p className="text-white font-semibold">IQR Creator</p>
                </div>
              </div>

            </div>
          </div> */}

          {/* ================= EXTRA INFO ================= */}
          <div className="bg-[#16171d] rounded-2xl p-6 border border-gray-800">
            <h2 className="text-lg font-semibold mb-4 text-white">
              Additional Info
            </h2>

            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">

              {[
                ["Applications", candidate.applications],
                ["Profile Views", candidate.profile_views],
                ["Connections", candidate.connections],
                ["Endorsements", candidate.endorsements],
                ["Search Appearance", candidate.search_appearance],
                ["Saved", candidate.saved_by_recruiters],
                ["Email Verified", candidate.verified_email ? "Yes" : "No"],
                ["Phone Verified", candidate.verified_phone ? "Yes" : "No"],
                ["Relocate", candidate.relocate ? "Yes" : "No"],
                ["Work Mode", candidate.work_mode],
              ].map(([label, value], i) => (
                <div key={i} className="bg-gray-900 rounded-xl p-3">
                  <p className="text-gray-400 text-xs">{label}</p>
                  <p className="text-white font-semibold mt-1">{value}</p>
                </div>
              ))}

            </div>
          </div>

        </div>
      </div>
    </div>
  );
}
