export default function SearchBar({ searchTerm, setSearchTerm }) {
  return (
    <input
      type="text"
      placeholder="Search Candidate ID..."
      value={searchTerm}
      onChange={(e) => setSearchTerm(e.target.value)}
      className="w-full px-4 py-2.5 rounded-xl 
           border-none 
           bg-gray-50 text-gray-800 placeholder-gray-400
           focus:outline-none focus:ring-0 focus:border-none
           shadow-sm transition-all duration-200"
    />
  );
}
