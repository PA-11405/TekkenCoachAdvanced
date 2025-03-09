// src/components/MoveDetail.js
import React from 'react';
import { Card, CardContent, Typography, CardMedia, List, ListItem, ListItemText } from '@mui/material';

const MoveDetail = ({ move }) => {
  return (
    <Card style={{ marginTop: '20px' }}>
      {move.image_url ? (
        <CardMedia
          component="img"
          style={{ width: '150px', height: '150px', objectFit: 'contain', margin: 'auto' }}
          image={move.image_url}
          alt={move.character}
        />
      ) : null}
      <CardContent>
        <Typography variant="h5">{move.move_name}</Typography>
        <Typography variant="subtitle1">Character: {move.character}</Typography>
        <Typography variant="body2">
          Frame Data: Startup: {move.frame_data.startup}, Block: {move.frame_data.block}, Hit: {move.frame_data.hit}, Counter Hit: {move.frame_data.counter_hit}
        </Typography>
        <Typography variant="h6" style={{ marginTop: '10px' }}>Common Issues</Typography>
        <List dense>
          {move.common_issues.map((issue, index) => (
            <ListItem key={index}>
              <ListItemText primary={issue} />
            </ListItem>
          ))}
        </List>
        <Typography variant="h6" style={{ marginTop: '10px' }}>Best Counters</Typography>
        <List dense>
          {move.best_counters.map((counter, index) => (
            <ListItem key={index}>
              <ListItemText primary={`${counter.character}: ${counter.counter}`} />
            </ListItem>
          ))}
        </List>
        <Typography variant="h6" style={{ marginTop: '10px' }}>In-Depth Counterplay</Typography>
        <Typography variant="body1">{move.in_depth_counterplay}</Typography>
      </CardContent>
    </Card>
  );
};

export default MoveDetail;
