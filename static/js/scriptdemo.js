 // Function to add new entry to the dataset and expense table  
function addItem() { 
    let type = itemType.value; 
    let name = document.getElementById("name"); 
    let category = document.getElementById("category");
    let date = document.getElementById("Date");
    let amount = document.getElementById("amount"); 
    const today = new Date();
        
    // Get the day, month, and year
    const day = today.getDate();
    const month = today.getMonth() + 1;
    const year = today.getFullYear();

    // Format the date as needed
    const formattedDate = `${year}-${month < 10 ? '0' + month : month}-${day < 10 ? '0' + day : day}`;
    // Input validation 
    if (name.value === "" || Number(amount.value) === 0) 
        return alert("Incorrect Input"); 
    if (date.value === "" || date.value>formattedDate)
        return alert("Invalid Date"); 
    if (Number(amount.value) <= 0) 
        return alert( 
            "Incorrect amount! can't add negative"
        ); 
  
    // Push new data 
    tableEntries.push({ 
        type: Number(type), 
        name: name.value, 
        category: category.value,
        date: date.value,
        amount: Number(amount.value), 
    }); 
  
    updateTable(); 
    name.value = "";
    category.value =""; 
    date.value="";
    amount.value = 0; 
} 
  
// Function to load all entry in the expense table 
function loadItems(e, i) { 
    let cls; 
    let table = document.getElementById("table"); 
    let row = table.insertRow(i + 1); 
    let cell0 = row.insertCell(0); 
    let cell1 = row.insertCell(1); 
    let cell2 = row.insertCell(2); 
    let c3 = row.insertCell(3); 
    let c4 = row.insertCell(4); 
    let c5 = row.insertCell(5);
    let c6 = row. insertCell(6);
    cell0.innerHTML = i + 1; 
    cell1.innerHTML = e.name; 
    cell2.innerHTML = e.category;
    c3.innerHTML = e.date; 
    c4.innerHTML = e.amount;
    c6.innerHTML = "☒"; 
    c6.classList.add("zoom"); 
    c6.addEventListener("click", () => del(e)); 
    if (e.type == 0) { 
        cls = "red"; 
        c5.innerHTML = "➚"; 
    } else { 
        cls = "green"; 
        c5.innerHTML = "➘"; 
    } 
    c5.style.color = cls;
    
} 
  
// Clear the table before updation 
function remove() { 
    while (table.rows.length > 1) table.deleteRow(-1); 
} 
  
// Function to delete a specific entry 
function del(el) { 
    remove(); 
    tableEntries = tableEntries.filter( 
        (e) => e.name !== el.name 
    ); 
    tableEntries.map((e, i) => loadItems(e, i)); 
    updateSummary(); 
} 
  
// To render all entries 
function updateTable() { 
    remove(); 
    updateSummary(); 
    tableEntries.map((e, i) => {loadItems(e, i);}); 
    
} 
function updateSummary() { 
    let totalIncome = tableEntries.reduce((t, e) => { 
        if (e.type === 1) t += e.amount; 
        return t; 
    }, 0); 
    let totalExpense = tableEntries.reduce((ex, e) => { 
        if (e.type === 0) ex += e.amount; 
        return ex; 
    }, 0); 
    if (totalIncome<=totalExpense)
    { return alert("Expense cannot be greater than Income");
      }
      else{
        updatedInc.innerText = totalIncome; 
        updatedExp.innerText = totalExpense; 
        updatedBal.innerText = totalIncome - totalExpense;
      }
} 
let tableEntries = [ 
    
]; 
  
