import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Ativacao({ emailPreenchido }) {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    email: emailPreenchido || '',
    code: ''
  });

  const [errors, setErrors] = useState({});
  const [isLoading, setIsLoading] = useState(false);
  const [successMessage, setSuccessMessage] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const validateForm = () => {
    const newErrors = {};
    if (!formData.email) newErrors.email = 'Email é obrigatório';
    if (!formData.code) newErrors.code = 'Código é obrigatório';
    
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
      const response = await fetch('http://127.0.0.1:5000/ativar', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: formData.email,
          code: formData.code
        })
      });

      const data = await response.json();
      
      if (!response.ok) {
        throw new Error(data.message || 'Erro ao ativar usuário');
      }

      setSuccessMessage('Ativação realizada com sucesso!');
      console.log('Sucesso:', data);
      
      // Redirecionamento imediato e garantido
      navigate('/login', { replace: true });

    } catch (error) {
      console.error('Erro:', error);
      setErrors({ submit: error.message });
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div style={{ padding: '20px', maxWidth: '400px', margin: '0 auto' }}>
      <h1>Ativação de Usuário</h1>
      {successMessage && (
        <div style={{ color: 'green', marginBottom: '10px' }}>
          {successMessage}
        </div>
      )}
      {errors.submit && (
        <div style={{ color: 'red', marginBottom: '10px' }}>
          {errors.submit}
        </div>
      )}
      
      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: '10px' }}>
          <label>Email:</label>
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            style={{ width: '100%', padding: '8px' }}
            disabled={!!emailPreenchido}
          />
          {errors.email && <span style={{ color: 'red' }}>{errors.email}</span>}
        </div>
  
        <div style={{ marginBottom: '10px' }}>
          <label>Código de Ativação:</label>
          <input
            type="text"
            name="code"
            value={formData.code}
            onChange={handleChange}
            style={{ width: '100%', padding: '8px' }}
          />
          {errors.code && <span style={{ color: 'red' }}>{errors.code}</span>}
        </div>
  
        <button 
          type="submit" 
          style={{ padding: '10px', width: '100%', background: 'blue', color: 'white' }}
          disabled={isLoading}
        >
          {isLoading ? 'Ativando...' : 'Ativar'}
        </button>
      </form>
    </div>
  );
}

export default Ativacao;