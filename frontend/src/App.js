import './App.css';

import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';


import MainPage from './Pages/MainPage';
import TaskPage from './Pages/TasksPage';

function App() {
  return (
    <>
    <Router>
      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="/tasks" element={<TaskPage />} />
      </Routes>
    </Router>
    </>
  );
}
export default App;
