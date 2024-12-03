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
    
    const regex = /mul\(\d+,\d+\)/g;
    const matches = data.match(regex);
    console.log(matches);
    total = 0;
    // Extract the numbers from the matches
    for (let i = 0; i < matches.length; i++) {
        const nums = matches[i].match(/\d+/g);
        console.log(nums);
        total += parseInt(nums[0]) * parseInt(nums[1]);
    }
    console.log(total);
});