// the “K complementary pairs in array” challenge
// target: worst case time complexity: O(N*logN), space: O(N*logN)

// worst time O(n * n) on Node.js, O(nlogn), space: O(n)
function solution(K, A) {
  let complementaryTotal = 0;

  // 1. sort it first,
  // e.g. sort(): mozilla uses merge sort, time O(nlog(n)), and space O(n)
  // Node's uses quick sort's whose time worst case is O(n^2)?
  // Using Python may be better to have a consitent result O(nlogn)
  A.sort();

  const count = A.length;
  // 2 find. time O(n * logn)
  for (let i = 0; i < count; i++) {
    const targetValue = K - A[i];
    const firstMatch = A.indexOf(targetValue);
    const finalMatch = A.lastIndexOf(targetValue);

    if (firstMatch > -1) {
      complementaryTotal += finalMatch - firstMatch + 1;
    }
  }

  return complementaryTotal;
}


const A = [1, 8, -3, 0, 1, 3, -2, 4, 5];
const resp = solution(6, A);
console.log(resp); // 7

// worst time O(n * n), avg O(n * 1);  space: O(n)
function solution2(K, A) {
  let complementaryTotal = 0;

  const count = A.length;
  const numberTable = {};

  // 1. put in a look-up table: // worst time O(n * n), avg:O(1); space: O(n)
  for (let i = 0; i < count; i++) {
    // worst: time O(n), average:O(1);  space: O(n)
    if (!numberTable[i.toString()]) {
      numberTable[i.toString()] = [];
    }
    numberTable[i.toString()].push(i);
  }

  // 3 find. time O(n * n)
  for (let i = 0; i < count; i++) {
    const targetValue = K - A[i];
    if (numberTable[targetValue.toString()]) {
      complementaryTotal += numberTable[targetValue.toString()].length;
    }
  }

  return complementaryTotal;
}
