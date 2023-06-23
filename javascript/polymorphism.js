// This example demostrate the polymorphism in javascript
// The polymorphism is the ability to use an object in different ways.
// In javascript, we can use the closure to implement the polymorphism.

// Example 1
// The following example demostrate the polymorphism

// Person
function Person(name, age) {
    this.name = name;
    this.age = age;
}

Person.prototype.getName = function() {
    return this.name;
}

//Employee
function Employee(name, age, salary) {
    Person.call(this, name, age);
    this.salary = salary;
}

Employee.prototype = Object.create(Person.prototype);
Employee.prototype.constructor = Employee;

Employee.prototype.getSalary = function() {
    return this.salary;
}

Employee.prototype.getName = function() {
    return this.name + " (Employee)";
}

//Customer
function Customer(name, age, address) {
    Person.call(this, name, age);
    this.address = address;
}

Customer.prototype = Object.create(Person.prototype);
Customer.prototype.constructor = Customer;

Customer.prototype.getAddress = function() {
    return this.address;
}

Customer.prototype.getName = function() {
    return this.name + " (Customer)";
}

var employee = new Employee("John", 30, 10000);
console.log(employee.getName());
console.log(employee.getSalary());

var customer = new Customer("John", 30, "New York");
console.log(customer.getName());
console.log(customer.getAddress());

// Output:
// John (Employee)
// 10000
// John (Customer)
// New York
