const fs = require('fs');

if (process.argv.length < 3) {
    console.error('Usage: node solution.js <input_file>');
    process.exit(1);
}

const inputFile = process.argv[2];
function addPadding(array, paddingValue, paddingSize) {
    const originalRows = array.length;
    const originalCols = array[0].length;
    const newRows = originalRows + 2 * paddingSize;
    const newCols = originalCols + 2 * paddingSize;

    // Create a new array with the new dimensions and fill it with the padding value
    const paddedArray = Array.from({ length: newRows }, () => Array(newCols).fill(paddingValue));

    // Copy the original array's values into the new array
    for (let i = 0; i < originalRows; i++) {
        for (let j = 0; j < originalCols; j++) {
            paddedArray[i + paddingSize][j + paddingSize] = array[i][j];
        }
    }

    return paddedArray;
}

fs.readFile(inputFile, 'utf8', (err, data) => {
    if (err) {
        console.error(`Error reading file: ${err.message}`);
        process.exit(1);
    }
    console.log(data);
    // Process the file content
    data = data.replace(/[\r]+/g, '');
    data = data.split('\n').map(x => x.split(''));
    // console.log(data[0].length);
    // console.log(data.length);
    // Add padding to the 2D array
    const paddingValue = '-';
    const paddingSize = 2;
    data = addPadding(data, paddingValue, paddingSize);
    console.log(data);
    total = 0;
    for (let i = 2; i < data.length -2; i++) {
        let slice = data.slice(i, i+3)
        // console.log(slice);
        for (let j = 2; j < data[0].length - 2; j++) {
            let square = [slice[0].slice(j, j+3), slice[1].slice(j, j+3), slice[2].slice(j, j+3)];
            // console.log(square);
            // diagonal up right
            if (square[2][0] == "M" && square[1][1] == "A" && square[0][2] == "S") {
                // diagonal down right
                if (square[0][0] == "M" && square[1][1] == "A" && square[2][2] == "S") {
                    total += 1;
                }
                // diagonal up left
                if (square[2][2] == "M" && square[1][1] == "A" && square[0][0] == "S") {
                    total += 1;
                }
            }
            // diagonal down left
            if (square[0][2] == "M" && square[1][1] == "A" && square[2][0] == "S") {
                // diagonal down right
                if (square[0][0] == "M" && square[1][1] == "A" && square[2][2] == "S") {
                    total += 1;
                }
                // diagonal up left
                if (square[2][2] == "M" && square[1][1] == "A" && square[0][0] == "S") {
                    total += 1;
                }
            }            
        }
    }
    console.log(total);
    
    
});
