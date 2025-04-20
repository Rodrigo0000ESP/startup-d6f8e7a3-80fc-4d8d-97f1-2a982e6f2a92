const fileInput = document.getElementById('fileInput');

fileInput.addEventListener('change', async function(event) {
  const file = event.target.files[0];

  const formData = new FormData();
  formData.append('receiptImage', file);

  const ocrResponse = await fetch('/api/ocr', {
    method: 'POST',
    body: formData
  });

  const ocrData = await ocrResponse.json();

  const csvResponse = await fetch('/api/csv', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      textData: ocrData
    })
  });

  const csvData = await csvResponse.json();

  // Display or allow download of csvData
});