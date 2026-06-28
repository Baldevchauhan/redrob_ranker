export default function CandidateCard({ candidate, rank }) {
  return (
    <div
      className="bg-white p-5 rounded-2xl shadow-md border border-gray-100 
                  hover:shadow-xl hover:-translate-y-1 transition-all duration-300"
    >
      {/* Rank Badge */}
      <div className="flex justify-between items-center mb-3">
        <h2 className="text-lg font-extrabold text-black">Candidate</h2>
        <span className="bg-blue-100 text-blue-600 text-sm font-bold px-3 py-1 rounded-full">
          #{rank}
        </span>
      </div>

      {/* Divider */}
      <div className="border-t border-gray-100 mb-3"></div>

      {/* Info Section */}
      <div className="space-y-2 text-gray-700">
        <p>
          <span className="font-medium text-gray-500">ID:</span>{" "}
          <span className="font-semibold text-gray-800">
            {candidate.candidate_id}
          </span>
        </p>

        <p>
          <span className="font-medium text-gray-500">Score:</span>{" "}
          <span className="font-bold text-green-600 text-lg">
            {candidate.score}
          </span>
        </p>
      </div>
    </div>
  );
}
