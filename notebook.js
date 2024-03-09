
import React, { useState } from 'react';
import './App.css';

function NoteForm({ addNote }) {
  const [text, setText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!text.trim()) return;
    addNote(text);
    setText('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Add a new note"
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button type="submit">Add Note</button>
    </form>
  );
}

function Note({ note, index, removeNote }) {
  return (
    <div className="note">
      {note}
      <button onClick={() => removeNote(index)}>x</button>
    </div>
  );
}

function App() {
  const [notes, setNotes] = useState([]);

  const addNote = (text) => {
    const newNotes = [...notes, text];
    setNotes(newNotes);
  };

  const removeNote = (index) => {
    const newNotes = [...notes];
    newNotes.splice(index, 1);
    setNotes(newNotes);
  };

  return (
    <div className="app">
      <h1>Notebook</h1>
      <NoteForm addNote={addNote} />
      <div className="notes-list">
        {notes.map((note, index) => (
          <Note key={index} index={index} note={note} removeNote={removeNote} />
        ))}
      </div>
    </div>
  );
}

export default App;
