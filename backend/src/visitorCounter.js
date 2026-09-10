const fs = require('fs');
const path = require('path');

const counterFile = path.join(__dirname, 'visitors.json');

function getCount() {
  if (!fs.existsSync(counterFile)) {
    fs.writeFileSync(counterFile, JSON.stringify({ count: 0 }));
  }
  const data = fs.readFileSync(counterFile);
  return JSON.parse(data).count;
}

function incrementCount() {
  const count = getCount() + 1;
  fs.writeFileSync(counterFile, JSON.stringify({ count }));
  console.log(`👀 Portfolio visited! Total visits: ${count}`);
  return count;
}

module.exports = { incrementCount };