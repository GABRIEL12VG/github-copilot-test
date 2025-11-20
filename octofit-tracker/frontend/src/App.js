

import './App.css';
import { NavLink, Routes, Route } from 'react-router-dom';
import logo from '../public/octofitapp-small.png';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  return (
    <div className="container">
      <nav className="navbar navbar-expand-lg navbar-dark bg-primary mb-4">
        <NavLink className="navbar-brand text-white d-flex align-items-center" to="/">
          <img src={logo} alt="OctoFit Logo" className="App-logo" />
          OctoFit Tracker
        </NavLink>
        <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav">
            <li className="nav-item"><NavLink className="nav-link text-white" to="/activities">Activities</NavLink></li>
            <li className="nav-item"><NavLink className="nav-link text-white" to="/leaderboard">Leaderboard</NavLink></li>
            <li className="nav-item"><NavLink className="nav-link text-white" to="/teams">Teams</NavLink></li>
            <li className="nav-item"><NavLink className="nav-link text-white" to="/users">Users</NavLink></li>
            <li className="nav-item"><NavLink className="nav-link text-white" to="/workouts">Workouts</NavLink></li>
          </ul>
        </div>
      </nav>
      <div className="card shadow-sm mb-4">
        <div className="card-body">
          <Routes>
            <Route path="/activities" element={<Activities />} />
            <Route path="/leaderboard" element={<Leaderboard />} />
            <Route path="/teams" element={<Teams />} />
            <Route path="/users" element={<Users />} />
            <Route path="/workouts" element={<Workouts />} />
            <Route path="/" element={<h1 className="display-4 text-center">Welcome to OctoFit Tracker!</h1>} />
          </Routes>
        </div>
      </div>
    </div>
  );
}

export default App;
