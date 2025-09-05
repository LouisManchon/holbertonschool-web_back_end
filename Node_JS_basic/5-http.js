// 5-http.js
const http = require('http');
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        return reject(new Error('Cannot load the database'));
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const fields = {};
      let total = 0;

      for (let i = 1; i < lines.length; i += 1) {
        const [firstname, , , field] = lines[i].split(',');
        if (field) {
          if (!fields[field]) fields[field] = [];
          fields[field].push(firstname);
          total += 1;
        }
      }

      let output = `Number of students: ${total}\n`;
      for (const [key, value] of Object.entries(fields)) {
        output += `Number of students in ${key}: ${value.length}. List: ${value.join(', ')}\n`;
      }

      resolve(output.trim());
    });
  });
}

const app = http.createServer((req, res) => {
  const file = process.argv[2];
  const { url } = req;

  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (url === '/') {
    res.end('Hello Holberton School!');
  } else if (url === '/students') {
    countStudents(file)
      .then((data) => res.end(`This is the list of our students\n${data}`))
      .catch(() => res.end('This is the list of our students\nCannot load the database'));
  }
});

app.listen(1245);

module.exports = app;
