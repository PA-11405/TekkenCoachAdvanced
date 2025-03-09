import React from 'react';
import { List, ListItem, ListItemText, Paper } from '@mui/material';

const MoveList = ({ moves, onSelect }) => {
  return (
    <Paper elevation={3} style={{ marginBottom: '20px' }}>
      <List>
        {moves.map((move, index) => (
          <ListItem button key={index} onClick={() => onSelect(move)}>
            <ListItemText primary={move} />
          </ListItem>
        ))}
      </List>
    </Paper>
  );
};

export default MoveList;
