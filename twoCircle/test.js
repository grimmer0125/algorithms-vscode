function solution(x1, y1, r1, x2, y2, r2) {
  const centerD = Math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));

  if ((r1 + r2) < centerD) {
    return 0;
  }

  const r1sq = r1 * r1;
  const r2sq = r2 * r2;

  // one circle is inside another circle
  if (r1 >= r2 && Math.abs(r1 - r2) >= centerD) {
    return Math.PI * r2sq;
  } else if (r1 < r2 && Math.abs(r1 - r2) >= centerD) {
    return Math.PI * r1sq;
  }

  // overlap, get interception area
  const theta1 = (Math.acos((r1sq + (centerD * centerD) - r2sq) / (2 * r1 * centerD))) * 2;
  const theta2 = (Math.acos((r2sq + (centerD * centerD) - r1sq) / (2 * r2 * centerD))) * 2;
  const area1 = 0.5 * r1sq * (theta1 - Math.sin(theta1));
  const area2 = 0.5 * r2sq * (theta2 - Math.sin(theta2));

  return area1 + area2;
}

const a = solution(2, 2, 3, 5, 5, 3);
console.log(a);
