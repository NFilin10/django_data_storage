// Get Elements
const dropZone = document.getElementById('drop-zone');
const fileInput = document.getElementById('file-input');
const fileNames = document.getElementById('file-names');

// Add Drag and Drop Event Listeners
dropZone.addEventListener('dragover', function(e) {
  e.preventDefault();
  e.stopPropagation();
});

dropZone.addEventListener('drop', function(e) {
  e.preventDefault();
  e.stopPropagation();
  fileInput.files = e.dataTransfer.files;
  displayFileNames();
});

// Add File Input Event Listener
fileInput.addEventListener('change', function() {
  displayFileNames();
});

// Add Drop Zone Click Event Listener
dropZone.addEventListener('click', function() {
  fileInput.click();
});

// Display File Names
function displayFileNames() {
  const files = fileInput.files;
  while (fileNames.firstChild) {
    fileNames.removeChild(fileNames.firstChild);
  }
  if (files.length === 0) {
    fileNames.innerHTML = '<p>No files selected</p>';
  } else {
    for (let i = 0; i < files.length; i++) {
      const div = document.createElement('div');
      div.classList.add('file-name-card');
      div.innerHTML = '<i class="fa fa-file-o file-icon"></i>' + files[i].name;
      fileNames.appendChild(div);
    }
  }
}

