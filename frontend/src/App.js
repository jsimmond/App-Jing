import styles from "./App.module.css";
import { useState } from "react";
import {
  Routes,
  Route,
  Navigate,
  useLocation
} from "react-router-dom";

import { TransitionGroup, CSSTransition } from "react-transition-group";
import { Provider as AlertProvider } from 'react-alert'

import { API_URL } from "constants";
import NavBar from "components/navbar/NavBar";
import { EventContext } from "contexts/EventContext";

import News from 'pages/News';
import Messages from 'pages/Messages';
import Matches from 'pages/Matches';
import Teams from 'pages/Teams';
import Admin from 'pages/Admin';
import Persons from "pages/Persons";
import Results from "pages/Results";
import Events from "pages/Events";
import axios from "axios";
import Maps from "pages/Maps";
import Alert from "components/alert/Alert";

function App() {
  const [event, _setEvent] = useState({ id: 5, name: "JING 2022" });
  const location = useLocation();

  function setEvent(event) {
    if (Number.isInteger(event)) {
      axios
        .get(`${API_URL}/events/${event}/`)
        .then((response) => {
          const res = response.data;
          _setEvent({ id: res.id, name: res.name });
        })
    }
    else if (typeof event === 'object' && event.hasOwnProperty('id') && event.hasOwnProperty('name')) {
      _setEvent(event);
    }
    else { _setEvent(null); }
  }

  return (
    <EventContext.Provider value={{ event, setEvent }}>
      <AlertProvider template={Alert} timeout={10000} position="bottom center">
        <div className={styles.root}>
          <NavBar />
          <TransitionGroup component={null} exit={false}>
            <CSSTransition key={location.pathname} classNames="fade" timeout={0}>
              <Routes location={location}>
                <Route index element={<News />} />
                <Route path="personas" element={<Persons />} />
                <Route path="partidos" element={<Matches />} />
                <Route path="equipos" element={<Teams />} />
                <Route path="mensajes" element={<Messages />} />
                <Route path="administracion" element={<Admin />} />
                <Route path="resultados" element={<Results />} />
                <Route path="eventos" element={<Events />} />
                <Route path="mapa" element={<Maps />} />

                <Route path="/hola" element={<Teams />} />
                <Route path="*" element={<Navigate to="/" replace={true} />} />
              </Routes>
            </CSSTransition>
          </TransitionGroup>
        </div>
      </AlertProvider>
    </EventContext.Provider>
  );
}

export default App;
