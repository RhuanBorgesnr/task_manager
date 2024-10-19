// src/App.tsx
import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
  Link,
} from "react-router-dom";
import { AuthProvider, useAuth } from "./context/AuthContext";
import TaskList from "./components/TaskList";
import TimeRecordList from "./components/TimeRecordList";
import Login from "./components/Login";
import PrivateRoute from "./components/PrivateRoute";
import LogoutButton from "./components/Logout";

const Navigation: React.FC = () => {
  const { isAuthenticated } = useAuth();

  return (
    <div className="navbar-container">
      {isAuthenticated && (
        <>
          <nav className="navbar">
            <ul className="navbar-links">
              <li>
                <Link to="/tasks">Lista de Tarefas</Link>
              </li>
              <li>
                <Link to="/time-records">Registros de Tempo</Link>
              </li>
            </ul>
          </nav>
          <LogoutButton /> {/* Botão fora do <li> */}
        </>
      )}
    </div>
  );
};

const App: React.FC = () => {
  return (
    <AuthProvider>
      <Router>
        <Navigation />
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route
            path="/tasks"
            element={<PrivateRoute element={<TaskList />} />}
          />
          <Route
            path="/time-records"
            element={<PrivateRoute element={<TimeRecordList />} />}
          />
          <Route path="/" element={<Navigate to="/login" />} />
        </Routes>
      </Router>
    </AuthProvider>
  );
};

export default App;
