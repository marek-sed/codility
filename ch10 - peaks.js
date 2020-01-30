function solution(A) {
  // write your code in JavaScript (Node.js 8.9.4)
  // 1 2 3 4 3 4 1 2 3 4 6 2
  const n = A.length
  const peaks = []
  if(n < 3) return 0
  
  for (let i = 1; i < A.length; i++) {
      if(A[i - 1] < A[i] && A[i] > A[i+1]) {
        peaks.push(i)
      }
  }
  
  if (peaks.length === 0) return 0
  
  for(let i = peaks.length; i > 0; i--) {
      if (n % i !== 0) continue 
      
      var d = Math.floor(n / i)
      const found = Array(i).fill(0)
      let count = 0
      for(let j = 0; j < peaks.length; j++) {
          const group = Math.floor(peaks[j] /  d)
          if(found[group] === 0) {
              found[group] = 1
              count++
          }
          if (count === i) {
              return i
          }
      }
  }
  
  return 0
}