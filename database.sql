import ocr_service
import csv_service

def process_upload(image_path, metadata):
    try:
        text_data = ocr_service.extract_text(image_path)
        if text_data:
            csv_path = csv_service.create_csv(text_data, metadata)
            update_database_status(metadata['user_id'], 'success', csv_path)
            return {'status': 'success', 'csv_path': csv_path}
        else:
            update_database_status(metadata['user_id'], 'failure')
            return {'status': 'failure', 'message': 'OCR failed to extract text.'}
    except Exception as e:
        update_database_status(metadata['user_id'], 'error')
        return {'status': 'error', 'message': str(e)}