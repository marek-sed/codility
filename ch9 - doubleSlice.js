function maxSlice(col, start, end) {
  function next(i) {
      return start < end ? i + 1 : i - 1;
  }
  function hasNext(i) {
      return start < end ? i < end : i > end   
  }
  function previous(i) {
      return start < end ? i - 1 : i + 1;
  }
  
  const max = []
  max[previous(start)] = 0
  let bestStart = 0
  for (let i = start; hasNext(i); i = next(i)) {
      const v = (max[previous(i)] || 0) + col[i]
      if(v < 0) {
          bestStart = i
      }
      max[i] = Math.max(v, 0)
  }
  
  return [bestStart, max]
}

function solution(A) {
  
  const [lrS, lr] = maxSlice(A, 1, A.length -1)
  const [rlS, rl] = maxSlice(A, A.length - 2, 0)
  rl.shift()
  
  let maxVal = 0
  for(let i = 0; i < lr.length - 1; i++) {
     maxVal = Math.max(maxVal, lr[i] + rl[i + 1])
  }
  
  return maxVal
}