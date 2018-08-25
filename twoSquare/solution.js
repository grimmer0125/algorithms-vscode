function getIntercet(line1, line2) {
  let intercetLen = 0;

  // line1' rectangle is in the right side
  if (line1[0] <= line2[0]) {
    // line2'range is within line1's range
    if (line1[1] >= line2[1]) {
      intercetLen = line2[1] - line2[0];
    } else {
      intercetLen = line1[1] - line2[0];
      if (intercetLen < 0) {
        intercetLen = 0;
      }
    }
  } else if (line2[1] >= line1[1]) {
    // line1'range is within line2's range
    intercetLen = line1[1] - line1[0];
  } else {
    intercetLen = line2[1] - line1[0];
    if (intercetLen < 0) {
      intercetLen = 0;
    }
  }

  return intercetLen;
}

function solution(K, L, M, N, P, Q, R, S) {
  const width1 = M - K;
  const height1 = N - L;
  const area1 = width1 * height1;

  const width2 = R - P;
  const height2 = S - Q;
  const area2 = width2 * height2;

  let intercetArea = 0;
  const intercetLen1 = getIntercet([K, M], [P, R]);
  const intercetLen2 = getIntercet([L, N], [Q, S]);
  if (intercetLen1 > 0 && intercetLen2 > 0) {
    intercetArea = intercetLen1 * intercetLen2;
  }

  const total = area1 + area2 - intercetArea;
  // console.log(total);

  return total;
}
module.exports = solution;
