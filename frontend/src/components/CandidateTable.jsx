import { useNavigate } from "react-router-dom";

export default function CandidateTable({
  candidates
}) {

  const navigate = useNavigate();

return (
  <div className="overflow-x-auto bg-white rounded-2xl shadow-md border border-gray-100">
    <table className="w-full text-left border-collapse">

      {/* Header */}
      <thead className="bg-gray-50 text-gray-700 uppercase text-sm tracking-wider">
        <tr>
          <th className="px-5 py-3">Rank</th>
          <th className="px-5 py-3">Candidate ID</th>
          <th className="px-5 py-3">Score</th>
        </tr>
      </thead>

      {/* Body */}
      <tbody className="text-gray-700">
        {candidates.map((candidate, index) => (
          <tr
            key={candidate.candidate_id}
            className="border-t hover:bg-blue-300 cursor-pointer 
                       transition-all duration-200"
            onClick={() =>
              navigate(`/candidate/${candidate.candidate_id}`)
            }
          >
            <td className="px-5 py-3 font-medium text-gray-900">
              #{index + 1}
            </td>

            <td className="px-5 py-3 font-semibold text-gray-800">
              {candidate.candidate_id}
            </td>

            <td className="px-5 py-3 font-bold text-green-600">
              {candidate.score}
            </td>
          </tr>
        ))}
      </tbody>

    </table>
  </div>
);
}