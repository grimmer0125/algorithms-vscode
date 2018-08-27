/**
 *  input a nail array (A) and use a hammer to drill k times to
 *  return the maximal number of same height of nails.
 *  A is consistent of non-decreasing integral. k >=0
 */
function solution(A, K) {
  const n = A.length;
  let best = 1; // FIXME: maybe 0 if A is empty
  let count = 1;
  for (let i = 0; i < n - 1; i++) {
    if (A[i] == A[i + 1]) {
      count += 1; // when i =0, if [1,1,3], count = 1.
    } else {
      count = 0;
    }

    // if (((n - 1) - i) > K) {
    //   console.log('debug1');
    // } else {
    //   console.log('debug2');
    // }
    const remaining = (((n - 1) - i) > K ? K : ((n - 1) - i));

    if ((count + remaining + 1) > best) {
      best = count + remaining + 1;
    }
  }

  return best;
}

const a = [1, 1, 3, 3, 3, 4, 5, 5, 5, 5];

const answer = solution(a, 2);
console.log(answer);
console.log('end');
