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

function showModal(modalName,event) {
    event.preventDefault(); 
  
    const button = document.getElementById("calBtn");
    const modal = document.getElementById(modalName);
  
    const rect = button.getBoundingClientRect();
    console.log(rect.top);
    console.log(window.scrollY);
    if (modal === "priorityModal"){
      modal.style.top = `${window.scrollY + rect.top + rect.height }`;
    }else{
    modal.style.top = `${window.scrollY - 10}px`;

    }
    // modal.style.left = `${rect.left}px`;
    modal.style.display = "block"; 
  }
  
  function hideModal(modalName) {
    const modal = document.getElementById(modalName);
    modal.style.display = "none";
  }
  
  function setDueDate() {
    const dueDateInput = document.getElementById("due_date_input").value;
  
    if (dueDateInput) {
      document.getElementById("due_date").value = dueDateInput;
  
      hideModal('dueDateModal');
    } else {
      alert("Please select a due date.");
    }
  }
