document.addEventListener('DOMContentLoaded', function() {
  const promptInput = document.getElementById('promptInput');

  // Hide placeholder text when the textarea is focused
  promptInput.addEventListener('focus', function() {
      promptInput.placeholder = '';
  });

  // Show placeholder text when the textarea loses focus and is empty
  promptInput.addEventListener('blur', function() {
      if (promptInput.value.trim() === '') {
          promptInput.placeholder = 'Type your input';
      }
  });

  // Adjust textarea height dynamically based on content
  promptInput.addEventListener('input', function() {
      promptInput.style.height = 'auto';
      promptInput.style.height = promptInput.scrollHeight + 'px';
  });

  // Trigger input event on page load to initialize the textarea
  promptInput.dispatchEvent(new Event('input'));
});
