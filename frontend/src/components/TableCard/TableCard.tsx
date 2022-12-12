import { faPlus } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { Pagination, Table } from "react-bootstrap";
import Searchbar from "../Searchbar/Searchbar";
import "./TableCard.css";

type Column = {
  name: string;
  key: string;
};

interface TableCardProps {
  columns?: Array<Column>;
  data?: Array<any>;
  totalDataCount?: number;
  currentPage?: number;
  nextPage?: string | null;
  previousPage?: string | null;
}

function TableCard({
  columns = [],
  data = [],
  totalDataCount = 0,
  currentPage = 1,
  nextPage = null,
  previousPage = null,
}: TableCardProps) {
  const rows = data.map((row, index) => {
    return (
      <tr key={index}>
        {columns.map((column, index2) => {
          return <td key={index2}>{row[column.key]}</td>;
        })}
      </tr>
    );
  });

  return (
    <div className="table-card-container">
      <div className="table-card">
        <div className="table-card-header">
          <Searchbar />

          <button className="btn btn-outline-secondary insert-btn">
            <FontAwesomeIcon icon={faPlus} />
            &ensp;Inserir
          </button>
        </div>

        <div className="table-card-box">
          <Table responsive className="table">
            <thead className="table-head">
              <tr>
                {columns.map((column, index) => (
                  <th key={index}>{column.name}</th>
                ))}
              </tr>
            </thead>

            <tbody>{rows}</tbody>
          </Table>
        </div>

        <div className="table-footer">
          <p>Mostrando {`${data.length} de ${totalDataCount}`} resultados</p>
          <div className="table-pagination">
            <Pagination>
              <Pagination.First disabled={currentPage === 1} />
              <Pagination.Prev disabled={currentPage === 1} />
              {previousPage && (
                <Pagination.Item>{currentPage - 1}</Pagination.Item>
              )}
              <Pagination.Item active>{currentPage}</Pagination.Item>
              {nextPage && (
                <Pagination.Item>{currentPage + 1}</Pagination.Item>
              )}
              <Pagination.Next disabled={nextPage === null} />
              <Pagination.Last disabled={nextPage === null} />
            </Pagination>
          </div>
        </div>
      </div>
    </div>
  );
}

export default TableCard;
