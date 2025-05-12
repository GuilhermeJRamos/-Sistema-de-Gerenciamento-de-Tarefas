function hasUniqueCharacters(str) {
    const charSet = new Set();
    for (let char of str) {
        if (charSet.has(char)) {
            return false; // Caractere repetido encontrado
        }
        charSet.add(char);
    }
    return true; // Todos os caracteres são únicos
}

// Teste a função
console.log(hasUniqueCharacters("abcdefg")); // true
console.log(hasUniqueCharacters("abcdeaf")); // false
console.log(hasUniqueCharacters("")); // true
console.log(hasUniqueCharacters("a")); // true
console.log(hasUniqueCharacters("a b c!")); // true
console.log(hasUniqueCharacters("1234567890")); // true
console.log(hasUniqueCharacters("1234512345")); // false