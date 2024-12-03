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
    
    const regex_mul = /mul\(([0-9]+),([0-9]+)\)/g;
    const regex_do = /do\(\)/;
    const regex_dont = /don't\(\)/;
    const matches = [];
    total = 0;

    left_p = 0;
    reading = true;
    for (right_p = 0; right_p < data.length; right_p++) {
        if (data.substring(left_p, right_p).match(regex_dont)) {
            left_p = right_p;
            reading = false;
            continue;
        }
        else if (data.substring(left_p, right_p).match(regex_do)) {
            left_p = right_p;
            reading = true;
            continue;
        }
        else if (data.substring(left_p, right_p).match(regex_mul) && reading) {
            console.log(data.substring(left_p, right_p).match(regex_mul));
            matches.push(data.substring(left_p, right_p)
                        .match(regex_mul)[0]);
            left_p = right_p;
        }

        
    }
    console.log(matches);
    // Extract the numbers from the matches
    for (let i = 0; i < matches.length; i++) {
        const nums = matches[i].match(/\d+/g);
        console.log(nums);
        total += parseInt(nums[0]) * parseInt(nums[1]);
    }
    console.log(total);
});
