import React, { useState, useEffect } from "react";
import axios from "../utils/axios";
import "./TimeRecordList.css";
import { FaTrash } from "react-icons/fa";

interface TimeRecord {
  id: number;
  date: string;
  formatted_hours: number;
  description: string;
  task: number;
  task_description: string;
}

interface Task {
  id: number;
  description: string;
}

const TimeRecordList: React.FC = () => {
  const [timeRecords, setTimeRecords] = useState<TimeRecord[]>([]);
  const [tasks, setTasks] = useState<Task[]>([]);
  const [users, setUser] = useState<any>([]);

  const [filters, setFilters] = useState({
    date: "",
    hours: "",
    description: "",
    taskId: "",
    users: "",
  });
  const [date, setDate] = useState("");
  const [hours, setHours] = useState("");
  const [description, setDescription] = useState("");
  const [taskId, setTaskId] = useState("");
  const [userData, setUserData] = useState<{
    username: string;
    groups: string[];
  } | null>(null);

  console.log(hours);
  useEffect(() => {
    fetchTimeRecords();
    fetchTasks();
    fetchUsers();
  }, [filters]);

  const formatDateToBR = (dateString: string): string => {
    const date = new Date(dateString);
    const day = date.getUTCDate().toString().padStart(2, "0");
    const month = (date.getUTCMonth() + 1).toString().padStart(2, "0");
    const year = date.getUTCFullYear();
    return `${day}/${month}/${year}`;
  };

  const convertTimeToDecimal = (timeString: string) => {
    const [hours, minutes] = timeString.split(":").map(Number);
    return (hours + minutes / 60).toFixed(2);
  };

  useEffect(() => {
    const fetchUserDetails = async () => {
      try {
        const response = await axios.get("/user/");
        setUserData(response.data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchUserDetails();
  }, []);
  const fetchTimeRecords = () => {
    const params = {
      date: filters.date,
      hours: filters.hours,
      description: filters.description,
      task: filters.taskId,
      user: filters.users,
    };
    axios
      .get("time-records/", { params })
      .then((response) => setTimeRecords(response.data))
      .catch((error) => console.error(error));
  };

  const fetchTasks = () => {
    axios
      .get("tasks/")
      .then((response) => setTasks(response.data))
      .catch((error) => console.error(error));
  };
  const fetchUsers = () => {
    axios
      .get("/users/non-admins/")
      .then((response) => setUser(response.data))
      .catch((error) => console.error(error));
  };

  const handleDelete = (timeId: number) => {
    axios
      .delete(`time-records/${timeId}/`)
      .then(() => {
        setTimeRecords(
          timeRecords.filter((timeRecord) => timeRecord.id !== timeId)
        );
      })
      .catch((error) => console.error(error));
  };

  const handleSubmit = (event: React.FormEvent) => {
    const decimalHours = convertTimeToDecimal(hours);

    event.preventDefault();
    axios
      .post("time-records/", {
        date,
        hours: decimalHours,
        description,
        task: taskId,
      })
      .then((response) => {
        setTimeRecords([...timeRecords, response.data]);
        setDate("");
        setHours("");
        setDescription("");
        setTaskId("");
      })
      .catch((error) => console.error(error));
  };

  const handleFilterChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>
  ) => {
    const { name, value } = e.target;
    setFilters({ ...filters, [name]: value });
  };
  const isAdmin = userData?.groups.includes("Administrador");

  return (
    <div className="time-record-list-container">
      <h1>Registros de Tempo</h1>
      {!isAdmin && (
        <form onSubmit={handleSubmit}>
          <input
            type="date"
            value={date}
            onChange={(e) => setDate(e.target.value)}
            placeholder="Data"
            required
          />
          <input
            type="time"
            value={hours}
            onChange={(e) => setHours(e.target.value)}
            placeholder="Horas"
            required
          />
          <input
            type="text"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            placeholder="Descrição"
            required
          />
          <select
            value={taskId}
            onChange={(e) => setTaskId(e.target.value)}
            required
          >
            <option value="">Selecione Tarefa</option>
            {tasks.map((task) => (
              <option key={task.id} value={task.id}>
                {task.description}
              </option>
            ))}
          </select>
          <button type="submit">Registrar Tempo</button>
        </form>
      )}

      <h2>Filtrar Registros de Tempo</h2>
      <div className="filter-container">
        <input
          type="date"
          name="date"
          value={filters.date}
          onChange={handleFilterChange}
        />
        <input
          type="number"
          name="hours"
          value={filters.hours}
          onChange={handleFilterChange}
          placeholder="Horas"
        />
        <input
          type="text"
          name="description"
          value={filters.description}
          onChange={handleFilterChange}
          placeholder="Descrição"
        />
        <select
          name="taskId"
          value={filters.taskId}
          onChange={handleFilterChange}
        >
          <option value="">Tarefa</option>
          {tasks.map((task) => (
            <option key={task.id} value={task.id}>
              {task.description}
            </option>
          ))}
        </select>
        {isAdmin && (
          <select
            name="users"
            value={filters.users}
            onChange={handleFilterChange}
          >
            <option value="">Usuário</option>
            {users.map((user: any) => (
              <option key={user.id} value={user.id}>
                {user.username}
              </option>
            ))}
          </select>
        )}
      </div>

      <div className="time-record-list-header">
        <span className="time-record-date-header">Data</span>
        <span className="time-record-hours-header">Horas</span>
        <span className="time-record-description-header">Descrição</span>
        <span className="time-record-task-header">Tarefa</span>
      </div>
      <ul className="time-record-list">
        {timeRecords.map((record) => (
          <li key={record.id} className="time-record-item">
            <span className="time-record-date">
              {formatDateToBR(record.date)}
            </span>
            <span className="time-record-hours">{record.formatted_hours}</span>
            <span className="time-record-description">
              {record.description}
            </span>
            <span className="time-record-task">{record.task_description}</span>
            <button
              className="delete-button"
              onClick={() => handleDelete(record.id)}
            >
              <FaTrash />
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TimeRecordList;
