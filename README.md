# bloom-filter
# Bloom Filter Implementation with Google BigQuery

This repository contains a simple implementation of a Bloom Filter in Python, integrated with Google BigQuery for storing and retrieving filter states.

## Features
- Implements a Bloom Filter for approximate membership testing.
- Stores the Bloom Filter state in BigQuery.
- Loads the state from BigQuery to check for membership.

## Prerequisites
Before running the scripts, ensure you have the following:
- Python 3.x installed.
- Google Cloud SDK installed and authenticated.
- A Google Cloud project with BigQuery enabled.
- A BigQuery dataset and table to store the Bloom Filter state.

## Setup
1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Install required dependencies:**
   ```sh
   pip install google-cloud-bigquery
   ```

3. **Set up Google Cloud authentication:**
   ```sh
   gcloud auth application-default login
   ```

## Usage
### 1. Upload Bloom Filter State to BigQuery
Run the following script to create a Bloom Filter, add items, and store the state in BigQuery:
```sh
python upload_bloom.py
```

### 2. Check Membership in the Bloom Filter
Run the following script to check if an item is present in the Bloom Filter:
```sh
python test_bloom_filter.py
```
Example output:
```
✅ 'apple' is likely present in the Bloom filter.
❌ 'kiwi' is NOT present in the Bloom filter.
```

## Files
- `bloom_filter.py` - Implementation of the Bloom Filter.
- `upload_bloom.py` - Adds items to the Bloom Filter and uploads the state to BigQuery.
- `test_bloom_filter.py` - Loads the Bloom Filter state from BigQuery and checks for item presence.

## BigQuery Table Schema
Ensure your BigQuery table has the following schema:
| Column Name | Type     |
|------------|---------|
| bit_array  | STRING  |

## Troubleshooting
- If authentication issues occur, ensure you are authenticated with:
  ```sh
  gcloud auth application-default login
  ```
- If `IndexError: list index out of range` occurs, verify that the Bloom Filter size matches in both upload and test scripts.
- If `AttributeError: 'BloomFilter' object has no attribute 'set_state'`, use `load_state()` instead of `set_state()`.

## Contributing
Feel free to fork this repository and submit pull requests with improvements or fixes.

## License
This project is licensed under the MIT License.
