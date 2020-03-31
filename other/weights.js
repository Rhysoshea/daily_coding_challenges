function orderWeight(str) {
  if (str === "") return "";
  array = str.split(" ").map(Number).sort();
  console.log(array)
  var unsorted = [], sorted = [], converted = [];
  for (i=0; i<array.length; i++) {
    unsorted[i] = digitSum(array[i]);
  }
  console.log(unsorted)
  sorted = unsorted.concat().sort(function(a, b){return a-b;});
  console.log(sorted)
  for (i=0; i<array.length; i++) {
    converted[i] = array[unsorted.indexOf(sorted[i])];
    delete unsorted[unsorted.indexOf(sorted[i])];
  }
  console.log(converted.join(" "));
}
//
function digitSum(num) {
  var sum = 0;
  while (num > 0) {
    sum += num%10;
    num = Math.floor(num/10);
  }
  return sum;
}
orderWeight("56 65 74 100 180 92 44 13 200")
