import React from 'react';

const PeopleCount = ({ count }) => {
  return (
    <div className="people-count">
      <p>People in the room: <span>{count}</span></p>
    </div>
  );
};

export default PeopleCount;
