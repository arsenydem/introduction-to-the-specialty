const express = require('express');
const { v4: uuidv4 } = require('uuid');
const path = require('path');

const app = express();
const PORT = 3000;

app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

let tasks = [];

app.get('/api/tasks', (req, res) => {
  const { filter } = req.query;
  let filtered = tasks;

  if (filter === 'active') {
    filtered = tasks.filter(t => !t.completed);
  } else if (filter === 'completed') {
    filtered = tasks.filter(t => t.completed);
  }

  res.json(filtered);
});

app.get('/api/tasks/:id', (req, res) => {
  const task = tasks.find(t => t.id === req.params.id);
  if (!task) {
    return res.status(404).json({ error: 'Задача не найдена' });
  }
  res.json(task);
});

app.post('/api/tasks', (req, res) => {
  const { title, description } = req.body;
  if (!title || typeof title !== 'string' || title.trim() === '') {
    return res.status(400).json({ error: 'Название обязательно' });
  }

  const newTask = {
    id: uuidv4(),
    title: title.trim(),
    description: description || '',
    completed: false,
    createdAt: new Date().toISOString()
  };
  tasks.push(newTask);
  res.status(201).json(newTask);
});

app.put('/api/tasks/:id', (req, res) => {
  const { title, description, completed } = req.body;
  const taskIndex = tasks.findIndex(t => t.id === req.params.id);

  if (taskIndex === -1) {
    return res.status(404).json({ error: 'Задача не найдена' });
  }

  if (!title || typeof title !== 'string' || title.trim() === '') {
    return res.status(400).json({ error: 'Название обязательно' });
  }

  if (typeof completed !== 'boolean') {
    return res.status(400).json({ error: 'Поле completed должно быть boolean' });
  }

  tasks[taskIndex] = {
    ...tasks[taskIndex],
    title: title.trim(),
    description: description || '',
    completed
  };
  res.json(tasks[taskIndex]);
});

app.delete('/api/tasks/:id', (req, res) => {
  const taskIndex = tasks.findIndex(t => t.id === req.params.id);
  if (taskIndex === -1) {
    return res.status(404).json({ error: 'Задача не найдена' });
  }
  tasks.splice(taskIndex, 1);
  res.json({ success: true });
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});