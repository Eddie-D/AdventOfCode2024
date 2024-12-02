import * as fs from 'fs';

fs.readFile('Input.txt',(err, data) => {
    //Read file and split into arr1 and arr2
    data = data.toString();
    const rows = data.split('\r\n');
    const days = [];
    rows.forEach(line => {
        days.push(line.split(' ').map(x => parseInt(x)));
    });

    // part1(days);
    part2(days);
});

function part1(days){
    let daysSafe = 0;
    days.map(day => isValidDayPart1(day)).forEach((value, index) => {
        console.log('Day ', index + 1, ' is safe: ', value)
        if(value)
            daysSafe++;
    });
    console.log('Days Safe: ', daysSafe);
}

function part2(days){
    let daysSafe = 0;
    days.map(day => isValidDayPart2(day)).forEach((value, index) => {
        console.log('Day ', index + 1, ' is safe: ', value)
        if(value)
            daysSafe++;
    });
    console.log('Days Safe: ', daysSafe);
}

function isValidDayPart2(day){
    // Taking the cowards way out at cost of inefficiency since all the lines are quite short.
    if(isValidDayPart1(day))
        return true;
    for(let i = 0; i < day.length; i++){
        if(isValidDayPart1(day.toSpliced(i,1)))
            return true;
    }
    return false;
}

function isValidDayPart1(day){
    let parity = Math.sign(day[1] - day[0]); //Increasing = 1
    for(let i = 0; i < day.length - 1; i++){
        if(!compareToNext(day[i], day[i + 1], parity))
            return false;
    }
    return true;
}

function compareToNext(first, next, parity){
    const diff = (next - first) * parity;
    return (0 < diff && diff <= 3);
}