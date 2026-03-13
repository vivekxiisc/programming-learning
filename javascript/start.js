console.log("vivek");
let tasks = ["Wash dishes"];
console.log(tasks)
tasks.push("Do laundry", "Buy groceries");
console.log(tasks); // ["Wash dishes", "Do laundry", "Buy groceries"]

// let completedTask = tasks.pop();
// console.log(completedTask); // "Buy groceries"
// tasks.pop("Buy groceries");
tasks.pop();
console.log(tasks);       // ["Wash dishes", "Do laundry"]
let names = ["Alice", "Bob", "Charlie"];

for (const name of names) {
  console.log(`Hello, ${name}!`);
}

