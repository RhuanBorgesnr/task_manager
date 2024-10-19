import React, { useState, useEffect } from "react";
import "./TaskList.css";
import axios from "../utils/axios";
import { FaTrash } from 'react-icons/fa';
interface Task {
  id: number;
  user: number;
  created_at: string;
  description: string;
  username: string;
}

const formatDateToBR = (dateString: string): string => {
  const date = new Date(dateString);
  const day = date.getUTCDate().toString().padStart(2, "0");
  const month = (date.getUTCMonth() + 1).toString().padStart(2, "0");
  const year = date.getUTCFullYear();
  return `${day}/${month}/${year}`;
};

const TaskList: React.FC = () => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [description, setDescription] = useState("");

  useEffect(() => {
    axios
      .get("tasks/")
      .then((response) => setTasks(response.data))
      .catch((error) => console.error(error));
  }, []);

  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    axios
      .post("tasks/", {
        description,
      })
      .then((response) => {
        setTasks([...tasks, response.data]);
        setDescription("");
      })
      .catch((error) => console.error(error));
  };

  const handleDelete = (taskId: number) => {
    axios
      .delete(`tasks/${taskId}/`)
      .then(() => {
        setTasks(tasks.filter((task) => task.id !== taskId));
      })
      .catch((error) => console.error(error));
  };
  return (
    <div className="task-list-container">
      <h1>Lista de Tarefas</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          placeholder="Descrição da tarefa"
          required
        />

        <button type="submit">Cadastrar Tarefa</button>
      </form>
      <div className="task-list-header">
        <span className="task-description-header">Descrição</span>
        <span className="task-created-at-header">Criado em</span>
        <span className="task-username-header">Usuário</span>
      </div>
      <ul className="task-list">
        {tasks.map((task) => (
          <li key={task.id} className="task-item">
            <span className="task-description">{task.description}</span>
            <span className="task-created-at">
              {formatDateToBR(task.created_at)}
            </span>
            <span className="task-username">{task.username}</span>
            <button
              className="delete-button"
              onClick={() => handleDelete(task.id)}
            >
              <FaTrash /> 
            </button>
          </li>
          
        ))}
      </ul>
    </div>
  );
};

export default TaskList;
