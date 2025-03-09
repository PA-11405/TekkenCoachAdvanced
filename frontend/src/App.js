import React, { useState, useEffect } from 'react';
import axios from 'axios';
import MoveList from './components/MoveList';
import MoveDetail from './components/MoveDetail';
import { Container, Typography, Box } from '@mui/material';

function App() {
  const [moves, setMoves] = useState([]);
  const [selectedMove, setSelectedMove] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:8000/moves')
      .then(response => {
        setMoves(response.data.moves);
      })
      .catch(error => console.error(error));
  }, []);

  const handleMoveSelect = (moveName) => {
    axios.get(`http://localhost:8000/move/${encodeURIComponent(moveName)}`)
      .then(response => {
        setSelectedMove(response.data);
      })
      .catch(error => console.error(error));
  };

  return (
    <Container maxWidth="md">
      <Box my={4}>
        <Typography variant="h3" align="center" gutterBottom>
          Tekken Coach
        </Typography>
        <MoveList moves={moves} onSelect={handleMoveSelect} />
        {selectedMove && <MoveDetail move={selectedMove} />}
      </Box>
    </Container>
  );
}

export default App;
