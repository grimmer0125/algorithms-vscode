// https://en.wikipedia.org/wiki/Breadth-first_search
function solution(data, queryParam1, queryParam2) {

  let currentLevelList = [];
  let nextLevelList = [];
  currentLevelList.push(data);

  while (currentLevelList.length > 0) {
    // console.log('currentLevelList:')
    for (const node of currentLevelList) {
      // console.log('node:', node)
      if (node[queryParam1] && node.[queryParam2]) {
        console.log(`${node[queryParam1]} ${node[queryParam2]}`);
      } else {
        // no gameCode, no recordId
      }

      if (node.children && node.children.length > 0) {
        nextLevelList = nextLevelList.concat(node.children);
      }
    }
    currentLevelList = nextLevelList;
    nextLevelList = [];
  }
}
