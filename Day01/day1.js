import * as fs from 'fs';

const arr1 = [];
const arr2 = [];

fs.readFile('Input.txt',(err, data) => {
    //Read file and split into arr1 and arr2
    data = data.toString();
    data = data.split('\r\n');
    data.forEach(line => {
        const [num1, num2] = line.split('   ')
        arr1.push(parseInt(num1));
        arr2.push(parseInt(num2));
    });

    // part1();
    part2();
});

function part1(){
    //Sort arrays
    arr1.sort();
    arr2.sort();
    console.log(arr1);
    console.log(arr2);

    let sum = 0;
    for(let i = 0; i < arr1.length; i++){
        sum += Math.abs(arr1[i] - arr2[i]);
    }
    console.log('There are ', arr1.length, ' entries');
    console.log('The answer is: ', sum);
}

function part2(){
    //Sort array 2
    arr2.sort();

    let sum = 0;
    arr1.forEach(check => {
        let index = arr2.findIndex(x => x === check);
        if(index >= 0)
            do{
                sum += check;
                index++;
            }   while(check === arr2[index]);
    });
    console.log('There are ', arr1.length, ' entries');
    console.log('The answer is: ', sum);
}