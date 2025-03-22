document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('upload-form');
    const fileInput = document.getElementById('file-input');
    const fileInputText = document.getElementById('file-input-text');
    const submitBtn = document.getElementById('submit-btn');
    const resultsSection = document.getElementById('results-section');
    const originalImage = document.getElementById('original-image');
    const processedImage = document.getElementById('processed-image');
    const downloadBtn = document.getElementById('download-btn');
    const tryAgainBtn = document.getElementById('try-again-btn');
    const loadingElement = document.getElementById('loading');

    // Handle file selection
    fileInput.addEventListener('change', function() {
        if (fileInput.files.length > 0) {
            const file = fileInput.files[0];
            // Check if file is an image
            if (!file.type.match('image/(jpeg|jpg|png)')) {
                alert('Please select a valid image file (JPG, JPEG, or PNG)');
                fileInput.value = '';
                fileInputText.textContent = 'Choose an image';
                submitBtn.disabled = true;
                return;
            }
            
            fileInputText.textContent = file.name;
            submitBtn.disabled = false;
            
            // Show original image preview
            const reader = new FileReader();
            reader.onload = function(e) {
                originalImage.src = e.target.result;
            };
            reader.readAsDataURL(file);
        } else {
            fileInputText.textContent = 'Choose an image';
            submitBtn.disabled = true;
        }
    });

    // Handle form submission
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        if (fileInput.files.length === 0) {
            return;
        }
        
        // Show loading
        loadingElement.style.display = 'block';
        resultsSection.style.display = 'none';
        
        const formData = new FormData();
        formData.append('file', fileInput.files[0]);
        
        fetch('/remove-bg', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            // Hide loading
            loadingElement.style.display = 'none';
            
            // Get the processed image URL
            const processedImageUrl = `/processed/${data.filename}`;
            
            // Update UI with the processed image
            processedImage.src = processedImageUrl;
            downloadBtn.href = processedImageUrl;
            
            // Show results
            resultsSection.style.display = 'block';
        })
        .catch(error => {
            console.error('Error:', error);
            loadingElement.style.display = 'none';
            alert('An error occurred while processing your image. Please try again.');
        });
    });

    // Try again button
    tryAgainBtn.addEventListener('click', function() {
        resultsSection.style.display = 'none';
        fileInput.value = '';
        fileInputText.textContent = 'Choose an image';
        submitBtn.disabled = true;
    });
});