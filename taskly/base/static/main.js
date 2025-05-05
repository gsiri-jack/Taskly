function openUpdateModal(taskId) {
  fetch(`update-task/${taskId}/`)
    .then((response) => response.text())
    .then((html) => {
      document.getElementById("modalContent").innerHTML = html;
      new bootstrap.Modal(document.getElementById("updateTaskModal")).show();
    });
}

function submitUpdateForm(event, form) {
  event.preventDefault();
  const formData = new FormData(form);

  fetch(form.action, {
    method: "POST",
    body: formData,
  })
    .then((res) => res.json())
    .then((data) => {
      if (data.success) {
        location.reload();
      }
    });
}

function toggleTask(taskId, checkbox) {
  fetch(`toggle-task/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
      "X-CSRFToken": getCookie("csrftoken"), // Add this function below
    },
    body: `task_id=${taskId}`,
  })
    .then((response) => response.json())
    .then((data) => {
      const textElement = document.getElementById(`task-text-${taskId}`);
      if (data.completed) {
        textElement.classList.add("completed");
        console.log(textElement.classList);
      } else {
        textElement.classList.remove("completed");
        console.log("no", textElement.classList);
      }
    });
}
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

function showDueDateModal(event) {
    event.preventDefault(); // Prevent default behavior
  
    const button = document.getElementById("calBtn");
    const modal = document.getElementById("dueDateModal");
  
    // Get the button's position and dimensions
    const rect = button.getBoundingClientRect();
  
    // Set the modal's position relative to the button
    // modal.style.position = "rel";
    modal.style.top = `${window.scrollY}px`; // Adjust for scrolling
    modal.style.left = `${rect.left + rect.width + 10}px`; // Place it to the right of the button with a 10px margin
    modal.style.display = "block"; // Make the modal visible
  }
  
  function hideDueDateModal() {
    const modal = document.getElementById("dueDateModal");
    modal.style.display = "none"; // Hide the modal
  }
  
  function setDueDate() {
    const dueDateInput = document.getElementById("due_date_input").value;
  
    if (dueDateInput) {
      // Set the due date in the form input
      document.getElementById("due_date").value = dueDateInput;
  
      // Hide the modal
      hideDueDateModal();
    } else {
      alert("Please select a due date.");
    }
  }