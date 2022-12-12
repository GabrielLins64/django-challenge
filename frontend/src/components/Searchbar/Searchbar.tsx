import { faMagnifyingGlass } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import "./Searchbar.css";

function Searchbar() {
  return (
    <div className="search-bar-container">
      <div className="input-group search-bar">
        <input
          type="text"
          className="form-control"
          placeholder="Pesquisar"
        />
        <button className="btn btn-secondary">
          <FontAwesomeIcon
            icon={faMagnifyingGlass}
            className="form-control-feedback"
          />
          &ensp;Buscar
        </button>
      </div>
    </div>
  );
}

export default Searchbar;
