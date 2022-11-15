// var list=[1,2,3,4,5]
// list.reverse()
// console.log(list)
var numbers = [ 1,2,3,4,5];
var reversedNum = [];
for(let i =  numbers.length -1; i >= 0; i--) {
  reversedNum.push(numbers[i]);
  
}
console.log(reversedNum)