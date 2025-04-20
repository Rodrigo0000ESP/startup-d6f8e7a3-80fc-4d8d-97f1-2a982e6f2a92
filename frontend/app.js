const extractedData = receiveExtractedReceiptData();

const categorizedData = categorizeData(extractedData);

const csvData = generateCSV(categorizedData);

return csvData;