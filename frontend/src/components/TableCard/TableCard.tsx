import { faArrowsRotate, faPlus } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import React from "react";
import { Button, Pagination, Table } from "react-bootstrap";
import Searchbar from "../Searchbar/Searchbar";
import "./TableCard.css";

type Column = {
  name: string;
  key: string;
  type?: string;
};

interface TableCardProps {
  columns?: Array<Column>;
  data?: Array<any>;
  totalDataCount?: number;
  currentPage?: number;
  setPage?: React.Dispatch<React.SetStateAction<number>>;
  hasInsertBtn?: boolean;
  insertAction?: () => void;
  refreshCallback?: () => void;
}

const pageSize = 50;

function TableCard({
  columns = [],
  data = [],
  totalDataCount = 0,
  currentPage = 1,
  hasInsertBtn = false,
  setPage = () => {},
  insertAction = () => {},
  refreshCallback = () => {},
}: TableCardProps) {
  const rows = data.map((row, index) => {
    return (
      <tr key={index}>
        {columns.map((column, index2) => {
          if (column?.type === "bool")
            return <td key={index2}>{row[column.key] ? "Sim" : "Não"}</td>;
          else return <td key={index2}>{row[column.key]}</td>;
        })}
      </tr>
    );
  });

  const hasNextPage = (): boolean => {
    return totalDataCount > pageSize * currentPage;
  };

  const handlePaginateNext = () => {
    setPage(currentPage + 1);
  };

  const handlePaginatePrevious = () => {
    setPage(currentPage - 1);
  };

  const handlePaginateFirst = () => {
    setPage(1);
  };

  const handlePaginateLast = () => {
    let lastPage = Math.ceil(totalDataCount / pageSize);
    setPage(lastPage);
  };

  return (
    <div className="table-card-container">
      <div className="table-card">
        <div className="table-card-header">
          <Searchbar />

          <div className="table-card-header-right-controls">
            <Button onClick={refreshCallback} variant="outline-secondary">
              <FontAwesomeIcon icon={faArrowsRotate} />
              &ensp;Atualizar
            </Button>
            {hasInsertBtn && (
              <button
                onClick={insertAction}
                className="btn btn-outline-secondary insert-btn"
              >
                <FontAwesomeIcon icon={faPlus} />
                &ensp;Inserir
              </button>
            )}
          </div>
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
              <Pagination.First
                onClick={handlePaginateFirst}
                disabled={currentPage === 1}
              />
              <Pagination.Prev
                onClick={handlePaginatePrevious}
                disabled={currentPage === 1}
              />
              {currentPage > 1 && (
                <Pagination.Item onClick={handlePaginatePrevious}>
                  {currentPage - 1}
                </Pagination.Item>
              )}
              <Pagination.Item active>{currentPage}</Pagination.Item>
              {hasNextPage() && (
                <Pagination.Item onClick={handlePaginateNext}>
                  {currentPage + 1}
                </Pagination.Item>
              )}
              <Pagination.Next
                onClick={handlePaginateNext}
                disabled={!hasNextPage()}
              />
              <Pagination.Last
                onClick={handlePaginateLast}
                disabled={!hasNextPage()}
              />
            </Pagination>
          </div>
        </div>
      </div>
    </div>
  );
}

export default TableCard;
