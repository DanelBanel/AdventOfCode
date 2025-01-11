const fs = require('fs');

if (process.argv.length < 3) {
    console.error('Usage: node solution.js <input_file>');
    process.exit(1);
}

const inputFile = process.argv[2];

fs.readFile(inputFile, 'utf8', (err, data) => {
    if (err) {
        console.error(`Error reading file: ${err.message}`);
        process.exit(1);
    }
    console.log(data);
    // Process the file content

});