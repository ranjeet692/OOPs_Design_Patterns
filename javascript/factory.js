// This example demostrate the factory in javascript
// The factory is a design pattern that creates objects without exposing the instantiation logic to the client.
// The factory design pattern is useful when we have a super class with multiple sub-classes and based on input, we need to return one of the sub-class.
// The factory design pattern provides approach to code for interface rather than implementation.

// Example 1
// The following example demostrate the factory
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

function Customer(name, age, address) {
    Person.call(this, name, age);
    this.address = address;
}

Customer.prototype = Object.create(Person.prototype);
Customer.prototype.constructor = Customer;

Customer.prototype.getAddress = function() {
    return this.address;
}

function Factory() {
    this.create = function(type, name, age, value) {
        switch (type) {
            case "employee":
                return new Employee(name, age, value);
                break;
            case "customer":
                return new Customer(name, age, value);
                break;
            default:
                return new Person(name, age);
        }
    }
}

var factory = new Factory();
var employee = factory.create("employee", "John", 30, 10000);
console.log(employee.getName());
console.log(employee.getSalary());

var customer = factory.create("customer", "John", 30, "New York");
console.log(customer.getName());
console.log(customer.getAddress());

// Output:
// John
// 10000
// John
// New York