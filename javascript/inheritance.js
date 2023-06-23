// This example demostrate the inheritance in javascript

// Example 1
// The following example demostrate the inheritance
function Person(name, age) {
    this.name = name;
    this.age = age;
}

Person.prototype.getName = function() {
    return this.name;
}

function Employee(name, age, salary) {
    Person.call(this, name, age);
    this.salary = salary;
}

Employee.prototype = Object.create(Person.prototype);
Employee.prototype.constructor = Employee;

Employee.prototype.getSalary = function() {
    return this.salary;
}

var employee = new Employee("John", 30, 10000);
console.log(employee.getName());
console.log(employee.getSalary());

// Output:
// John
// 10000