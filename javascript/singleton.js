// This example demostrate the singleton in javascript
// The singleton is a design pattern that restricts the instantiation of a class to one object.

// Example 1
// The following example demostrate the singleton
var singleton = (function() {
    var instance;
    function init() {
        var name = "John";
        function getName() {
            return name;
        }
        return {
            getName: getName
        }
    }
    return {
        getInstance: function() {
            if (!instance) {
                instance = init();
            }
            return instance;
        }
    }
})();

var singleton1 = singleton.getInstance();
var singleton2 = singleton.getInstance();

console.log(singleton1.getName());
console.log(singleton2.getName());

// Output:
// John
// John