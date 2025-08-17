import React, { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5000/api/messages")
      .then(res => setMessages(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h1>Messages from Flask API</h1>
      <ul>
        {messages.map(m => <li key={m[0]}>{m[1]}</li>)}
      </ul>
    </div>
  );
}

export default App;
