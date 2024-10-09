# S3 File Upload with KMS Encryption

This project demonstrates how to upload files to an Amazon S3 bucket with server-side encryption using AWS KMS (Key Management Service). The script uses the `boto3` library to interact with AWS services and securely manages credentials and configuration using environment variables.

## Features

- Upload files to a specified S3 bucket.
- Server-side encryption with AWS KMS.
- Secure credential management using environment variables and `.env` file.

## Prerequisites

To run this project, ensure you have the following installed:

- Python 3.x
- AWS Account with access to S3 and KMS
- `boto3` and `python-dotenv` libraries

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/m4n1nh0/bucket-upload.git
   cd bucket-upload
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root directory with the following content, replacing the placeholder values with your actual AWS credentials and bucket/KMS information:
   ```bash
   AWS_ACCESS_KEY_ID=your_aws_access_key_id
   AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
   S3_BUCKET_NAME=your_s3_bucket_name
   KMS_KEY_ID=your_kms_key_id
   ```

## Usage

1. Ensure your `.env` file is correctly configured with the necessary credentials and identifiers.
   
2. Upload a file to the S3 bucket by running the script:

   ```bash
   python bucket.py
   ```

   The file specified in the script (`file_to_upload.txt`) will be uploaded to the bucket with the KMS encryption key.

## Environment Variables

The script relies on the following environment variables:

- `AWS_ACCESS_KEY_ID`: Your AWS access key ID.
- `AWS_SECRET_ACCESS_KEY`: Your AWS secret access key.
- `S3_BUCKET_NAME`: The name of your S3 bucket.
- `KMS_KEY_ID`: The ID of the KMS key for encryption.

## Error Handling

- If the file is not found: A message will be printed: `"The file was not found"`.
- If credentials are missing: The script will notify that `"Credentials not available"`.
- In case of other AWS client errors, a detailed message will be printed.

## Security Considerations

- **Do not share the `.env` file** with sensitive information in version control. Make sure to add `.env` to your `.gitignore` file.
- Consider using AWS IAM roles or AWS Secrets Manager for managing credentials in production environments.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

### Additional Notes:
1. The placeholder URLs should be updated to the correct repository location if applicable.
2. Ensure you include a `requirements.txt` file with the dependencies, which should contain:
   ```text
   boto3
   python-dotenv
   ```