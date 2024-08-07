#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error('Request failed:', error);
    return;
  }

  try {
    const todos = JSON.parse(body);
    const completed = {};

    todos.forEach((todo) => {
      if (todo.completed) {
        if (completed[todo.userId] === undefined) {
          completed[todo.userId] = 1;
        } else {
          completed[todo.userId] += 1;
        }
      }
    });

    console.log(completed);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
