import { exportCSV } from "../services/api";

export default function ExportButton() {
  return (
    <button
      onClick={exportCSV}
      className="px-5 py-2.5 bg-blue-600 text-white font-medium rounded-lg 
                 shadow-md hover:bg-blue-700 hover:shadow-lg 
                 focus:outline-none focus:ring-2 focus:ring-blue-400 focus:ring-offset-2 
                 active:scale-95 transition-all duration-200"
    >
      Download CSV
    </button>
  );
}