const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        return reject(new Error('Cannot load the database'));
      }

      const content = data.split('\n').filter((line) => line.trim() !== '');
      const fields = {};
      let total = 0;

      for (let i = 1; i < content.length; i += 1) {
        const [firstname, , , field] = content[i].split(',');

        if (field) {
          if (!fields[field]) {
            fields[field] = [];
          }
          fields[field].push(firstname);
          total += 1;
        }
      }

      console.log(`Number of students: ${total}`);
      for (const [key, value] of Object.entries(fields)) {
        console.log(`Number of students in ${key}: ${value.length}. List: ${value.join(', ')}`);
      }

      resolve();
    });
  });
}

module.exports = countStudents;
