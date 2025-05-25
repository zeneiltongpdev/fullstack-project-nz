import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // Importe o useNavigate
import Ativacao from './Ativar';

function Cadastrar() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: '',
    cnpj: '',
    phone: ''
  });

  const [errors, setErrors] = useState({});
  const [isLoading, setIsLoading] = useState(false);
  const [successMessage, setSuccessMessage] = useState('');
  const [showAtivacao, setShowAtivacao] = useState(false); // Novo estado para controlar a exibição

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const validateForm = () => {
    const newErrors = {};
    if (!formData.name) newErrors.name = 'Nome é obrigatório';
    if (!formData.email) newErrors.email = 'Email é obrigatório';
    if (!formData.password) newErrors.password = 'Senha é obrigatória';
    else if (formData.password.length < 6) newErrors.password = 'Senha deve ter no mínimo 6 caracteres';
    if (!formData.cnpj) newErrors.cnpj = 'CNPJ é obrigatório';
    if (!formData.phone) newErrors.phone = 'Telefone é obrigatório';
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    if (!validateForm()) {
      return;
    }

    setIsLoading(true);
    
    try {
      const response = await fetch('http://127.0.0.1:5000/user', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          name: formData.name,
          email: formData.email,
          cnpj: formData.cnpj,
          password: formData.password,
          phone: formData.phone
        })
      });

      if (!response.ok) {
        throw new Error('Erro ao cadastrar usuário');
      }

      const data = await response.json();
      setSuccessMessage('Cadastro realizado com sucesso! Aguarde a ativação.');
      setShowAtivacao(true); // Mostra o formulário de ativação
      console.log('Sucesso:', data);

    } catch (error) {
      console.error('Erro:', error);
      setErrors({ submit: 'Erro ao enviar cadastro. Por favor, tente novamente.' });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div style={{ padding: '20px', maxWidth: '400px', margin: '0 auto' }}>
      {!showAtivacao ? (
        <>
          <h1>Cadastro de Usuário</h1>
          {successMessage && <div style={{ color: 'green', marginBottom: '10px' }}>{successMessage}</div>}
          {errors.submit && <div style={{ color: 'red', marginBottom: '10px' }}>{errors.submit}</div>}
          
          <form onSubmit={handleSubmit}>
            <div style={{ marginBottom: '10px' }}>
              <label>Name :</label>
              <input
                type="text"
                name="name"
                value={formData.name}
                onChange={handleChange}
                style={{ width: '100%', padding: '8px' }}
              />
              {errors.name && <span style={{ color: 'red' }}>{errors.name}</span>}
            </div>

            <div style={{ marginBottom: '10px' }}>
              <label>Email:</label>
              <input
                type="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                style={{ width: '100%', padding: '8px' }}
              />
              {errors.email && <span style={{ color: 'red' }}>{errors.email}</span>}
            </div>

            <div style={{ marginBottom: '10px' }}>
              <label>Senha:</label>
              <input
                type="password"
                name="password"
                value={formData.password}
                onChange={handleChange}
                style={{ width: '100%', padding: '8px' }}
              />
              {errors.password && <span style={{ color: 'red' }}>{errors.password}</span>}
            </div>

            <div style={{ marginBottom: '10px' }}>
              <label>CNPJ:</label>
              <input
                type="text"
                name="cnpj"
                value={formData.cnpj}
                onChange={handleChange}
                style={{ width: '100%', padding: '8px' }}
              />
              {errors.cnpj && <span style={{ color: 'red' }}>{errors.cnpj}</span>}
            </div>

            <div style={{ marginBottom: '10px' }}>
              <label>Telefone:</label>
              <input
                type="text"
                name="phone"
                value={formData.phone}
                onChange={handleChange}
                style={{ width: '100%', padding: '8px' }}
              />
              {errors.phone && <span style={{ color: 'red' }}>{errors.phone}</span>}
            </div>

            <button 
              type="submit" 
              style={{ padding: '10px', width: '100%', background: 'blue', color: 'white' }}
              disabled={isLoading}
            >
              {isLoading ? 'Enviando...' : 'Cadastrar'}
            </button>
          </form>

          <button 
            onClick={() => navigate('/login')} // Use navigate para redirecionar
            style={{ 
              marginTop: '10px',
              padding: '10px', 
              width: '100%', 
              background: 'gray', 
              color: 'white',
              border: 'none'
            }}
          >
            Já tem conta? Faça Login
          </button>

        </>
      ) : (
        <Ativacao emailPreenchido={formData.email} />
      )}
    </div>
  );
}

export default Cadastrar;