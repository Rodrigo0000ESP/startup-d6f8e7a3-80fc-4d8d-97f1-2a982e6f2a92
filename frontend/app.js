const fs = require('fs');

function generateCSV(receiptData) {
  const { date, amount, hotelName } = receiptData;

  const csvData = `Date,Amount,Hotel Name
${date},${amount},${hotelName}`;

  fs.writeFile('receipt_data.csv', csvData, (err) => {
    if (err) {
      console.error(err);
    } else {
      console.log('CSV file generated successfully');
    }
  });
}

const extractedReceiptData = {
  date: '2022-01-01',
  amount: 100.50,
  hotelName: 'Example Hotel'
};

generateCSV(extractedReceiptData);