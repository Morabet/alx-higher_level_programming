#!/usr/bin/node

const argv = require('process').argv;

async function getCompleted (url) {
  const request = new Request(url);
  const response = await fetch(request);

  const tasks = await response.json();
  const completed = tasks.filter(task => task.completed === true);
  const users = [...new Set(completed.map(task => task.userId))];
  const obj = {};
  for (const user of users) {
    const count = completed.filter(com => com.userId === user).length;
    obj[user] = count;
  }
  console.log(obj);
}

if (argv.length >= 3) {
  getCompleted(argv[2]);
}
