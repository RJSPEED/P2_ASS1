import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [data, setData] = useState({ branches: [] });
  useEffect(() => {
    const fetchData = async () => {
      const result = await axios(
        'https://speedsoftworld.ga/api/branches',
      );
      setData(result.data);
    };
    fetchData();
  }, []);
    
  return (
    <ul>
      <div>
        <h3>Branch List:</h3>
        {data.branches.map(item => (
          <li key={item.objectID}>
            <p> {item.name}, {item.city} </p>
          </li>
        ))}
      </div>
    </ul>
  );
}
export default App;