function validateForm() {
  const weight = Number.parseFloat(document.forms["bmiForm"]["weight"].value)
  const height = Number.parseFloat(document.forms["bmiForm"]["height"].value)

  // Clear previous error messages
  const existingError = document.querySelector(".error-message")
  if (existingError) {
    existingError.remove()
  }

  if (!weight || !height || isNaN(weight) || isNaN(height)) {
    showError("Please enter valid numeric values for both fields.")
    return false
  }

  if (weight <= 0) {
    showError("Weight must be greater than 0.")
    return false
  }

  if (height <= 0) {
    showError("Height must be greater than 0.")
    return false
  }

  if (weight < 10) {
    showError("Weight must be at least 10 kg.")
    return false
  }

  if (weight > 600) {
    showError("Weight must be ≤ 600 kg.")
    return false
  }

  if (height < 50) {
    showError("Height must be at least 50 cm.")
    return false
  }

  if (height > 272) {
    showError("Height must be ≤ 272 cm.")
    return false
  }

  return true
}

function showError(message) {
  const form = document.querySelector("form")
  const errorDiv = document.createElement("div")
  errorDiv.className = "error-message"
  errorDiv.textContent = message
  form.appendChild(errorDiv)
}

// Add smooth input animations
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".input-field").forEach((input) => {
    input.addEventListener("focus", function () {
      this.style.transform = "translateY(-2px)"
    })

    input.addEventListener("blur", function () {
      this.style.transform = "translateY(0)"
    })
  })
})
