from google.cloud import bigquery
from bloom_filter import BloomFilter  # Ensure bloom_filter.py is in the same directory

def save_to_bigquery():
    client = bigquery.Client()
    table_id = "nimble-courier-449405-f7.my_dataset.fruit_bloom_filter"  # Replace with your actual project ID & dataset name

    bloom_filter = BloomFilter()

    # Add fruits to the Bloom filter
    fruits = ["apple", "banana", "grape", "mango", "orange","water","pen"]
    for fruit in fruits:
        bloom_filter.add(fruit)

    base64_state = bloom_filter.get_state()

    rows_to_insert = [{"bit_array": base64_state}]

    errors = client.insert_rows_json(table_id, rows_to_insert)
    if errors:
        print("Errors:", errors)
    else:
        print("Bloom filter saved to BigQuery.")

# Run the function when executing the script
if __name__ == "__main__":
    save_to_bigquery()

