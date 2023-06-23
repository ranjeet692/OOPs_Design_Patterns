// This example demostrate the encapsulation in javascript
// The encapsulation is the process of hiding the implementation details from the user.
// In javascript, we can use the closure to implement the encapsulation.
// The closure is a function that has access to the outer function's variables.
// The closure has three scope chains:
// 1. Own scope where variables defined between its curly brackets
// 2. Outer function's variables
// 3. Global variables

// Example 1
// The following example demostrate the closure
function outerFunction() {
    var outerVariable = 10;
    function innerFunction() {
        console.log(outerVariable);
    }
    return innerFunction;
}
var innerFunction = outerFunction();
innerFunction();

// Example 3
function Person(name, age) {
    this.name = name;
    this.age = age;
}

Person.prototype.getName = function() {
    return this.name;
}

Person.prototype.getAge = function() {
    return this.age;
}

var person = new Person("John", 30);
console.log(person.getName());
console.log(person.getAge());

// Output:
// John
// 30