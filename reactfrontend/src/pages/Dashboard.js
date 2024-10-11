import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

const Dashboard = () => {
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem('accessToken');
    if (!token) {
      navigate('/login');  // Redirect to login if not authenticated
    }
  }, [navigate]);

  return (
    <div>
      <h1>Welcome to the Dfnerijni3rnion3rion3oiashboard!</h1>
    </div>
  );
};

export default Dashboard;
