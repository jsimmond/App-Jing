import { useContext, useEffect, useRef, useState } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import axios from "axios";

// import styles from "./Matches.module.css";
import SidebarPage from "pages/wrapper/SidebarPage";
import LoadingOverlay from "components/loading/LoadingOverlay";
import { EventContext } from "contexts/EventContext";
import { useIsFirstRender, usePrevious } from "utils/hooks";
import { capitalize, objectToParamsString, paramsStringToObject } from "utils";
import TablePagination from "components/pagination/TablePagination";

export default function TableSearchPage({
  SidebarComponent,
  TableComponent,
  apiUrl,
  label,
}) {
  const { event, setEvent } = useContext(EventContext);
  const [filters, setFilters] = useState({});
  const [rows, setRows] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [alreadyChanged, setAlreadyChanged] = useState(false);
  const location = useLocation();
  const navigate = useNavigate();

  const [currentPage, setCurrentPage] = useState(1);
  const prevPage = usePrevious(currentPage);
  const [pageSize, setPageSize] = useState(10);
  const [totalCount, setTotalCount] = useState(0);

  const rootRef = useRef();
  const abortControllerRef = useRef(new AbortController());
  const pathnameRef = useRef(location.pathname);
  const keepLoading = useRef(false);

  useEffect(() => {
    return () => {
      abortControllerRef.current.abort();
      setIsLoading(false);
    };
  }, []);

  useEffect(() => {
    if (!event || location.pathname !== pathnameRef.current) return;

    // Load filters from URL
    if (alreadyChanged) {
      setAlreadyChanged(false);
    } else {
      const params = paramsStringToObject(location.search);
      const { event: eventParam, page: pageParam, ...filtersParam } = params;
      if (eventParam === undefined || pageParam === undefined) {
        params.event = eventParam ?? event.id;
        params.page = pageParam ?? 1;
        navigate("?" + objectToParamsString(params), { replace: true });
        return;
      }
      if (eventParam !== event.id) setEvent(eventParam);
      setCurrentPage(pageParam);
      setFilters(filtersParam);
      setAlreadyChanged(true);
    }

    //// Fetch:
    // Abort previous request
    abortControllerRef.current.abort();
    abortControllerRef.current = new AbortController();
    // Prevent previous request from setting loading off when canceled
    if (isLoading) keepLoading.current = true;
    setIsLoading(true);
    axios
      .get(`http://localhost:8000${apiUrl}${location.search}`, {
        signal: abortControllerRef.current.signal,
      })
      .then((response) => {
        setRows(response.data.results);
        setTotalCount(response.data.count);
        rootRef.current.scrollTo(0, 0);
      })
      .finally(() => {
        if (!keepLoading.current) {
          setIsLoading(false);
        }
        keepLoading.current = false;
      })
      .catch((error) => {
        if (axios.isCancel(error)) {
          // do nothing
        } else {
          throw error;
        }
      });
  }, [location]);

  useEffect(() => {
    if (!event || isFirstRender) return;
    if (alreadyChanged) {
      setAlreadyChanged(false);
    } else {
      const searchFilters = { event: event.id, ...filters, page: currentPage };
      console.log(currentPage, prevPage);
      if (currentPage !== 1 && prevPage === currentPage) {
        setCurrentPage(1);
        return;
      }
      navigate("?" + objectToParamsString(searchFilters));
      setAlreadyChanged(true);
    }
  }, [event, currentPage, filters]);

  const paginationEl = (
    <TablePagination
      current={currentPage}
      size={pageSize}
      count={totalCount}
      setCurrent={setCurrentPage}
      className="justify-content-center"
    />
  );

  return (
    <SidebarPage
      sidebar={<SidebarComponent filters={filters} setFilters={setFilters} />}
      rootRef={rootRef}
    >
      <h1>{capitalize(label)}</h1>
      <h4>{event?.name}</h4>
      {isLoading && <LoadingOverlay />}

      {rows.length > 0 ? (
        <>
          {paginationEl}
          <TableComponent rows={rows} />
          {paginationEl}
        </>
      ) : (
        <p className="text-center lead">
          No se encontraron {label} con los criterios seleccionados
        </p>
      )}

      {event === undefined && (
        <p className="text-center lead">No se ha seleccionado un evento</p>
      )}
    </SidebarPage>
  );
}
