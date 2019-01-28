let recursion = (num) => {
    if num === 1 {
        return 1
    }
    else {
        return num * recursion(num - 1)
    }
}
console.log(recursion(5))
