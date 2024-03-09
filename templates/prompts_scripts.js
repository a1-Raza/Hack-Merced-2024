
document.addEventListener('DOMContentLoaded', function() {
    const promptForm = document.getElementById('promptForm');
    const promptList = document.getElementById('promptList');
  
    promptForm.addEventListener('submit', function(event) {
      event.preventDefault();
  
      const promptText = document.getElementById('promptText').value.trim();
  
      if (promptText !== '') {
        createPrompt(promptText);
      } else {
        alert('Please enter a prompt.');
      }
  
      promptForm.reset();
    });
  
    function createPrompt(promptText) {
      const promptItem = document.createElement('div');
      promptItem.classList.add('prompt-item');
      promptItem.innerHTML = `<p>${promptText}</p>`;
      promptList.appendChild(promptItem);
    }
  });
  