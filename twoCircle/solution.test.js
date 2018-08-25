const solution = require('./solution');

test('test twoCircle', () => {
  const diff = solution(2, 2, 3, 5, 5, 3) - 5.137;
  expect(diff).toBeLessThan(0.001);
});
