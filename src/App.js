import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Cadastrar from './Cadastro';
import Login from './Login';
import Ativacao from './Ativar';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/cadastro" replace />} />
        <Route path="/cadastro" element={<Cadastrar />} />
        <Route path="/login" element={<Login />} />
        <Route path="/ativar" element={<Ativacao />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;